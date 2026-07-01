training_days = int(input(""))
training_hours_per_day = float(input(""))
break_minutes_per_day = int(input(""))


total_training_hours = training_days * training_hours_per_day
total_break_hours = training_days * break_minutes_per_day / 60
actual_training_hours = total_training_hours - total_break_hours

print("=== World Cup Training Summary ===")
print(f"Training Days: {training_days}")
print(f"Training Hours Before Breaks: {total_training_hours:.1f}")
print(f"Break Time: {total_break_hours:.1f}")
print(f"Actual Training Hours: {actual_training_hours:.1f}")
