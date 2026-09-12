"""External reference markets: what venues other than Kalshi think a tennis match is worth."""
from tennis_edge.external_market.schema import (  # noqa: F401
    ExternalMarketObservation, ExternalStore, ExternalMarketError, SOURCE_KINDS,
)
from tennis_edge.external_market.devig import (  # noqa: F401
    american_to_decimal, decimal_to_american, implied, overround, devig_proportional,
    devig_power, devig_shin, devig_all, DevigResult,
)
from tennis_edge.external_market.consensus import (  # noqa: F401
    Reference, build_reference, INDEPENDENCE_GROUPS,
)
