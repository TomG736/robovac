from homeassistant.components.vacuum import VacuumEntityFeature
from .base import RoboVacEntityFeature, RobovacCommand


class T2267:
    homeassistant_features = (
        VacuumEntityFeature.BATTERY
        | VacuumEntityFeature.CLEAN_SPOT
        | VacuumEntityFeature.FAN_SPEED
        | VacuumEntityFeature.LOCATE
        | VacuumEntityFeature.PAUSE
        | VacuumEntityFeature.RETURN_HOME
        | VacuumEntityFeature.SEND_COMMAND
        | VacuumEntityFeature.START
        | VacuumEntityFeature.STATE
        | VacuumEntityFeature.STOP
        | VacuumEntityFeature.MAP
    )
    robovac_features = (
        RoboVacEntityFeature.CLEANING_TIME
        | RoboVacEntityFeature.CLEANING_AREA
        | RoboVacEntityFeature.DO_NOT_DISTURB
        | RoboVacEntityFeature.AUTO_RETURN
        | RoboVacEntityFeature.ROOM
        | RoboVacEntityFeature.ZONE
        | RoboVacEntityFeature.BOOST_IQ
        | RoboVacEntityFeature.MAP
        | RoboVacEntityFeature.CONSUMABLES
    )
    commands = {
        # protocol: 150
        # power switch: 151
        # RobovacCommand.MODE: {
        #     "code": 152,
        #     "values": [], # unknown
        # },
        RobovacCommand.STATUS: {
            # there is far more to this field!
            "code": 153,
            "values": {
                b"\x10\x052\x00": "Cleaning",
                b"\x10\x052\x02\x08\x01": "Paused",
                b"\x10\x07B\x00": "Recharge",
                b"\x10\x03\x1a\x00": "Charging",
                b"\x10\x03\x1a\x02\x08\x01": "completed",
                b"\x10\x04*\x00": "QuickMapping",
                b"\x10\x05R\x00": "standby",  # Locating?
            },
        },
        # cleaning params: 154
        RobovacCommand.DIRECTION: {
            "code": 155,
            "values": ["Forward", "Back", "Left", "Right"],
        },
        RobovacCommand.START_PAUSE: 156,
        RobovacCommand.DO_NOT_DISTURB: 157,
        RobovacCommand.FAN_SPEED: {
            "code": 158,
            "values": ["Quiet", "Standard", "Turbo", "Max"],
        },
        RobovacCommand.BOOST_IQ: 159,
        RobovacCommand.LOCATE: 160,
        # volume: 161
        # language: 162
        RobovacCommand.BATTERY: 163,
        # timing: 164
        # reserved2: 165
        # log_debug: 166
        # clean_statistics: 167
        RobovacCommand.CONSUMABLES: 168,
        # app_dev_info: 169
        # map_edit: 170
        # multi_maps_ctrl: 171
        # multi_maps_mng: 172
        # station: 173
        # media_manager: 174
        # reserved3: 175
        # unisetting: 176
        RobovacCommand.ERROR: 177,
        # toast: 178
        # analysis: 179

        # RobovacCommand.RETURN_HOME: 101,
        # These commands need codes adding
        # RobovacCommand.CLEANING_AREA: 0,
        # RobovacCommand.CLEANING_TIME: 0,
        # RobovacCommand.AUTO_RETURN: 0,
    }
