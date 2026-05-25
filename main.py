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
        if not controller.ai_engaged:
            if input_user == "Engage" or input_user == "1":
                controller.machine.status = "Loading machine data..."
                render_ui(controller)
                time.sleep(2)  # Simulate delay
                controller.ai_engaged = True
                controller.machine.status = "OPERATIONAL"
                render_ui(controller)               
        else:
            if input_user == "5":
                controller.running = False
                controller.machine.status = "Terminating session..."
                time.sleep(2)  # Simulate delay
                

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
