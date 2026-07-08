customer = input().strip()
balance = float(input())
item_count = int(input())
total = 0

for _ in range(item_count):
    input().strip()
    price = float(input())
    qty = int(input())
    total += price * qty

remaining = balance - total

if remaining >= 0:
    print(f"{customer} bought everything. Remaining balance: {remaining:.2f} Baht")
else:
    print(f"Purchase Failed! Missing {-remaining:.2f} Baht")
