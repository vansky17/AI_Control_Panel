from monitor_info import build_info_lines


def build_menu_lines(controller):
    lines = []
    lines.append("=== AI Control Terminal ===")
    lines.append("")
    if controller.state == "BOOTING":
        lines.append(f"Machine: -----")
        lines.append(f"Status: {controller.machine.status}")
        lines.append("===================================")
    elif controller.state == "OPERATIONAL":
        lines.append(f"Machine: {controller.machine.name}")
        lines.append(f"Status: {controller.machine.status}")
        lines.append("===================================")
        # for index, option in enumerate(controller.menu_options, start=1):
        #     lines.append(f"{index}. {option}")
        lines.append("Select an option:")
    elif controller.state == "COMPONENT_EXPLORER":
        # for index, part in enumerate(controller.machine.parts, start=1):
        #     lines.append(f"{index}. {part.name}")
        lines.append("Welcome to the Component Explorer.")
        lines.append("Choose a component to view details.")
        lines.append("===================================")
    elif controller.state == "DIAGNOSTICS":
        lines.append(f"Machine: {controller.machine.name}")
        lines.append(f"Status: {controller.machine.status}")
        lines.append("===================================")
        lines.append("Diagnostics Information:")
        lines.append("System is operating within normal parameters.")
        lines.append("===================================")
    elif controller.state == "MAINTENANCE":
        lines.append(f"Machine: {controller.machine.name}")
        lines.append(f"Status: {controller.machine.status}")
        lines.append("===================================")
        lines.append("This option is not available with your license.")
        lines.append("Please select another option.")          
        lines.append("===================================")
    elif controller.state == "USERMANUAL":
        lines.append(f"Machine: {controller.machine.name}")
        lines.append(f"Status: {controller.machine.status}")
        lines.append("===================================")
        lines.append("YOU WON'T READ THIS MANUAL ANYWAY.")
        lines.append("SO NO MANUAL FOR YOU.")          
        lines.append("===================================")
    return lines
