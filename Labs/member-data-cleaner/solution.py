VALID_DOMAINS = (".com", ".co.th", ".ac.th")


def validate_member(name, email, age_text):
    if "@" not in email or not email.endswith(VALID_DOMAINS):
        return False, "Invalid email"

    try:
        age = int(age_text)
    except ValueError:
        return False, f"Age '{age_text}' is not a valid integer"

    if age < 18 or age > 60:
        return False, f"Age {age} is out of valid range (18-60)"

    return True, age


member_count = int(input())
valid_members = []
errors = []

for _ in range(member_count):
    name = input().strip()
    email = input().strip()
    age_text = input().strip()

    is_valid, result = validate_member(name, email, age_text)
    if is_valid:
        valid_members.append((name, email, result))
    else:
        errors.append(f"Row for {name}: {result}")

print("Valid Members:")
if valid_members:
    for name, email, age in valid_members:
        print(f"{name} ({email}, {age})")
else:
    print("None")

print("Errors:")
if errors:
    for error in errors:
        print(error)
else:
    print("None")

print(f"Summary: {len(valid_members)} valid, {len(errors)} invalid")
