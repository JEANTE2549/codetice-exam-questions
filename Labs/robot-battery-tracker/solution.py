class Robot:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.battery = 100

    def move(self, direction, steps):
        required_battery = steps * 4
        if self.battery < required_battery:
            print(f"{self.name} has insufficient battery to move.")
            return

        if direction == "UP":
            self.y += steps
        elif direction == "DOWN":
            self.y -= steps
        elif direction == "RIGHT":
            self.x += steps
        elif direction == "LEFT":
            self.x -= steps

        self.battery -= required_battery
        print(f"{self.name} moved to ({self.x}, {self.y}). Battery: {self.battery}")

    def status(self):
        print(f"Status: {self.name} at ({self.x}, {self.y}), Battery: {self.battery}")


robot = Robot(input().strip())
command_count = int(input())

for _ in range(command_count):
    direction = input().strip().upper()
    steps = int(input())
    robot.move(direction, steps)

robot.status()
