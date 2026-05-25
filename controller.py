from machine import Machine


class Controller:
    def __init__(self):

        print("Initializing controller...")

        self.machine = Machine()

        print("Machine connected to controller.")

        self.selected_part = None

        print("No machine part selected.")

        self.menu_options = [
            "Component Explorer",
            "Diagnostics",
            "Maintenance",
            "User Manual",
            "Exit"
        ]

        self.running = True
        print("Controller initialization complete.")