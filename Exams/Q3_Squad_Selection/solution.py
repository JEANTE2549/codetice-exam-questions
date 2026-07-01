n = int(input())
squad = {}
positions_order = []

for _ in range(n):
    data = input().split()
    name = data[0]
    position = data[1]
    
    if position not in squad:
        squad[position] = []
        positions_order.append(position)
        
    squad[position].append(name)
    
for pos in positions_order:
    print(f"Position: {pos}")
    for player in squad[pos]:
        print(f"- {player}")
