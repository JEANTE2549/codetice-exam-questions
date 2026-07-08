def to_celsius(value, unit):
    if unit == "C":
        return value
    if unit == "F":
        return (value - 32) * 5 / 9
    return value - 273.15


def from_celsius(value, unit):
    if unit == "C":
        return value
    if unit == "F":
        return (value * 9 / 5) + 32
    return value + 273.15


temperature = float(input())
from_unit = input().strip().upper()
to_unit = input().strip().upper()

celsius = to_celsius(temperature, from_unit)
converted = from_celsius(celsius, to_unit)
status = "Danger: High Temperature!" if celsius > 100 else "Normal"

print(f"Converted: {converted:.2f} {to_unit}")
print(f"Status: {status}")
