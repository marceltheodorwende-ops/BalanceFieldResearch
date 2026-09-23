from bfg_studio import (
    DomainInvariantSummary,
    corridor_overlap,
)

def test_corridor_overlap_detects_shared_interval():
    a=DomainInvariantSummary(
        carrier_id="a",samples=10,successful_reclosures=10,
        novelty_fraction_among_successful=1.0,
        metrics={"neutral_retention":{
            "mean":0.5,"std":0.1,"q10":0.3,"q25":0.4,"median":0.5,
            "q75":0.6,"q90":0.7,"min":0.2,"max":0.8
        }}
    )
    b=DomainInvariantSummary(
        carrier_id="b",samples=10,successful_reclosures=10,
        novelty_fraction_among_successful=1.0,
        metrics={"neutral_retention":{
            "mean":0.55,"std":0.1,"q10":0.4,"q25":0.45,"median":0.55,
            "q75":0.65,"q90":0.8,"min":0.3,"max":0.9
        }}
    )
    c=corridor_overlap([a,b],"neutral_retention")
    assert c["shared"]
    assert c["lower"]==0.4
    assert c["upper"]==0.7
    assert c["overlap_ratio"]>0

def test_corridor_overlap_can_be_empty():
    a=DomainInvariantSummary(
        carrier_id="a",samples=1,successful_reclosures=1,
        novelty_fraction_among_successful=1.0,
        metrics={"omega_keep":{
            "mean":0.1,"std":0.0,"q10":0.1,"q25":0.1,"median":0.1,
            "q75":0.1,"q90":0.2,"min":0.1,"max":0.2
        }}
    )
    b=DomainInvariantSummary(
        carrier_id="b",samples=1,successful_reclosures=1,
        novelty_fraction_among_successful=1.0,
        metrics={"omega_keep":{
            "mean":0.8,"std":0.0,"q10":0.7,"q25":0.8,"median":0.8,
            "q75":0.8,"q90":0.9,"min":0.7,"max":0.9
        }}
    )
    c=corridor_overlap([a,b],"omega_keep")
    assert not c["shared"]
    assert c["lower"] is None
    assert c["upper"] is None
