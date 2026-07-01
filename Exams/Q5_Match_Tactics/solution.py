class Player:
    def __init__(self, name, stamina):
        self.name = name
        self.stamina = int(stamina)

class Attacker(Player):
    def shoot(self):
        if self.stamina >= 10:
            self.stamina -= 10
            print(f"{self.name} shoots the ball! Stamina left: {self.stamina}")
        else:
            print(f"{self.name} is too tired to shoot.")

class Defender(Player):
    def tackle(self):
        if self.stamina >= 15:
            self.stamina -= 15
            print(f"{self.name} tackles! Stamina left: {self.stamina}")
        else:
            print(f"{self.name} is too tired to tackle.")

def main():
    n = int(input())
    players = {}
    
    for _ in range(n):
        parts = input().split()
        cmd = parts[0]
        
        if cmd == "CREATE":
            role = parts[1]
            name = parts[2]
            stamina = parts[3]
            
            if role == "Attacker":
                players[name] = Attacker(name, stamina)
            elif role == "Defender":
                players[name] = Defender(name, stamina)
                
        elif cmd == "ACTION":
            name = parts[1]
            action = parts[2]
            
            p = players[name]
            if action == "shoot":
                p.shoot()
            elif action == "tackle":
                p.tackle()

if __name__ == "__main__":
    main()
