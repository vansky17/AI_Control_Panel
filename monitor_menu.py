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
    if controller.state == "OPERATIONAL":
        lines.append(f"Machine: {controller.machine.name}")
        lines.append(f"Status: {controller.machine.status}")
        lines.append("===================================")
        for index, option in enumerate(controller.menu_options, start=1):
            lines.append(f"{index}. {option}")
        lines.append("===================================")
        lines.append("")
        lines.append("For Exit type 'e' or 'Exit'")
    if controller.state == "COMPONENT_EXPLORER":
        for index, part in enumerate(controller.machine.parts, start=1):
            lines.append(f"{index}. {part.name}")
        lines.append("===================================")
        lines.append("")
        lines.append("For BACK type 'b' or 'Back'")
    return lines
