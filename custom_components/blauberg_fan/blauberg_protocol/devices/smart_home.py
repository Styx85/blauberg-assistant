from __future__ import annotations
from enum import Enum
from .blauberg_device import (
    BlaubergDevice,
    Purpose,
    SinglePointAction,
    ComplexAction,
    Component,
    OptionalAction,
    variable_to_bytes,
)
from collections.abc import Mapping
from ..packet import Packet, Section

import logging

LOG = logging.getLogger(__name__)


smart_home = BlaubergDevice(
    name=["Blauberg VENTO Expert A50-1 W V.2", "Blauberg VENTO Expert A85-1 W V.2", "Blauberg VENTO Expert A100-1 W V.2", "Blauberg VENTO Expert Duo A30-1 W V.2", "Blauberg VENTO Expert A30 W V.2"],
    parameter_map={
        Purpose.POWER: SinglePointAction(0x01),
        # TODO add other existing purposes as well
    },
    optional_entity_map=[],
    attribute_map={},
)
