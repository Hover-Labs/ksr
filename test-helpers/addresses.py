import smartpy as sp

# This file contains addresses for tests which are named and ensure uniqueness across the test suite.

# The address which acts as the Token Admin
ADMIN_ADDRESS = sp.address("tz1abmz7jiCV2GH2u81LRrGgAFFgvQgiDiaf")

# The governor
GOVERNOR_ADDRESS = sp.address("tz1NoYvKjXTzTk54VpLxBfouJ33J8jwKPPvw")

# An address which is rotated to.
ROTATED_ADDRESS = sp.address("tz1eibLoCDot2w2QWyR7kMoVDTto9fYs2mnJ")

# Contract address
DEXTER_ADDRESS = sp.address("tz1aRoaRhSpRYvFdyvgWLL6TGyRoGF51wDjM")
OVEN_REGISTRY_ADDRESS = sp.address("tz1VQnqCCqX4K5sP3FNkVSNKTdCAMJDd3E1n")
TOKEN_ADDRESS = sp.address("tz1aJS7Pk9uWR3wWyFf1i3RwhYxN84G7stom")

# An address which acts as a Fund Administrator.
FUND_ADMINISTRATOR_ADDRESS = sp.address("tz1VmiY38m3y95HqQLjMwqnMS7sdMfGomzKi")

# The address which owns an Oven
OVEN_OWNER_ADDRESS = sp.address("tz1S8MNvuFEUsWgjHvi3AxibRBf388NhT1q2")

# The address which acts as the OvenProxy.
OVEN_PROXY_ADDRESS = sp.address("tz1c461F8GirBvq5DpFftPoPyCcPR7HQM6gm")

# The address which acts as the OvenFactory
OVEN_FACTORY_ADDRESS = sp.address("tz1irJKkXS2DBWkU1NnmFQx1c1L7pbGg4yhk")

# The address which acts as an Oven
OVEN_ADDRESS = sp.address("tz1LmaFsWRkjr7QMCx5PtV6xTUz3AmEpKQiF")

# An series of named addresses with no particular role.
# These are used for token transfer tests.
ALICE_ADDRESS = sp.address("tz1LLNkQK4UQV6QcFShiXJ2vT2ELw449MzAA")
BOB_ADDRESS = sp.address("tz1UMCB2AHSTwG7YcGNr31CqYCtGN873royv")
CHARLIE_ADDRESS = sp.address("tz1R6Ej25VSerE3MkSoEEeBjKHCDTFbpKuSX")

# An address which is never used. This is a `null` value for addresses.
NULL_ADDRESS = sp.address("tz1bTpviNnyx2PXsNmGpCQTMQsGoYordkUoA")
