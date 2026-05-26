from machine import Machine
from controller import Controller
from ui import render_ui
import time


def main():

    controller = Controller()
    input_user= ""
    while controller.running:
        render_ui(controller)
        input_user = input("Select option:")
        print(input_user)
        if controller.state == "BOOTING":
            if input_user == "Engage" or input_user == "1":
                controller.machine.status = "Loading machine data..."
                render_ui(controller)
                time.sleep(2)  # Simulate delay
                controller.machine.status = "OPERATIONAL"
                controller.state = "OPERATIONAL"
                render_ui(controller)   
        elif controller.state == "OPERATIONAL" and input_user == "1":
            controller.state = "COMPONENT_EXPLORER"
            time.sleep(2)
            render_ui(controller)
                # Handle operational menu option    
                # 

        elif controller.state == "COMPONENT_EXPLORER":
            if input_user.isdigit():
                try:
                    selected_index = int(input_user) - 1
                    if 0 <= selected_index < len(controller.machine.parts):
                        controller.selected_part = controller.machine.parts[selected_index]
                    # render_ui(controller)
                    # time.sleep(2)
                    else:
                        print("Invalid selection. Please try again.")
                except ValueError:
                     print("Invalid input. Please enter a number corresponding to the component.")
            else:
                if input_user == "e" or input_user == "Exit":
                    controller.running = False
                    controller.machine.status = "Terminating session..."
                    render_ui(controller)
                    time.sleep(1)  # Simulate delay
                if input_user == "b" or input_user == "Back":
                    controller.state = "OPERATIONAL"
                    time.sleep(1)
                    render_ui(controller)    

        elif controller.state == "COMPONENT_EXPLORER" and (input_user == "b" or input_user == "Back"):
            controller.state = "OPERATIONAL"
            time.sleep(1)
            render_ui(controller)         
        else:
            if input_user == "e" or input_user == "Exit":
                controller.running = False
                controller.machine.status = "Terminating session..."
                render_ui(controller)
                time.sleep(1)  # Simulate delay1
                

main()

machine = Machine()

print()
print("Machine Name:")
print(machine.name)
print()
print("Machine Status:")
print(machine.status)

print()
print("Machine Parts:")

for part in machine.parts:

    print(f"- {part.name}")
