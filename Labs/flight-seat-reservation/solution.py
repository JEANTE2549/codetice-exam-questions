available_count = int(input())
available_seats = set()
for _ in range(available_count):
    available_seats.add(input().strip())

booked_count = int(input())
booked_seats = set()
for _ in range(booked_count):
    booked_seats.add(input().strip())

price_count = int(input())
seat_prices = {}
for _ in range(price_count):
    zone = input().strip()
    price = float(input())
    seat_prices[zone] = price


def reserve_seat(seat_no):
    if seat_no not in available_seats:
        return False, f"Failed: Seat {seat_no} does not exist on this flight."

    if seat_no in booked_seats:
        return False, f"Failed: Seat {seat_no} is already reserved by another passenger."

    booked_seats.add(seat_no)
    price = seat_prices[seat_no[0]]
    return True, f"Success: Reserved seat {seat_no}. Price: {price:.2f} Baht."


request_count = int(input())
for _ in range(request_count):
    requested_seat = input().strip()
    _, message = reserve_seat(requested_seat)
    print(message)
