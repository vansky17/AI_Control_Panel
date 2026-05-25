def build_menu_lines(controller):
    lines = []
    lines.append("=== AI Control Terminal ===")
    lines.append("")
    lines.append(f"Machine: {controller.machine.name}")
    lines.append(f"Status: {controller.machine.status}")
    lines.append("===================================")
    for index, option in enumerate(controller.menu_options, start=1):
        lines.append(f"{index}. {option}")
    return lines
