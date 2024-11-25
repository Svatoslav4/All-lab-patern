# bridge.py

class Appliance:
    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError


class Washer(Appliance):
    def start(self):
        print("Washer started.")

    def stop(self):
        print("Washer stopped.")


class VacuumCleaner(Appliance):
    def start(self):
        print("Vacuum cleaner started.")

    def stop(self):
        print("Vacuum cleaner stopped.")


class Switch:
    def __init__(self, appliance: Appliance):
        self.appliance = appliance

    def turn_on(self):
        self.appliance.start()

    def turn_off(self):
        self.appliance.stop()
