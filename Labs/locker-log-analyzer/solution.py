log_count = int(input())
lockers = {}

for _ in range(log_count):
    locker_id, member_name, action = input().strip().split(",")
    lockers.setdefault(locker_id, None)

    if action == "RENT":
        lockers[locker_id] = member_name
    elif action == "RETURN":
        lockers[locker_id] = None

for locker_id in sorted(lockers):
    member_name = lockers[locker_id]
    if member_name is None:
        print(f"{locker_id}: Available (None)")
    else:
        print(f"{locker_id}: Occupied ({member_name})")
