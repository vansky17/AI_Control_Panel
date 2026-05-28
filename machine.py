class MachinePart:
    def __init__(self, name, image_path, description, diagnostics):
        self.name = name
        self.image_path = image_path
        self.description = description
        self.diagnostics = diagnostics


class Machine:
    def __init__(self):
        self.name = "Industrial Cooling System"

        self.status = "OFFLINE"

        self.parts = [
            MachinePart(
                "Hydraulics",
                "images/hydraulics.png",
                "Controls coolant pressure and fluid transport.",
                "Pressure stable | Temperature nominal"
            ),
            MachinePart(
                "Dispenser",
                "images/dispenser.png",
                "Regulates internal machine temperature.",
                "Fan speed normal"
            ),
            MachinePart(
                "Control Unit",
                "images/control_unit.png",
                "Processes machine logic and automation.",
                "No active faults"
            ),
            MachinePart(
                "Electrical Panel",
                "images/electrical_panel.png",
                "Distributes electrical power to subsystems.",
                "Voltage stable"
            ),
            MachinePart(
                "Inspection Camera",
                "images/inspection_camera.png",
                "Handles precision alignment and measurement.",
                "Alignment calibrated"
            ),
            MachinePart(
                "Servo Drive",
                "images/servo_drive.png",
                "Prevents system overpressure.",
                "Operational"
            )
        ]
        
print("Machine system initialized.")