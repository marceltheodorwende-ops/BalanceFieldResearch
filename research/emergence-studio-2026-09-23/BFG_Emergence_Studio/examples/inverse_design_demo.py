from bfg_studio import NumericalPolicy, ReferenceGramCarrier
from bfg_studio.search import inverse_design
hits=inverse_design(trials=200,dim=6,persistent_rank=4,steps=8,
                    carrier=ReferenceGramCarrier(),policy=NumericalPolicy(),seed=4,top_k=5)
for h in hits:
    print(h.score,h.seed,h.run.summary())
