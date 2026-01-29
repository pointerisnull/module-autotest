# TCP and Crimson download ports
DEFAULT_PORT = 23
DEFAULT_DOWNLOAD_PORT = 789

# Crimson user auth
CRIMSON_USER = "admin"
CRIMSON_PASS = "password"

BACKOFF_BASE = 2

# File paths
PINOUT_SETTINGS_PATH = "./settings/pinout.csv"
CONFIG_PATH = "./settings/device_config.csv"

# Thermocouple Types
TC_TYPE_B = 'b'
TC_TYPE_E = 'e'
TC_TYPE_J = 'j'
TC_TYPE_K = 'k'
TC_TYPE_N = 'n'
TC_TYPE_R = 'r'
TC_TYPE_S = 's'
TC_TYPE_T = 't'

# GUI Defaults
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600

# Modules
MODULES = ['8DI/8DO', '8DI/8RO', '2UIN MIX', '4UIN MIX', '6UIN', 'DA Strain Gage']

# Default Thresholds
HIGH_VOLTAGE_MAX = 3.3
HIGH_VOLTAGE_MIN = 1.5
HIGH_VOLTAGE_EXP = 2.5

LOW_VOLTAGE_MAX = 1.4
LOW_VOLTAGE_MIN = 0
LOW_VOLTAGE_EXP = 0.5

VOLTAGE_TOLERANCE = 2 # Percent