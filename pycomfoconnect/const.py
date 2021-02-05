from enum import IntEnum, unique

# API contants

FAN_MODE_AWAY = 'away'
FAN_MODE_LOW = 'low'
FAN_MODE_MEDIUM = 'medium'
FAN_MODE_HIGH = 'high'

# Commands
CMD_FAN_MODE_AWAY =   b'\x84\x15\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00'
CMD_FAN_MODE_LOW =    b'\x84\x15\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x01'
CMD_FAN_MODE_MEDIUM = b'\x84\x15\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x02'
CMD_FAN_MODE_HIGH =   b'\x84\x15\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x03'
CMD_FAN_MODE_BOOSTa = b'\x84\x15\x01\x06\x00\x00\x00\x00'
CMD_FAN_MODE_BOOSTb = b'\x00\x00\x03'
CMD_FAN_MODE_BOOST10 =b'\x84\x15\x01\x06\x00\x00\x00\x00\x58\x02\x00\x00\x03'
CMD_MODE_AUTO =       b'\x85\x15\x08\x01' #AUTO !!!
CMD_MODE_MANUAL =     b'\x84\x15\x08\x01\x00\x00\x00\x00\x01\x00\x00\x00\x01' #MANUAL !!!
CMD_READ_CONFIG =     b'\x87\x15\x01'
CMD_READ_HRU = 	      b'\x01\x01\x01\x10\x08'
CMD_VENTMODE_SUPPLY = b'\x84\x15\x06\x01\x00\x00\x00\x00\x10\x0e\x00\x00\x01' ## SUPPLY ONLY !!!
CMD_VENTMODE_EXTRACT =b'\x84\x15\x06\x01\x00\x00\x00\x00\x10\x0e\x00\x00\x02' ## EXTRACT ONLY !!!
CMD_VENTMODE_BALANCE =b'\x85\x15\x06\x01' #BALANCE MODE AGAIN !!!
CMD_TEMPPROF_NORMAL = b'\x84\x15\x03\x01\x00\x00\x00\x00\xff\xff\xff\xff\x00' # NORMAL TEMP PROFILE
CMD_TEMPPROF_COOL =   b'\x84\x15\x03\x01\x00\x00\x00\x00\xff\xff\xff\xff\x01' # COOL TEMP PROFILE
CMD_TEMPROF_WARM =    b'\x84\x15\x03\x01\x00\x00\x00\x00\xff\xff\xff\xff\x02' # WARM TEMP PROFILE
CMD_BYPASS_ON =       b'\x84\x15\x02\x01\x00\x00\x00\x00\x10\x0e\x00\x00\x01' # BYPASS ASTIVATED
CMD_BYPASS_OFF =      b'\x84\x15\x02\x01\x00\x00\x00\x00\x10\x0e\x00\x00\x02' # BYPASS DEACTIVATED
CMD_BYPASS_AUTO =     b'\x85\x15\x02\x01' # BYPASS AUTO
CMD_SENS_TEMP_OFF =   b'\x03\x1d\x01\x04\x00' # SENSOR VENT: TEMP PASSIVE OFF
CMD_SENS_TEMP_AUTO =  b'\x03\x1d\x01\x04\x01' # SENSOR VENT: TEMP PASSIVE AUTO ONLY
CMD_SENS_TEMP_ON =    b'\x03\x1d\x01\x04\x02' # SENSOR VENT: TEMP PASSIVE ON
CMD_SENS_HUMC_OFF =   b'\x03\x1d\x01\x06\x00' # SENSOR VENT: HUMIDITY COMFORT OFF
CMD_SENS_HUMC_AUTO =  b'\x03\x1d\x01\x06\x01' # SENSOR VENT: HUMIDITY COMFORT AUTO ONLY
CMD_SENS_HUMC_ON =    b'\x03\x1d\x01\x06\x02' # SENSOR VENT: HUMIDITY COMFORT ON
CMD_SENS_HUMP_OFF =   b'\x03\x1d\x01\x07\x00' # SENSOR VENT: HUMIDITY PROTECTION OFF
CMD_SENS_HUMP_AUTO =  b'\x03\x1d\x01\x07\x01' # SENSOR VENT: HUMIDITY PROTECTION AUTO
CMD_SENS_HUMP_ON =    b'\x03\x1d\x01\x07\x02' # SENSOR VENT: HUMIDITY PROTECTION ON

@unique
class SENSOR(IntEnum):
    # Sensor locations
    SENSOR_AWAY = 16
    SENSOR_OPERATING_MODE_BIS = 49
    SENSOR_OPERATING_MODE = 56
    SENSOR_FAN_SPEED_MODE = 65
    SENSOR_BYPASS_ACTIVATIONSTATE = 66
    SENSOR_PROFILE_TEMPERATURE = 67
    SENSOR_FAN_MODE_SUPPLY = 70
    SENSOR_FAN_MODE_EXHAUST = 71
    SENSOR_FAN_NEXT_CHANGE = 81
    SENSOR_FAN_EXHAUST_DUTY = 117
    #SENSOR_FAN_SUPPLY_DUTY = 117
    SENSOR_FAN_SUPPLY_DUTY = 118
    #SENSOR_FAN_EXHAUST_DUTY = 118
    SENSOR_FAN_EXHAUST_FLOW = 119
    #SENSOR_FAN_SUPPLY_FLOW = 119
    SENSOR_FAN_SUPPLY_FLOW = 120
    #SENSOR_FAN_EXHAUST_FLOW = 120
    SENSOR_FAN_EXHAUST_SPEED = 121
    #SENSOR_FAN_SUPPLY_SPEED = 121
    SENSOR_FAN_SUPPLY_SPEED = 122
    #SENSOR_FAN_EXHAUST_SPEED = 122
    SENSOR_POWER_CURRENT = 128
    SENSOR_POWER_TOTAL_YEAR = 129
    SENSOR_POWER_TOTAL = 130
    SENSOR_PREHEATER_POWER_TOTAL_YEAR = 144
    SENSOR_PREHEATER_POWER_TOTAL = 145
    SENSOR_PREHEATER_POWER_CURRENT = 146
    SENSOR_SETTING_RF_PAIRING = 176
    SENSOR_DAYS_TO_REPLACE_FILTER = 192
    SENSOR_CURRENT_RMOT = 209
    SENSOR_SETTING_HEATING_SEASON = 210
    SENSOR_AVOIDED_HEATING_CURRENT = 213
    SENSOR_AVOIDED_HEATING_TOTAL_YEAR = 214
    SENSOR_AVOIDED_HEATING_TOTAL = 215
    SENSOR_AVOIDED_COOLING_CURRENT = 216
    SENSOR_AVOIDED_COOLING_TOTAL_YEAR = 217
    SENSOR_AVOIDED_COOLING_TOTAL = 218
    SENSOR_TEMPERATURE_SUPPLY = 221
    SENSOR_AUTO_STATE = 225
    SENSOR_HUM_OVERDRIVE = 226
    SENSOR_BYPASS_STATE = 227
    SENSOR_FROST_PROTECTION_STATE = 228
    SENSOR_TEMPERATURE_EXTRACT = 274
    SENSOR_TEMPERATURE_EXHAUST = 275
    SENSOR_TEMPERATURE_OUTDOOR = 276
    SENSOR_HUMIDITY_EXTRACT = 290
    SENSOR_HUMIDITY_EXHAUST = 291
    SENSOR_HUMIDITY_OUTDOOR = 292
    SENSOR_HUMIDITY_SUPPLY = 294
