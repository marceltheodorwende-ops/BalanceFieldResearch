import importlib.util,json,sys,contextlib,io
from pathlib import Path
root=Path(__file__).resolve().parent
package=root.parent/'package'; sys.path.insert(0,str(package))
out=root/'fresh_verification'; out.mkdir(exist_ok=True)
research=package/'research/bfg-fundamental-closure'
for filename in ['audit_consistency.py','stress_csr.py','stress_neutral_contrast.py']:
    spec=importlib.util.spec_from_file_location(filename[:-3],research/filename)
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    if filename=='audit_consistency.py':
        capture=io.StringIO()
        with contextlib.redirect_stdout(capture): module.main()
        result=json.loads(capture.getvalue())
    else:
        result=module.run_batch()
    (out/(filename[:-3]+'.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(filename,json.dumps(result),flush=True)

