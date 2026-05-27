def build_info_lines(selected_part):

    lines = []

    if selected_part is None:

        lines.append("No component selected.")

        return lines

    lines.append("Selected Component:")
    lines.append(selected_part.name)

    lines.append("")
    lines.append(selected_part.image_path)

    lines.append("")

    lines.append("Description:")
    lines.append(selected_part.description)

    lines.append("")

    lines.append("Diagnostics:")
    lines.append(selected_part.diagnostics)

    return lines