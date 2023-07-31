from collections.abc import Mapping
from .blauberg_device import BlaubergDevice
from .smart_wifi import smart_wifi
from .ecoventv2 import eco_vent

devices: Mapping[int, BlaubergDevice] = {
  0x300: eco_vent,
  0x400: eco_vent,
  0x500: eco_vent,
  0x600: smart_wifi}
