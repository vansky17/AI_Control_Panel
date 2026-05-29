import tkinter as tk
from monitor_info import build_info_lines
from monitor_menu import build_menu_lines
import time
from PIL import Image, ImageTk
import winsound
import os

def start_ui(controller):
    print("Pillow works")
     # =========================
    # WINDOW
    # =========================

    root = tk.Tk()
    root.configure(bg="black")
    root.title(
        "ROOM 4 - INDUSTRIAL SERVICE TERMINAL"
    )

    root.geometry("1200x700")

    root.after(1000, lambda: winsound.PlaySound("sounds/welcome.wav", winsound.SND_FILENAME))

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
        relief="solid",
        bg="black"
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
        relief="solid",
        bg="black"
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
          # Simulate delay
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

        if not controller.options_visited:
            root.after(1000, lambda: winsound.PlaySound("sounds/options_menu.wav", winsound.SND_FILENAME))
            controller.options_visited = True
    right_button_frame = tk.Frame(
    right_frame,
    bg="black"
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
        image_label.config(image="")
        image_label.image = None
        
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
        winsound.PlaySound(
        "sounds/clicky.wav",
        winsound.SND_FILENAME
        )
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
        if option == "Component Explorer" and not controller.component_explorer_visited:    
            root.after(1000, lambda: winsound.PlaySound("sounds/Compenent_Explorer.wav", winsound.SND_FILENAME))
            controller.component_explorer_visited = True
        back_button.config(state="normal")
        refresh_ui()
    def select_part(part):
        winsound.PlaySound(
        "sounds/clicky.wav",
        winsound.SND_FILENAME
        )
        controller.selected_part = part

        refresh_ui()
#    Four menu buttons, initially hidden, will be shown when the AI is engaged. Each button will correspond to a menu option and will call the open_menu function with the appropriate option when clicked.
    menu_buttons = []

    for index, option in enumerate(controller.menu_options):

        button = tk.Button(
        text=option,
        width=20,
        font=("Consolas", 12),
        command=lambda opt=option: open_menu(opt),
        bg="#001100",
        fg="#55FF55",
        activebackground="#003300",
        activeforeground="#AAFFAA"
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
        font=("Consolas", 14,"bold"),
        bg="#001100",
        fg="#55FF55",
        activebackground="#003300",
        activeforeground="#AAFFAA"
   )

    engage_button.pack(side="left", padx=10)

    exit_button = tk.Button(
    right_button_frame,
    text="Exit",
    font=("Consolas", 14,"bold"),
    state="disabled",
    command=exit_session,
    bg="#001100",
    fg="#55FF55",
    activebackground="#003300",
    activeforeground="#AAFFAA"
    )

    exit_button.pack(side="left", padx=10)

    back_button = tk.Button(
    right_button_frame,
    text="Back",
    font=("Consolas", 14,"bold"),
    state="disabled",
    command=go_back,
    bg="#001100",
    fg="#55FF55",
    activebackground="#003300",
    activeforeground="#AAFFAA"
    )

    back_button.pack(side="left", padx=10)
  
    # LEFT LABEL

    left_label = tk.Label(
        left_frame,
        text="LEFT MONITOR",
        justify="left",
        anchor="nw",
        font=("Consolas", 12),
        bg="black",
        fg="#00FF00"
    )

    left_label.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )
    #  images:
    image_label = tk.Label(left_frame)

    image_label.pack(
        pady=10
    )
    # RIGHT LABEL


    right_label = tk.Label(
        right_frame,
        text="RIGHT MONITOR",
        justify="left",
        anchor="nw",
        font=("Consolas", 12),
        bg="black",
        fg="#00FF00"
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
        if controller.selected_part and controller.selected_part.image_path:
            try:
                image = Image.open(controller.selected_part.image_path)
                image = image.resize((400, 300))
                photo = ImageTk.PhotoImage(image)
                image_label.config(image=photo)
                image_label.image = photo  # Keep a reference to prevent garbage collection
            except Exception as e:
                print(f"Error loading image: {e}")
                image_label.config(image="")

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