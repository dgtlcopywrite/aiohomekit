#
# Copyright 2019 aiohomekit team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


class CharacteristicsTypes:

    """
    All known characteristic types.

    There is no centralised repository for all of these.

    * Some have by reverse engineered by open source projects like HAP-NodeJS
    * Some are "self documenting" (the name appears in the API endpoints)
    * Some are documented in open source
    """

    ACCESSORY_IDENTIFIER = "00000057-0000-1000-8000-0026BB765291"
    ACCESSORY_PROPERTIES = "000000A6-0000-1000-8000-0026BB765291"
    ACCESS_CODE_CONTROL_POINT = "00000262-0000-1000-8000-0026BB765291"
    ACCESS_CODE_SUPPORTED_CONFIGURATION = "00000261-0000-1000-8000-0026BB765291"
    ACCESS_CONTROL_LEVEL = "000000E5-0000-1000-8000-0026BB765291"
    ACTIVE = "000000B0-0000-1000-8000-0026BB765291"
    ACTIVE_IDENTIFIER = "000000E7-0000-1000-8000-0026BB765291"
    ACTIVITY_INTERVAL = "0000023B-0000-1000-8000-0026BB765291"
    ADMINISTRATOR_ONLY_ACCESS = "00000001-0000-1000-8000-0026BB765291"
    AIRPLAY_ENABLE = "0000025B-0000-1000-8000-0026BB765291"
    AIR_PURIFIER_STATE_CURRENT = "000000A9-0000-1000-8000-0026BB765291"
    AIR_PURIFIER_STATE_TARGET = "000000A8-0000-1000-8000-0026BB765291"
    AIR_QUALITY = "00000095-0000-1000-8000-0026BB765291"
    APP_MATCHING_IDENTIFIER = "000000A4-0000-1000-8000-0026BB765291"
    ASSET_UPDATE_READINESS = "00000269-0000-1000-8000-0026BB765291"
    AUDIO_FEEDBACK = "00000005-0000-1000-8000-0026BB765291"
    BATTERY_LEVEL = "00000068-0000-1000-8000-0026BB765291"
    BRIGHTNESS = "00000008-0000-1000-8000-0026BB765291"
    BUTTON_EVENT = "00000126-0000-1000-8000-0026BB765291"
    CAMERA_OPERATING_MODE_INDICATOR = "0000021D-0000-1000-8000-0026BB765291"
    CARBON_DIOXIDE_DETECTED = "00000092-0000-1000-8000-0026BB765291"
    CARBON_DIOXIDE_LEVEL = "00000093-0000-1000-8000-0026BB765291"
    CARBON_DIOXIDE_PEAK_LEVEL = "00000094-0000-1000-8000-0026BB765291"
    CARBON_MONOXIDE_DETECTED = "00000069-0000-1000-8000-0026BB765291"
    CARBON_MONOXIDE_LEVEL = "00000090-0000-1000-8000-0026BB765291"
    CARBON_MONOXIDE_PEAK_LEVEL = "00000091-0000-1000-8000-0026BB765291"
    CATEGORY = "000000A3-0000-1000-8000-0026BB765291"
    CCA_ENERGY_DETECT_THRESHOLD = "00000246-0000-1000-8000-0026BB765291"
    CCA_SIGNAL_DETECT_THRESHOLD = "00000245-0000-1000-8000-0026BB765291"
    CHARACTERISTIC_VALUE_ACTIVE_TRANSITION_COUNT = (
        "0000024B-0000-1000-8000-0026BB765291"
    )
    CHARACTERISTIC_VALUE_TRANSITION_CONTROL = "00000143-0000-1000-8000-0026BB765291"
    CHARGING_STATE = "0000008F-0000-1000-8000-0026BB765291"
    CLOSED_CAPTIONS = "000000DD-0000-1000-8000-0026BB765291"
    COLOR_TEMPERATURE = "000000CE-0000-1000-8000-0026BB765291"
    CONFIGURATION_STATE = "00000263-0000-1000-8000-0026BB765291"
    CONFIGURED_NAME = "000000E3-0000-1000-8000-0026BB765291"
    CONFIGURE_BRIDGED_ACCESSORY = "000000A0-0000-1000-8000-0026BB765291"
    CONFIGURE_BRIDGED_ACCESSORY_STATUS = "0000009D-0000-1000-8000-0026BB765291"
    CONTACT_STATE = "0000006A-0000-1000-8000-0026BB765291"
    CURRENT_HEATER_COOLER_STATE = "000000B1-0000-1000-8000-0026BB765291"
    CURRENT_HUMIDIFIER_DEHUMIDIFIER_STATE = "000000B3-0000-1000-8000-0026BB765291"
    CURRENT_MEDIA_STATE = "000000E0-0000-1000-8000-0026BB765291"
    CURRENT_TIME = "0000009B-0000-1000-8000-0026BB765291"
    CURRENT_TRANSPORT = "0000022B-0000-1000-8000-0026BB765291"
    CURRENT_VISIBILITY_STATE = "00000135-0000-1000-8000-0026BB765291"
    DAY_OF_THE_WEEK = "00000098-0000-1000-8000-0026BB765291"
    DENSITY_NO2 = "000000C4-0000-1000-8000-0026BB765291"
    DENSITY_OZONE = "000000C3-0000-1000-8000-0026BB765291"
    DENSITY_PM10 = "000000C7-0000-1000-8000-0026BB765291"
    DENSITY_PM25 = "000000C6-0000-1000-8000-0026BB765291"
    DENSITY_SO2 = "000000C5-0000-1000-8000-0026BB765291"
    DENSITY_VOC = "000000C8-0000-1000-8000-0026BB765291"
    DIAGONAL_FIELD_OF_VIEW = "00000224-0000-1000-8000-0026BB765291"
    DISCOVERED_BRIDGED_ACCESSORIES = "0000009F-0000-1000-8000-0026BB765291"
    DISCOVER_BRIDGED_ACCESSORIES = "0000009E-0000-1000-8000-0026BB765291"
    DISPLAY_ORDER = "00000136-0000-1000-8000-0026BB765291"
    DOOR_STATE_CURRENT = "0000000E-0000-1000-8000-0026BB765291"
    DOOR_STATE_TARGET = "00000032-0000-1000-8000-0026BB765291"
    EVENT_RETRANSMISSION_MAXIMUM = "0000023D-0000-1000-8000-0026BB765291"
    EVENT_SNAPSHOTS_ACTIVE = "00000223-0000-1000-8000-0026BB765291"
    EVENT_TRANSMISSION_COUNTERS = "0000023E-0000-1000-8000-0026BB765291"
    FAN_STATE_CURRENT = "000000AF-0000-1000-8000-0026BB765291"
    FAN_STATE_TARGET = "000000BF-0000-1000-8000-0026BB765291"
    FILTER_CHANGE_INDICATION = "000000AC-0000-1000-8000-0026BB765291"
    FILTER_LIFE_LEVEL = "000000AB-0000-1000-8000-0026BB765291"
    FILTER_RESET_INDICATION = "000000AD-0000-1000-8000-0026BB765291"
    FIRMWARE_REVISION = "00000052-0000-1000-8000-0026BB765291"
    HARDWARE_FINISH = "0000026C-0000-1000-8000-0026BB765291"
    HARDWARE_REVISION = "00000053-0000-1000-8000-0026BB765291"
    HEART_BEAT = "0000024A-0000-1000-8000-0026BB765291"
    HEATING_COOLING_CURRENT = "0000000F-0000-1000-8000-0026BB765291"
    HEATING_COOLING_TARGET = "00000033-0000-1000-8000-0026BB765291"
    HOMEKIT_CAMERA_ACTIVE = "0000021B-0000-1000-8000-0026BB765291"
    HORIZONTAL_TILT_CURRENT = "0000006C-0000-1000-8000-0026BB765291"
    HORIZONTAL_TILT_TARGET = "0000007B-0000-1000-8000-0026BB765291"
    HUE = "00000013-0000-1000-8000-0026BB765291"
    IDENTIFIER = "000000E6-0000-1000-8000-0026BB765291"
    IDENTIFY = "00000014-0000-1000-8000-0026BB765291"
    IMAGE_MIRROR = "0000011F-0000-1000-8000-0026BB765291"
    IMAGE_ROTATION = "0000011E-0000-1000-8000-0026BB765291"
    INPUT_DEVICE_TYPE = "000000DC-0000-1000-8000-0026BB765291"
    INPUT_EVENT = "00000073-0000-1000-8000-0026BB765291"
    INPUT_SOURCE_TYPE = "000000DB-0000-1000-8000-0026BB765291"
    IN_USE = "000000D2-0000-1000-8000-0026BB765291"
    IS_CONFIGURED = "000000D6-0000-1000-8000-0026BB765291"
    LEAK_DETECTED = "00000070-0000-1000-8000-0026BB765291"
    LIGHT_LEVEL_CURRENT = "0000006B-0000-1000-8000-0026BB765291"
    LINK_QUALITY = "0000009C-0000-1000-8000-0026BB765291"
    LOCK_MANAGEMENT_AUTO_SECURE_TIMEOUT = "0000001A-0000-1000-8000-0026BB765291"
    LOCK_MANAGEMENT_CONTROL_POINT = "00000019-0000-1000-8000-0026BB765291"
    LOCK_MECHANISM_CURRENT_STATE = "0000001D-0000-1000-8000-0026BB765291"
    LOCK_MECHANISM_LAST_KNOWN_ACTION = "0000001C-0000-1000-8000-0026BB765291"
    LOCK_MECHANISM_TARGET_STATE = "0000001E-0000-1000-8000-0026BB765291"
    LOCK_PHYSICAL_CONTROLS = "000000A7-0000-1000-8000-0026BB765291"
    LOGS = "0000001F-0000-1000-8000-0026BB765291"
    MAC_RETRANSMISSION_MAXIMUM = "00000247-0000-1000-8000-0026BB765291"
    MAC_TRANSMISSION_COUNTERS = "00000248-0000-1000-8000-0026BB765291"
    MANAGED_NETWORK_ENABLE = "00000215-0000-1000-8000-0026BB765291"
    MANUALLY_DISABLED = "00000227-0000-1000-8000-0026BB765291"
    MANUFACTURER = "00000020-0000-1000-8000-0026BB765291"
    MAXIMUM_TRANSMIT_POWER = "00000243-0000-1000-8000-0026BB765291"
    MODEL = "00000021-0000-1000-8000-0026BB765291"
    MOTION_DETECTED = "00000022-0000-1000-8000-0026BB765291"
    MULTIFUNCTION_BUTTON = "0000026B-0000-1000-8000-0026BB765291"
    MUTE = "0000011A-0000-1000-8000-0026BB765291"
    NAME = "00000023-0000-1000-8000-0026BB765291"
    NETWORK_ACCESS_VIOLATION_CONTROL = "0000021F-0000-1000-8000-0026BB765291"
    NETWORK_CLIENT_PROFILE_CONTROL = "0000020C-0000-1000-8000-0026BB765291"
    NETWORK_CLIENT_STATUS_CONTROL = "0000020D-0000-1000-8000-0026BB765291"
    NFC_ACCESS_CONTROL_POINT = "00000264-0000-1000-8000-0026BB765291"
    NFC_ACCESS_SUPPORTED_CONFIGURATION = "00000265-0000-1000-8000-0026BB765291"
    NIGHT_VISION = "0000011B-0000-1000-8000-0026BB765291"
    OBSTRUCTION_DETECTED = "00000024-0000-1000-8000-0026BB765291"
    OCCUPANCY_DETECTED = "00000071-0000-1000-8000-0026BB765291"
    ON = "00000025-0000-1000-8000-0026BB765291"
    OPERATING_STATE_RESPONSE = "00000232-0000-1000-8000-0026BB765291"
    OUTLET_IN_USE = "00000026-0000-1000-8000-0026BB765291"
    PAIRING_FEATURES = "0000004F-0000-1000-8000-0026BB765291"
    PAIRING_PAIRINGS = "00000050-0000-1000-8000-0026BB765291"
    PAIR_SETUP = "0000004C-0000-1000-8000-0026BB765291"
    PAIR_VERIFY = "0000004E-0000-1000-8000-0026BB765291"
    PASSWORD_SETTING = "000000E4-0000-1000-8000-0026BB765291"
    PERIODIC_SNAPSHOTS_ACTIVE = "00000225-0000-1000-8000-0026BB765291"
    PICTURE_MODE = "000000E2-0000-1000-8000-0026BB765291"
    PING = "0000023C-0000-1000-8000-0026BB765291"
    POSITION_CURRENT = "0000006D-0000-1000-8000-0026BB765291"
    POSITION_HOLD = "0000006F-0000-1000-8000-0026BB765291"
    POSITION_STATE = "00000072-0000-1000-8000-0026BB765291"
    POSITION_TARGET = "0000007C-0000-1000-8000-0026BB765291"
    POWER_MODE_SELECTION = "000000DF-0000-1000-8000-0026BB765291"
    PRODUCT_DATA = "00000220-0000-1000-8000-0026BB765291"
    PROGRAMMABLE_SWITCH_OUTPUT_STATE = "00000074-0000-1000-8000-0026BB765291"
    PROGRAM_MODE = "000000D1-0000-1000-8000-0026BB765291"
    REACHABLE = "00000063-0000-1000-8000-0026BB765291"
    RECEIVED_SIGNAL_STRENGTH_INDICATION = "0000023F-0000-1000-8000-0026BB765291"
    RECEIVER_SENSITIVITY = "00000244-0000-1000-8000-0026BB765291"
    RECORDING_AUDIO_ACTIVE = "00000226-0000-1000-8000-0026BB765291"
    RELATIVE_HUMIDITY_CURRENT = "00000010-0000-1000-8000-0026BB765291"
    RELATIVE_HUMIDITY_DEHUMIDIFIER_THRESHOLD = "000000C9-0000-1000-8000-0026BB765291"
    RELATIVE_HUMIDITY_HUMIDIFIER_THRESHOLD = "000000CA-0000-1000-8000-0026BB765291"
    RELATIVE_HUMIDITY_TARGET = "00000034-0000-1000-8000-0026BB765291"
    RELAY_CONTROL_POINT = "0000005E-0000-1000-8000-0026BB765291"
    RELAY_ENABLED = "0000005B-0000-1000-8000-0026BB765291"
    RELAY_STATE = "0000005C-0000-1000-8000-0026BB765291"
    REMAINING_DURATION = "000000D4-0000-1000-8000-0026BB765291"
    REMOTE_KEY = "000000E1-0000-1000-8000-0026BB765291"
    ROTATION_DIRECTION = "00000028-0000-1000-8000-0026BB765291"
    ROTATION_SPEED = "00000029-0000-1000-8000-0026BB765291"
    ROUTER_STATUS = "0000020E-0000-1000-8000-0026BB765291"
    SATURATION = "0000002F-0000-1000-8000-0026BB765291"
    SECURITY_SYSTEM_ALARM_TYPE = "0000008E-0000-1000-8000-0026BB765291"
    SECURITY_SYSTEM_STATE_CURRENT = "00000066-0000-1000-8000-0026BB765291"
    SECURITY_SYSTEM_STATE_TARGET = "00000067-0000-1000-8000-0026BB765291"
    SELECTED_AUDIO_STREAM_CONFIGURATION = "00000128-0000-1000-8000-0026BB765291"
    SELECTED_CAMERA_RECORDING_CONFIGURATION = "00000209-0000-1000-8000-0026BB765291"
    SELECTED_DIAGNOSTICS_MODES = "0000024D-0000-1000-8000-0026BB765291"
    SELECTED_RTP_STREAM_CONFIGURATION = "00000117-0000-1000-8000-0026BB765291"
    SERIAL_NUMBER = "00000030-0000-1000-8000-0026BB765291"
    SERVICE_LABEL_INDEX = "000000CB-0000-1000-8000-0026BB765291"
    SERVICE_LABEL_NAMESPACE = "000000CD-0000-1000-8000-0026BB765291"
    SETUP_DATA_STREAM_TRANSPORT = "00000131-0000-1000-8000-0026BB765291"
    SETUP_ENDPOINTS = "00000118-0000-1000-8000-0026BB765291"
    SETUP_TRANSFER_TRANSPORT = "00000201-0000-1000-8000-0026BB765291"
    SET_DURATION = "000000D3-0000-1000-8000-0026BB765291"
    SIGNAL_TO_NOISE_RATIO = "00000241-0000-1000-8000-0026BB765291"
    SIRI_ENABLE = "00000255-0000-1000-8000-0026BB765291"
    SIRI_ENDPOINT_SESSION_STATUS = "00000254-0000-1000-8000-0026BB765291"
    SIRI_ENGINE_VERSION = "0000025A-0000-1000-8000-0026BB765291"
    SIRI_INPUT_TYPE = "00000132-0000-1000-8000-0026BB765291"
    SIRI_LIGHT_ON_USE = "00000258-0000-1000-8000-0026BB765291"
    SIRI_LISTENING = "00000256-0000-1000-8000-0026BB765291"
    SIRI_TOUCH_TO_USE = "00000257-0000-1000-8000-0026BB765291"
    SLAT_STATE_CURRENT = "000000AA-0000-1000-8000-0026BB765291"
    SLEEP_DISCOVERY_MODE = "000000E8-0000-1000-8000-0026BB765291"
    SLEEP_INTERVAL = "0000023A-0000-1000-8000-0026BB765291"
    SMOKE_DETECTED = "00000076-0000-1000-8000-0026BB765291"
    SOFTWARE_REVISION = "00000054-0000-1000-8000-0026BB765291"
    STATUS_ACTIVE = "00000075-0000-1000-8000-0026BB765291"
    STATUS_FAULT = "00000077-0000-1000-8000-0026BB765291"
    STATUS_LO_BATT = "00000079-0000-1000-8000-0026BB765291"
    STATUS_TAMPERED = "0000007A-0000-1000-8000-0026BB765291"
    STREAMING_STATUS = "00000120-0000-1000-8000-0026BB765291"
    SUPPORTED_ASSET_TYPES = "00000268-0000-1000-8000-0026BB765291"
    SUPPORTED_AUDIO_CONFIGURATION = "00000115-0000-1000-8000-0026BB765291"
    SUPPORTED_AUDIO_RECORDING_CONFIGURATION = "00000207-0000-1000-8000-0026BB765291"
    SUPPORTED_CAMERA_RECORDING_CONFIGURATION = "00000205-0000-1000-8000-0026BB765291"
    SUPPORTED_CHARACTERISTIC_VALUE_TRANSITION_CONFIGURATION = (
        "00000144-0000-1000-8000-0026BB765291"
    )
    SUPPORTED_DATA_STREAM_TRANSPORT_DATA_CONFIGURATION = (
        "00000130-0000-1000-8000-0026BB765291"
    )
    SUPPORTED_DIAGNOSTICS_MODES = "0000024C-0000-1000-8000-0026BB765291"
    SUPPORTED_DIAGNOSTICS_SNAPSHOT = "00000238-0000-1000-8000-0026BB765291"
    SUPPORTED_ROUTER_CONFIGURATION = "00000210-0000-1000-8000-0026BB765291"
    SUPPORTED_RTP_CONFIGURATION = "00000116-0000-1000-8000-0026BB765291"
    SUPPORTED_TRANSFER_TRANSPORT_CONFIGURATION = "00000202-0000-1000-8000-0026BB765291"
    SUPPORTED_VIDEO_RECORDING_CONFIGURATION = "00000206-0000-1000-8000-0026BB765291"
    SUPPORTED_VIDEO_STREAM_CONFIGURATION = "00000114-0000-1000-8000-0026BB765291"
    SWING_MODE = "000000B6-0000-1000-8000-0026BB765291"
    TARGET_CONTROL_LIST = "00000124-0000-1000-8000-0026BB765291"
    TARGET_CONTROL_SUPPORTED_CONFIGURATION = "00000123-0000-1000-8000-0026BB765291"
    TARGET_HEATER_COOLER_STATE = "000000B2-0000-1000-8000-0026BB765291"
    TARGET_HUMIDIFIER_DEHUMIDIFIER_STATE = "000000B4-0000-1000-8000-0026BB765291"
    TARGET_MEDIA_STATE = "00000137-0000-1000-8000-0026BB765291"
    TARGET_VISIBILITY_STATE = "00000134-0000-1000-8000-0026BB765291"
    TEMPERATURE_COOLING_THRESHOLD = "0000000D-0000-1000-8000-0026BB765291"
    TEMPERATURE_CURRENT = "00000011-0000-1000-8000-0026BB765291"
    TEMPERATURE_HEATING_THRESHOLD = "00000012-0000-1000-8000-0026BB765291"
    TEMPERATURE_TARGET = "00000035-0000-1000-8000-0026BB765291"
    TEMPERATURE_UNITS = "00000036-0000-1000-8000-0026BB765291"
    THIRD_PARTY_CAMERA_ACTIVE = "0000021C-0000-1000-8000-0026BB765291"
    THREAD_CONTROL_POINT = "00000704-0000-1000-8000-0026BB765291"
    THREAD_NODE_CAPABILITIES = "00000702-0000-1000-8000-0026BB765291"
    THREAD_OPENTHREAD_VERSION = "00000706-0000-1000-8000-0026BB765291"
    THREAD_STATUS = "00000703-0000-1000-8000-0026BB765291"
    TILT_CURRENT = "000000C1-0000-1000-8000-0026BB765291"
    TILT_TARGET = "000000C2-0000-1000-8000-0026BB765291"
    TIME_UPDATE = "0000009A-0000-1000-8000-0026BB765291"
    TRANSMIT_POWER = "00000242-0000-1000-8000-0026BB765291"
    TUNNELED_ACCESSORY_ADVERTISING = "00000060-0000-1000-8000-0026BB765291"
    TUNNELED_ACCESSORY_CONNECTED = "00000059-0000-1000-8000-0026BB765291"
    TUNNELED_ACCESSORY_STATE_NUMBER = "00000058-0000-1000-8000-0026BB765291"
    TUNNEL_CONNECTION_TIMEOUT = "00000061-0000-1000-8000-0026BB765291"
    TYPE_SLAT = "000000C0-0000-1000-8000-0026BB765291"
    VALVE_TYPE = "000000D5-0000-1000-8000-0026BB765291"
    VERSION = "00000037-0000-1000-8000-0026BB765291"
    VERTICAL_TILT_CURRENT = "0000006E-0000-1000-8000-0026BB765291"
    VERTICAL_TILT_TARGET = "0000007D-0000-1000-8000-0026BB765291"
    VOLUME = "00000119-0000-1000-8000-0026BB765291"
    VOLUME_CONTROL_TYPE = "000000E9-0000-1000-8000-0026BB765291"
    VOLUME_SELECTOR = "000000EA-0000-1000-8000-0026BB765291"
    WAKE_CONFIGURATION = "00000222-0000-1000-8000-0026BB765291"
    WAN_CONFIGURATION_LIST = "00000211-0000-1000-8000-0026BB765291"
    WAN_STATUS_LIST = "00000212-0000-1000-8000-0026BB765291"
    WATER_LEVEL = "000000B5-0000-1000-8000-0026BB765291"
    WI_FI_CAPABILITIES = "0000022C-0000-1000-8000-0026BB765291"
    WI_FI_CONFIGURATION_CONTROL = "0000022D-0000-1000-8000-0026BB765291"
    WI_FI_SATELLITE_STATUS = "0000021E-0000-1000-8000-0026BB765291"
    ZOOM_DIGITAL = "0000011D-0000-1000-8000-0026BB765291"
    ZOOM_OPTICAL = "0000011C-0000-1000-8000-0026BB765291"

    # Vendor specific extensions

    # Elgato Eve
    VENDOR_EVE_ENERGY_VOLTAGE = "E863F10A-079E-48FF-8F27-9C2605A29F52"
    VENDOR_EVE_ENERGY_AMPERE = "E863F126-079E-48FF-8F27-9C2605A29F52"
    VENDOR_EVE_ENERGY_WATT = "E863F10D-079E-48FF-8F27-9C2605A29F52"
    VENDOR_EVE_ENERGY_KW_HOUR = "E863F10C-079E-48FF-8F27-9C2605A29F52"

    # 0 = high, 4 = medium, 7 = low.
    VENDOR_EVE_MOTION_SENSITIVITY = "E863F120-079E-48FF-8F27-9C2605A29F52"
    # Persistence of motion indication in seconds
    VENDOR_EVE_MOTION_DURATION = "E863F12D-079E-48FF-8F27-9C2605A29F52"

    VENDOR_EVE_ROOM_AIR_QUALITY_PPM = "E863F10B-079E-48FF-8F27-9C2605A29F52"

    VENDOR_EVE_DEGREE_AIR_PRESSURE = "E863F10F-079E-48FF-8F27-9C2605A29F52"
    VENDOR_EVE_DEGREE_ELEVATION = "E863F130-079E-48FF-8F27-9C2605A29F52"

    # HAA - Home Accessory Architect
    # https://github.com/RavenSystem/esp-homekit-devices
    VENDOR_HAA_SETUP = "F0000102-0218-2017-81BF-AF2B7C833922"
    VENDOR_HAA_UPDATE = "F0000101-0218-2017-81BF-AF2B7C833922"
    
    # iDevices
    VENDOR_IDEVICES_ENERGY_MONITORING = "6747C101-FAC9-4D62-ADF4-E764D0A8B39D"
    # milliWatts
    VENDOR_IDEVICES_REALTIME_ENERGY = "6747C102-FAC9-4D62-ADF4-E764D0A8B39D"
    # milliWattHours/10 (/365 to get total use)
    VENDOR_IDEVICES_AVERAGE_YEARLY_ENERGY = "6747C103-FAC9-4D62-ADF4-E764D0A8B39D"
    VENDOR_IDEVICES_TOTAL_SECONDS_ON = "6747C104-FAC9-4D62-ADF4-E764D0A8B39D"
    VENDOR_IDEVICES_TOTAL_SECONDS_SINCE_RESET = "6747C105-FAC9-4D62-ADF4-E764D0A8B39D"
    # r/w, bool
    VENDOR_IDEVICES_RESET_ENERGY_COUNTERS = "6747C106-FAC9-4D62-ADF4-E764D0A8B39D"

    # Koogeek
    # Watts
    VENDOR_KOOGEEK_REALTIME_ENERGY = "4AAAF931-0DEC-11E5-B939-0800200C9A66"
    VENDOR_KOOGEEK_REALTIME_ENERGY_2 = "7BBBA96E-EB2D-11E5-A837-0800200C9A66"

    # VOCOLinc
    VENDOR_VOCOLINC_HUMIDIFIER_SPRAY_LEVEL = "69D52519-0A4E-4898-8335-4739F9116D0A"
    VENDOR_VOCOLINC_HUMIDIFIER_TIMER_SETTING = "F84B3138-E44F-49B9-AA91-9E1736C247C0"
    VENDOR_VOCOLINC_HUMIDIFIER_COUNTDOWN = "43CE176B-2933-4034-98A7-AD215BEEBF2F"

    VENDOR_VOCOLINC_LIGHTBULB_LIGHT_TIMER_SETTING = (
        "A30DFE91-271A-42A5-88BA-00E3FF5488AD"
    )
    VENDOR_VOCOLINC_LIGHTBULB_LIGHT_EFFECT_MODE = "146889FC-7C42-429B-93AB-E80F79759E90"
    VENDOR_VOCOLINC_LIGHTBULB_LIGHT_EFFECT_FLAG = "9D4B479D-9EFB-4739-98F3-B33E6543BF7B"
    VENDOR_VOCOLINC_LIGHTBULB_FLASHING_MODE = "2C42B339-6EC9-4ED5-8DBF-FFCCC721B144"
    VENDOR_VOCOLINC_LIGHTBULB_SMOOTHING_MODE = "A3663C89-DC18-42EF-8297-910A4C0C9B61"
    VENDOR_VOCOLINC_LIGHTBULB_BREATHING_MODE = "6533B15C-AECB-455F-8896-20B125390F61"

    VENDOR_VOCOLINC_OUTLET_ENERGY = "FC093458-18F0-4B1D-8360-BB68A3FCC9C5"

    # Ecobee
    # r/o, uint8 - current mode - home(0)/sleep(1)/away(2)/temp(3)
    VENDOR_ECOBEE_CURRENT_MODE = "B7DDB9A3-54BB-4572-91D2-F1F5B0510F8C"
    # r/w, float - home heat temperature between 7.2 and 26.1
    VENDOR_ECOBEE_HOME_TARGET_HEAT = "E4489BBC-5227-4569-93E5-B345E3E5508F"
    # r/w, float - home cool temperature between 18.3 and 33.3
    VENDOR_ECOBEE_HOME_TARGET_COOL = "7D381BAA-20F9-40E5-9BE9-AEB92D4BECEF"
    # r/w, float - sleep heat temperature between 7.2 and 26.1
    VENDOR_ECOBEE_SLEEP_TARGET_HEAT = "73AAB542-892A-4439-879A-D2A883724B69"
    # r/w, float - sleep cool temperature between 18.3 and 33.3
    VENDOR_ECOBEE_SLEEP_TARGET_COOL = "5DA985F0-898A-4850-B987-B76C6C78D670"
    # r/w, float - away heat temp between 7.2 and 26.1
    VENDOR_ECOBEE_AWAY_TARGET_HEAT = "05B97374-6DC0-439B-A0FA-CA33F612D425"
    # r/w, float - away cool temp between 18.3 and 33.3
    VENDOR_ECOBEE_AWAY_TARGET_COOL = "A251F6E7-AC46-4190-9C5D-3D06277BDF9F"
    # w/o, uint8 - set hold schedule mode - home(0)/sleep(1)/away(2)
    VENDOR_ECOBEE_SET_HOLD_SCHEDULE = "1B300BC2-CFFC-47FF-89F9-BD6CCF5F2853"
    # r/w, string - 2014-01-03T00:00:00-07:00T
    VENDOR_ECOBEE_TIMESTAMP = "1621F556-1367-443C-AF19-82AF018E99DE"
    # w/o, bool - true to clear hold mode, false does nothing
    VENDOR_ECOBEE_CLEAR_HOLD = "FA128DE6-9D7D-49A4-B6D8-4E4E234DEE38"
    # r/w, 100 for on, 0 for off/auto
    # https://support.ecobee.com/s/articles/Multi-Speed-Fan-installations
    VENDOR_ECOBEE_FAN_WRITE_SPEED = "C35DA3C0-E004-40E3-B153-46655CDD9214"
    # r/o, Mirrors status of above
    VENDOR_ECOBEE_FAN_READ_SPEED = "48F62AEC-4171-4B4A-8F0E-1EEB6708B3FB"

    # ConnectSense
    # r/o, float - amps between 0 and 20
    VENDOR_CONNECTSENSE_ENERGY_AMPS = "00000004-0000-1000-8000-001D4B474349"
    # r/o, uint32 - state timer - in epoch format
    VENDOR_CONNECTSENSE_STATE_TIMER = "00000005-0000-1000-8000-001D4B474349"
    # r/o, unit32 - total amps
    VENDOR_CONNECTSENSE_TOTAL_AMPS = "00000006-0000-1000-8000-001D4B474349"
    # r/o, float - volts between 0 and 130
    VENDOR_CONNECTSENSE_ENERGY_VOLTAGE = "00000008-0000-1000-8000-001D4B474349"
    # r/o, float - amps between 0 and 20 on 20a in-wall outlet
    VENDOR_CONNECTSENSE_ENERGY_AMPS_20 = "00000009-0000-1000-8000-001D4B474349"
    # r/o, float - watts
    VENDOR_CONNECTSENSE_ENERGY_WATT = "0000000A-0000-1000-8000-001D4B474349"
    # r/o, int - power factor between 0 and 100
    VENDOR_CONNECTSENSE_ENERGY_POWER_FACTOR = "0000000B-0000-1000-8000-001D4B474349"
    # r/o, float - kilowatt hours between 0 and 7743802671740404396
    VENDOR_CONNECTSENSE_ENERGY_KW_HOUR = "0000000C-0000-1000-8000-001D4B474349"
    # r/o, string - outlet assigned name
    VENDOR_CONNECTSENSE_ASSIGNED_NAME = "0000000E-0000-1000-8000-001D4B474349"
    # r/o, uint32 - device type attached to outlet
    VENDOR_CONNECTSENSE_DEVICE_TYPE = "0000000F-0000-1000-8000-001D4B474349"

    # r/w, uint32, percentage
    VENDOR_AQARA_GATEWAY_VOLUME = "EE56B186-B0D3-528E-8C79-C21FC9BCF437"
    # r/w, bool
    VENDOR_AQARA_PAIRING_MODE = "B1C09E4C-E202-4827-B343-B0F32F727CFF"

    # r/w, uint32, percentage
    VENDOR_AQARA_E1_GATEWAY_VOLUME = "EE56B186-B0D3-488E-8C79-C21FC9BCF437"
    # r/w, bool
    VENDOR_AQARA_E1_PAIRING_MODE = "B1C09E4C-E202-4827-B863-B0F32F727CFF"
