from facade import SmartHomeFacade
from settings_manager import SettingsManager, EnergyManager
from bridge import Washer, VacuumCleaner, Switch

if __name__ == "__main__":
    # Тестування Facade
    home = SmartHomeFacade()
    settings = SettingsManager()

    settings.set_setting("preferred_temperature", 22)
    home.set_climate_control(settings.get_setting("preferred_temperature"))

    home.control_lighting("on", brightness=75)
    home.activate_security_system()
    EnergyManager().monitor_usage()

    # Тестування Bridge
    washer = Washer()
    vacuum = VacuumCleaner()

    washer_switch = Switch(washer)
    vacuum_switch = Switch(vacuum)

    washer_switch.turn_on()
    vacuum_switch.turn_off()
