from machine import Machine


class Controller:
    def __init__(self):

        print("Initializing controller...")

        self.machine = Machine()
        self.selected_part = None

        self.menu_options = [
            "Component Explorer",
            "Diagnostics",
            "Maintenance",
            "User Manual",
        ]

        self.running = True
        # self.ai_engaged = False
        self.state = "BOOTING"
        print("Controller initialization complete.")