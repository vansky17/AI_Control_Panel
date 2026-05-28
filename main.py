from machine import Machine
from controller import Controller
from ui import start_ui
import time

from controller import Controller
from ui import start_ui


def main():

    controller = Controller()

    start_ui(controller)


main()

# def main():

#     controller = Controller()
#     start_ui(controller)
#     input_user= ""
#     while controller.running:
#         refresh_ui(controller)
#         input_user = input("Select option:")
#         print(input_user)
#         if controller.state == "BOOTING":
#             if input_user == "Engage" or input_user == "1":
#                 controller.machine.status = "Loading machine data..."
#                 refresh_ui(controller)
#                 time.sleep(2)  # Simulate delay
#                 controller.machine.status = "OPERATIONAL"
#                 controller.state = "OPERATIONAL"
#                 refresh_ui(controller)   
#         elif controller.state == "OPERATIONAL" and input_user == "1":
#             controller.state = "COMPONENT_EXPLORER"
#             time.sleep(2)
#             refresh_ui(controller)
#         elif controller.state == "COMPONENT_EXPLORER":
#             if input_user.isdigit():
#                 try:
#                     selected_index = int(input_user) - 1
#                     if 0 <= selected_index < len(controller.machine.parts):
#                         controller.selected_part = controller.machine.parts[selected_index]
#                     else:
#                         print("Invalid selection. Please try again.")
#                 except ValueError:
#                      print("Invalid input. Please enter a number corresponding to the component.")
#             else:
#                 if input_user == "e" or input_user == "Exit":
#                     controller.running = False
#                     controller.machine.status = "Terminating session..."
#                     refresh_ui(controller)
#                     time.sleep(1)  # Simulate delay
#                 if input_user == "b" or input_user == "Back":
#                     controller.state = "OPERATIONAL"
#                     time.sleep(1)
#                     refresh_ui(controller)    
#         elif controller.state in (
#            "COMPONENT_EXPLORER",
#            "DIAGNOSTICS",
#            "MAINTENANCE",
#            "USERMANUAL"
#         ) and input_user in ("b", "Back"):
#             controller.state = "OPERATIONAL"
#             time.sleep(1)
#             refresh_ui(controller)
#         elif controller.state == "OPERATIONAL" and input_user == "2":
#             controller.state = "DIAGNOSTICS"
#             time.sleep(1)
#             refresh_ui(controller)
#         elif controller.state == "OPERATIONAL" and input_user == "3":
#             controller.state = "MAINTENANCE"
#             time.sleep(1)
#             refresh_ui(controller)
#         elif controller.state == "OPERATIONAL" and input_user == "4":
#             controller.state = "USERMANUAL"
#             time.sleep(1)
#             refresh_ui(controller)
#         else:
#             if input_user == "e" or input_user == "Exit":
#                 controller.running = False
#                 controller.machine.status = "Terminating session..."
#                 refresh_ui(controller)
#                 time.sleep(1)  # Simulate delay1
                

# main()

# machine = Machine()

# print()
# print("Machine Name:")
# print(machine.name)
# print()
# print("Machine Status:")
# print(machine.status)

# print()
# print("Machine Parts:")

# for part in machine.parts:

#     print(f"- {part.name}")
