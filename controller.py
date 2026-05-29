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
        # Audio flags:
        self.component_explorer_visited = False
        self.welcome_visited = False
        self.license_visited = False
        self.options_visited = False
        print("Controller initialization complete.")