# settings_manager.py

class SettingsManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SettingsManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.settings = {}
        return cls._instance

    def set_setting(self, key, value):
        self.settings[key] = value

    def get_setting(self, key):
        return self.settings.get(key, None)


class EnergyManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(EnergyManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def monitor_usage(self):
        print("Monitoring energy usage...")

    def optimize_energy(self):
        print("Optimizing energy usage...")
