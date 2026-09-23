from bfg_studio import (
    BFGState,
    CarrierSchema,
    ExternalCarrierTemplate,
    NumericalPolicy,
)

schema = CarrierSchema(
    name="My Fixed External Carrier",
    domain="replace-with-domain",
    description="Declare the independently fixed measurement-to-BFG mapping.",
    measurement_mapping={
        "D": "replace with measured state-vector construction",
        "K": "replace with measured formation-operator construction",
        "Y": "replace with positive neutral-load construction",
        "R_C": "replace with recursively justified transition construction",
    },
    invariant_parameters={
        "important": "parameters must be fixed before held-out evaluation",
    },
)

class MyExternalCarrier(ExternalCarrierTemplate):
    def __init__(self):
        super().__init__(schema)

    def map_measurement_to_state(self, measurement, *, generation=0):
        # Implement with independently justified domain equations.
        raise NotImplementedError

    def advance(self, previous, step, policy: NumericalPolicy):
        # Implement domain-specific reconstruction after generic BFG reclosure.
        raise NotImplementedError
