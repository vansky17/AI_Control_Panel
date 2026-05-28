import tkinter as tk
from monitor_info import build_info_lines
from monitor_menu import build_menu_lines
import time
from PIL import Image, ImageTk

def start_ui(controller):
    print("Pillow works")
     # =========================
    # WINDOW
    # =========================

    root = tk.Tk()

    root.title(
        "ROOM 4 - INDUSTRIAL SERVICE TERMINAL"
    )

    root.geometry("1200x700")

    # =========================
    # MAIN FRAME
    # =========================

    main_frame = tk.Frame(root)

    main_frame.pack(
        fill="both",
        expand=True
    )

    # =========================
    # LEFT MONITOR
    # =========================

    left_frame = tk.Frame(
        main_frame,
        bd=2,
        relief="solid"
    )

    left_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    # =========================
    # RIGHT MONITOR
    # =========================

    right_frame = tk.Frame(
        main_frame,
        bd=2,
        relief="solid"
    )

    right_frame.pack(
        side="right",
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )
    menu_button_frame = tk.Frame(
    right_frame
   )

    menu_button_frame.pack(
    pady=20
   )
   #Button Commands 
    def engage_ai():
        controller.machine.status = "Loading machine data..."
        refresh_ui()
        time.sleep(1)  # Simulate delay
        controller.machine.status = "OPERATIONAL"
        controller.state = "OPERATIONAL"
        refresh_ui()
        engage_button.config(state="disabled")
        exit_button.config(state="normal")
        for index, button in enumerate(menu_buttons):
            button.place(
            in_=right_frame,
            x=40,
            y=170 + index * 45
            )

    right_button_frame = tk.Frame(
    right_frame
    )

    right_button_frame.pack(
        side="bottom",
        pady=20
    )
    def exit_session():

        controller.machine.status = "Terminating session..."

        refresh_ui()

        controller.state = "BOOTING"

        controller.machine.status = "OFFLINE"

        controller.selected_part = None
        
        back_button.config(state="disabled")
        refresh_ui()

        engage_button.config(state="normal")

        exit_button.config(state="disabled")
        for button in menu_buttons:
            button.place_forget()
        for button in component_buttons:
            button.place_forget()
    def go_back():

        controller.state = "OPERATIONAL"

        refresh_ui()
        back_button.config(state="disabled")
        for index, button in enumerate(menu_buttons):
            button.place(
            in_=right_frame,
            x=40,
            y=170 + index * 45
            )
        for button in component_buttons:
            button.place_forget()
    def open_menu(option):
        for button in menu_buttons:
            button.place_forget()
        if option == "Component Explorer":
            controller.state = "COMPONENT_EXPLORER"
            for index, button in enumerate(component_buttons):
                button.place(
                in_=right_frame,
                x=40,
                y=170 + index * 45
                )

        elif option == "Diagnostics":
            controller.state = "DIAGNOSTICS"
        elif option == "Maintenance":
            controller.state = "MAINTENANCE"
        elif option == "User Manual":
            controller.state = "USERMANUAL"
        
        back_button.config(state="normal")
        refresh_ui()
    def select_part(part):

        controller.selected_part = part

        refresh_ui()
#    Four menu buttons, initially hidden, will be shown when the AI is engaged. Each button will correspond to a menu option and will call the open_menu function with the appropriate option when clicked.
    menu_buttons = []

    for index, option in enumerate(controller.menu_options):

        button = tk.Button(
        text=option,
        width=20,
        font=("Consolas", 12),
        command=lambda opt=option: open_menu(opt)
        )

        menu_buttons.append(button)  
        # Hide buttons on booting screen
    for button in menu_buttons:
        button.place_forget()  

# Parts buttons will be created dynamically when the Component Explorer menu is opened, so we won't create them here. Instead, we'll generate them in the open_menu function when the "Component Explorer" option is selected.
    component_buttons = []

    for part in controller.machine.parts:

        button = tk.Button(
        text=part.name,
        width=20,
        font=("Consolas", 12),
        command=lambda p=part: select_part(p)
        )

        component_buttons.append(button)
        
    # BUTTONs

    engage_button = tk.Button(
        right_button_frame,
        text="Engage AI",
        command=engage_ai,
        font=("Consolas", 12)
   )

    engage_button.pack(side="left", padx=10)

    exit_button = tk.Button(
    right_button_frame,
    text="Exit",
    font=("Consolas", 12),
    state="disabled",
    command=exit_session
    )

    exit_button.pack(side="left", padx=10)

    back_button = tk.Button(
    right_button_frame,
    text="Back",
    font=("Consolas", 12),
    state="disabled",
    command=go_back
)

    back_button.pack(side="left", padx=10)
  
    # LEFT LABEL

    left_label = tk.Label(
        left_frame,
        text="LEFT MONITOR",
        justify="left",
        anchor="nw",
        font=("Consolas", 12)
    )

    left_label.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    # RIGHT LABEL


    right_label = tk.Label(
        right_frame,
        text="RIGHT MONITOR",
        justify="left",
        anchor="nw",
        font=("Consolas", 12)
    )

    right_label.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )
   
 
    # REFRESH UI


    def refresh_ui():

        info_lines = build_info_lines(
            controller.selected_part
        )

        menu_lines = build_menu_lines(
            controller
        )

        left_label.config(
            text="\n".join(info_lines)
        )

        right_label.config(
            text="\n".join(menu_lines)
        )

  
    # INITIAL REFRESH


    refresh_ui()
   
    # refresh_ui()
  
    # START TKINTER


    root.mainloop()















# from monitor_info import build_info_lines
# from monitor_menu import build_menu_lines
# import os


# MONITOR_WIDTH =50


# def pad_lines(lines, total_lines):
#     while len(lines) < total_lines:
#         lines.append("")

#     return lines


# def render_ui(controller):
#     os.system("cls")
#     info_lines = build_info_lines(controller.selected_part)

#     menu_lines = build_menu_lines(controller)

#     total_lines = max(len(info_lines), len(menu_lines))
#     info_lines = pad_lines(info_lines, total_lines)
#     menu_lines = pad_lines(menu_lines, total_lines)

#     print("=" * 100)
#     print("ROOM 4 - INDUSTRIAL SERVICE TERMINAL")
#     print("=" * 100)
#     print()

#     left_header = "LEFT MONITOR"
#     right_header = "RIGHT MONITOR"

#     print(
#         f"+{'-' * MONITOR_WIDTH}+  +{'-' * MONITOR_WIDTH}+"
#     )

#     print(
#         f"|{left_header:^{MONITOR_WIDTH}}|  |{right_header:^{MONITOR_WIDTH}}|"
#     )

#     print(
#         f"+{'-' * MONITOR_WIDTH}+  +{'-' * MONITOR_WIDTH}+"
#     )

#     for left, right in zip(info_lines, menu_lines):

#         print(
#             f"| {left:<{MONITOR_WIDTH - 2}}|  "
#             f"| {right:<{MONITOR_WIDTH - 2}}|"
#         )

#     print(
#         f"+{'-' * MONITOR_WIDTH}+  +{'-' * MONITOR_WIDTH}+"
#     )