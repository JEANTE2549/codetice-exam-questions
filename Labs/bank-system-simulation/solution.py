class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            return False

        self.balance -= amount
        return True


accounts = {}
command_count = int(input())

for _ in range(command_count):
    parts = input().split()
    command = parts[0]

    if command == "REGISTER":
        acc_no = parts[1]
        name = parts[2]
        balance = float(parts[3])
        accounts[acc_no] = BankAccount(acc_no, name, balance)
        print(f"Registered {acc_no} {name} with balance {balance:.2f} Baht.")

    elif command == "DEPOSIT":
        acc_no = parts[1]
        amount = float(parts[2])
        if acc_no not in accounts:
            print(f"Failed: Account {acc_no} not found.")
            continue

        accounts[acc_no].deposit(amount)
        print(f"Deposited {amount:.2f} Baht to {acc_no}. Balance: {accounts[acc_no].balance:.2f} Baht.")

    elif command == "WITHDRAW":
        acc_no = parts[1]
        amount = float(parts[2])
        if acc_no not in accounts:
            print(f"Failed: Account {acc_no} not found.")
            continue

        if accounts[acc_no].withdraw(amount):
            print(f"Withdrew {amount:.2f} Baht from {acc_no}. Balance: {accounts[acc_no].balance:.2f} Baht.")
        else:
            print(f"Failed: Insufficient balance in {acc_no}.")

    elif command == "TRANSFER":
        from_acc = parts[1]
        to_acc = parts[2]
        amount = float(parts[3])

        if from_acc not in accounts:
            print(f"Failed: Account {from_acc} not found.")
            continue
        if to_acc not in accounts:
            print(f"Failed: Account {to_acc} not found.")
            continue
        if not accounts[from_acc].withdraw(amount):
            print(f"Failed: Insufficient balance in {from_acc}.")
            continue

        accounts[to_acc].deposit(amount)
        print(f"Transferred {amount:.2f} Baht from {from_acc} to {to_acc}.")

print("Final Accounts:")
if accounts:
    for acc_no, account in accounts.items():
        print(f"{acc_no} {account.name}: {account.balance:.2f} Baht")
else:
    print("None")
