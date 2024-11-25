# subsystems.py

class LightingSystem:
    def turn_on_lights(self):
        print("Lights turned on.")

    def turn_off_lights(self):
        print("Lights turned off.")

    def set_brightness(self, level):
        print(f"Brightness set to {level}.")


class SecuritySystem:
    def arm_system(self):
        print("Security system armed.")

    def disarm_system(self):
        print("Security system disarmed.")

    def trigger_alarm(self):
        print("Alarm triggered!")


class ClimateControlSystem:
    def set_temperature(self, target_temp):
        print(f"Temperature set to {target_temp}°C.")

    def turn_on_heater(self):
        print("Heater turned on.")

    def turn_on_ac(self):
        print("Air conditioner turned on.")


class EntertainmentSystem:
    def play_music(self):
        print("Playing music.")

    def stop_music(self):
        print("Music stopped.")

    def set_volume(self, level):
        print(f"Volume set to {level}.")
