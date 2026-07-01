import json

budget = int(input())
players_json = input()
targets = input().split()

market_prices = json.loads(players_json)

total_cost = 0
for player in targets:
    total_cost += market_prices[player]
    
if total_cost <= budget:
    remaining = budget - total_cost
    print(f"Deal! You bought everyone for {total_cost}. Remaining budget: {remaining}")
else:
    print("Deal Failed! Not enough budget.")
