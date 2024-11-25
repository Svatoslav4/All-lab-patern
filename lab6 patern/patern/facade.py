# facade.py

from subsystems import LightingSystem, SecuritySystem, ClimateControlSystem, EntertainmentSystem
from settings_manager import EnergyManager

class SmartHomeFacade:
    def __init__(self):
        self.lighting = LightingSystem()
        self.security = SecuritySystem()
        self.climate = ClimateControlSystem()
        self.entertainment = EntertainmentSystem()
        self.energy_manager = EnergyManager()

    def activate_security_system(self):
        self.security.arm_system()

    def set_climate_control(self, temp):
        self.climate.set_temperature(temp)

    def control_lighting(self, action, brightness=None):
        if action == "on":
            self.lighting.turn_on_lights()
        elif action == "off":
            self.lighting.turn_off_lights()

        if brightness is not None:
            self.lighting.set_brightness(brightness)
