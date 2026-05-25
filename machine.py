class MachinePart:
    def __init__(self, name, description, diagnostics):
        self.name = name
        self.description = description
        self.diagnostics = diagnostics


class Machine:
    def __init__(self):
        self.name = "Industrial Cooling System"

        self.status = "Awaiting load"

        self.parts = [
            MachinePart(
                "Hydraulics",
                "Controls coolant pressure and fluid transport.",
                "Pressure stable | Temperature nominal"
            ),
            MachinePart(
                "Dispenser",
                "Regulates internal machine temperature.",
                "Fan speed normal"
            ),
            MachinePart(
                "Control Unit",
                "Processes machine logic and automation.",
                "No active faults"
            ),
            MachinePart(
                "Electrical Panel",
                "Distributes electrical power to subsystems.",
                "Voltage stable"
            ),
            MachinePart(
                "Inspection Camera",
                "Handles precision alignment and measurement.",
                "Alignment calibrated"
            ),
            MachinePart(
                "Servo Drive",
                "Prevents system overpressure.",
                "Operational"
            )
        ]
        
print("Machine system initialized.")