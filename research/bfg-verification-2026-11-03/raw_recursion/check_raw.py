"""Exact controls for source raw composition and conditional reconstruction."""
from pathlib import Path
import json
import sympy as s

OUT=Path(__file__).resolve().parent
I=s.eye(2);J=s.diag(1,2);E=J.inv();B=I;N=I
fa=s.diag(1,s.Rational(1,8));fb=s.diag(1,s.Rational(1,4))
ra=J*fa*J;rb=J*fb*J;e=s.Matrix([1,0])
assert ra==s.diag(1,s.Rational(1,2)) and rb==I
assert E*J==B*N==I
assert ra*e==rb*e==e
assert [len((r-I).nullspace()) for r in [ra,rb]]==[1,2]
assert J.inv()*ra*J.inv()==fa
Js=s.diag(1,0);Rs=s.diag(3,0);Jplus=Js
assert Js*(Jplus*Rs*Jplus)*Js==Rs
assert Rs.rank()<=Js.rank()
assert Js*I*Js!=I
t=s.symbols('t',nonnegative=True)
phi1,inf1=s.Integer(1),1+t
phi2,inf2=1+t,s.Integer(1)
assert phi1.subs(t,0)==phi2.subs(t,0)==inf1.subs(t,0)==inf2.subs(t,0)==1
assert phi1*inf1==phi2*inf2
assert s.diff(phi1*inf1,t)==s.diff(phi2*inf2,t)==1
assert s.diff(phi1,t)!=s.diff(phi2,t)
# Independent finite fixture for the exact interface equation and its inverse.
a,b,g,d=s.symbols('a b g d',nonzero=True,real=True)
NN=s.Matrix([[2,0],[0,3]]);Nstar=I
EE=s.Matrix([[1,1],[0,2]]);BB=s.diag(2,4)
FF=s.Matrix([[1,2],[3,4]])
dotN=-a*(NN-Nstar)+b*(EE*BB-BB*EE)+g*FF-d*NN**2
recovered=s.simplify((dotN+a*(NN-Nstar)-b*(EE*BB-BB*EE)+d*NN**2)/g)
assert recovered==FF and J*recovered*J==J*FF*J
assert dotN.subs(g,0)==(-a*(NN-Nstar)+b*(EE*BB-BB*EE)-d*NN**2)
# The source's two neutral conventions have different spectra for the same inputs.
M=I/s.sqrt(2)
RN=s.simplify(M.inv()*I*M.inv());RC=s.simplify(M*I*M)
assert RN==2*I and RC==I/2
report={'status':'PASS','date':'2026-11-03',
 'raw_composition_defined_conditionally':True,
 'same_primitive_coupling_balance_two_feedback_factors':True,
 'comparison_persistent_ranks':[1,2],
 'scalar_feedback_product_identity_alone_unique_flow':False,
 'neural_interface_reconstruction_given_complete_instantaneous_data':True,
 'gamma_zero_recovers_feedback_factor':False,
 'original_normalization_equals_later_conjugate_mediation':False,
 'primitive_factors_derived_from_fresh_formation_in_inspected_axiom':False,
 'unique_fundamental_initial_R_derived':False,
 'new_physical_rule_adopted':False,'event_rule_modified':False,
 'scope':'Exact finite diagnostic implications and direct source trace; no full-source independence or cognitive/physical validation'}
(OUT/'results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
