"""Constants for integration_blueprint."""
from logging import Logger, getLogger
from pyfamilysafety.account import OverrideTarget

LOGGER: Logger = getLogger(__package__)

NAME = "Microsoft Family Safety"
DOMAIN = "family_safety"
VERSION = "1.1.0b2"

DEFAULT_OVERRIDE_ENTITIES = [OverrideTarget.MOBILE,
                             OverrideTarget.WINDOWS,
                             OverrideTarget.XBOX,
                             OverrideTarget.ALL_DEVICES]
