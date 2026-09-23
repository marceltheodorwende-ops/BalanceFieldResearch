"""
Template for a domain-specific BFG carrier.

A real material / biological / network / agent model should implement
how the mathematically computed BFG reclosure candidate reconstructs
the next carrier-specific state. Keep the generic reclosure equations
in bfg_studio.core unchanged.
"""
from bfg_studio import CarrierAdapter, BFGState

class MyDomainCarrier(CarrierAdapter):
    def advance(self, previous, step, policy):
        if not step.success:
            return BFGState(
                D=previous.D, K=previous.K, Y=previous.Y, R_C=previous.R_C,
                generation=previous.generation+1,
                terminal=True,
                terminal_reason=step.terminal_reason
            )

        # Replace these four lines with independently justified carrier physics.
        D_next = previous.D
        K_next = previous.K
        Y_next = previous.Y
        R_next = previous.R_C

        return BFGState(
            D=D_next, K=K_next, Y=Y_next, R_C=R_next,
            generation=previous.generation+1,
            metadata={**previous.metadata, "carrier":"MyDomainCarrier"}
        )
