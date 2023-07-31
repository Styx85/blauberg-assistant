from collections.abc import Mapping
from .blauberg_device import BlaubergDevice
from .smart_wifi import smart_wifi
from .smart_home import smart_home

devices: Mapping[int, BlaubergDevice] = {
  0x300: smart_home,
  0x400: smart_home,
  0x500: smart_home,
  0x600: smart_wifi
}
