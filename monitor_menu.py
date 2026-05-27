from monitor_info import build_info_lines


def build_menu_lines(controller):
    lines = []
    lines.append("=== AI Control Terminal ===")
    lines.append("")
    if controller.state == "BOOTING":
        lines.append(f"Machine: -----")
        lines.append(f"Status: {controller.machine.status}")
        lines.append("===================================")
        lines.append("1. Engage AI")
        lines.append("")
        lines.append("For Exit type 'e' or 'Exit'")
    elif controller.state == "OPERATIONAL":
        lines.append(f"Machine: {controller.machine.name}")
        lines.append(f"Status: {controller.machine.status}")
        lines.append("===================================")
        for index, option in enumerate(controller.menu_options, start=1):
            lines.append(f"{index}. {option}")
        lines.append("===================================")
        lines.append("")
        lines.append("For Exit type 'e' or 'Exit'")
    elif controller.state == "COMPONENT_EXPLORER":
        for index, part in enumerate(controller.machine.parts, start=1):
            lines.append(f"{index}. {part.name}")
        lines.append("===================================")
        lines.append("")
        lines.append("For BACK type 'b' or 'Back'")
    elif controller.state == "DIAGNOSTICS":
        lines.append(f"Machine: {controller.machine.name}")
        lines.append(f"Status: {controller.machine.status}")
        lines.append("===================================")
        lines.append("Diagnostics Information:")
        lines.append("System is operating within normal parameters.")
        lines.append("===================================")
        lines.append("")
        lines.append("For BACK type 'b' or 'Back'")
    elif controller.state == "MAINTENANCE":
        lines.append(f"Machine: {controller.machine.name}")
        lines.append(f"Status: {controller.machine.status}")
        lines.append("===================================")
        lines.append("This option is not available with your license.")
        lines.append("Please select another option.")          
        lines.append("===================================")
        lines.append("")
        lines.append("For BACK type 'b' or 'Back'")
    elif controller.state == "USERMANUAL":
        lines.append(f"Machine: {controller.machine.name}")
        lines.append(f"Status: {controller.machine.status}")
        lines.append("===================================")
        lines.append("YOU WON'T READ THIS ANYWAY.")
        lines.append("SO NO MANUAL FOR YOU.")          
        lines.append("===================================")
        lines.append("")
        lines.append("For BACK type 'b' or 'Back'")
    return lines
