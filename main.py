from machine import Machine
from controller import Controller
from ui import render_ui


def main():

    controller = Controller()

    render_ui(controller)


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