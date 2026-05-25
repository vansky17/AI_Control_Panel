from monitor_info import build_info_lines
from monitor_menu import build_menu_lines


MONITOR_WIDTH = 45


def pad_lines(lines, total_lines):
    while len(lines) < total_lines:
        lines.append("")

    return lines


def render_ui(controller):

    info_lines = build_info_lines(controller.selected_part)

    menu_lines = build_menu_lines(controller)

    total_lines = max(len(info_lines), len(menu_lines))
    info_lines = pad_lines(info_lines, total_lines)
    menu_lines = pad_lines(menu_lines, total_lines)

    print("=" * 100)
    print("ROOM 4 - INDUSTRIAL SERVICE TERMINAL")
    print("=" * 100)
    print()

    left_header = "LEFT MONITOR"
    right_header = "RIGHT MONITOR"

    print(
        f"+{'-' * MONITOR_WIDTH}+  +{'-' * MONITOR_WIDTH}+"
    )

    print(
        f"|{left_header:^{MONITOR_WIDTH}}|  |{right_header:^{MONITOR_WIDTH}}|"
    )

    print(
        f"+{'-' * MONITOR_WIDTH}+  +{'-' * MONITOR_WIDTH}+"
    )

    for left, right in zip(info_lines, menu_lines):

        print(
            f"| {left:<{MONITOR_WIDTH - 2}}|  "
            f"| {right:<{MONITOR_WIDTH - 2}}|"
        )

    print(
        f"+{'-' * MONITOR_WIDTH}+  +{'-' * MONITOR_WIDTH}+"
    )