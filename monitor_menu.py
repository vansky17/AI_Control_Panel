def build_menu_lines(controller):
    lines = []
    lines.append("=== AI Control Terminal ===")
    lines.append("")
    if not controller.ai_engaged:
        lines.append(f"Machine: -----")
        lines.append(f"Status: {controller.machine.status}")
        lines.append("===================================")
        lines.append("1. Engage AI")
    else:
        lines.append(f"Machine: {controller.machine.name}")
        lines.append(f"Status: {controller.machine.status}")
        lines.append("===================================")
        for index, option in enumerate(controller.menu_options, start=1):
            lines.append(f"{index}. {option}")
    return lines
