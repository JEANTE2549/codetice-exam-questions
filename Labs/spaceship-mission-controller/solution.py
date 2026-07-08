class Spaceship:
    def __init__(self, name, fuel, payload_capacity):
        self.name = name
        self.fuel = fuel
        self.payload_capacity = payload_capacity


class Mission:
    def __init__(self, destination, distance, cargo_weight):
        self.destination = destination
        self.distance = distance
        self.cargo_weight = cargo_weight

    def launch(self, spaceship):
        if self.cargo_weight > spaceship.payload_capacity:
            print("Mission Failed! Cargo weight exceeds payload capacity.")
            return False

        required_fuel = (self.distance * 2.0) + (self.cargo_weight * 1.5)
        if spaceship.fuel < required_fuel:
            print("Mission Failed! Insufficient fuel.")
            return False

        spaceship.fuel -= required_fuel
        print(
            f"Liftoff Success! Spaceship {spaceship.name} is heading to {self.destination}. "
            f"Consumed {required_fuel:.2f} L. Remaining fuel: {spaceship.fuel:.2f} L."
        )
        return True


name = input().strip()
fuel = float(input())
payload_capacity = float(input())
destination = input().strip()
distance = float(input())
cargo_weight = float(input())

spaceship = Spaceship(name, fuel, payload_capacity)
mission = Mission(destination, distance, cargo_weight)
mission.launch(spaceship)
