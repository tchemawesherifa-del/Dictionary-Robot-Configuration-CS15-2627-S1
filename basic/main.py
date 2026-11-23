
robot = {
    "name": "leenieeee",
    "model": "leniez-67bot",
    "battery": 67,
    "speed": 6.7,
    "mode": "cutesieness "
}

print("===== LEENIEEEE'S ROBOT EMPIRE =====")

print("Robot name:", robot["name"])
print("Robot model:", robot["model"])

robot["battery"] = 100

robot["color"] = " pink"

robot.pop("mode")

print("\nTotal settings:", len(robot))

print("\n===== HELENES ROBOT SETTINGS ===")

for key, value in robot.items():
    print(key, ":", value)
