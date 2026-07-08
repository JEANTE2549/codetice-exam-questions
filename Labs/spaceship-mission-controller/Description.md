# Spaceship Mission Controller

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อตรวจสอบว่า spaceship 1 ลำ สามารถออกเดินทางทำ mission 1 mission ได้หรือไม่

spaceship มีข้อมูลดังนี้:

- ชื่อ spaceship
- fuel
- payload capacity

mission มีข้อมูลดังนี้:

- destination
- distance
- cargo weight

mission ต้องใช้ fuel ตามสูตร:

```text
required_fuel = (distance * 2.0) + (cargo_weight * 1.5)
```

mission จะล้มเหลวถ้า cargo weight เกิน payload capacity หรือ spaceship มี fuel ไม่เพียงพอ

## Input

input มีทั้งหมด 6 บรรทัด:

1. ชื่อ spaceship
2. fuel เป็นจำนวนทศนิยม
3. payload capacity เป็นจำนวนทศนิยม
4. destination
5. distance เป็นจำนวนทศนิยม
6. cargo weight เป็นจำนวนทศนิยม

## Output

ถ้า cargo weight เกินกำหนด ให้แสดงผล:

```text
Mission Failed! Cargo weight exceeds payload capacity.
```

ถ้า fuel ไม่เพียงพอ ให้แสดงผล:

```text
Mission Failed! Insufficient fuel.
```

ถ้า mission สำเร็จ ให้แสดงผล:

```text
Liftoff Success! Spaceship <name> is heading to <destination>. Consumed <required> L. Remaining fuel: <fuel> L.
```

ค่า fuel ต้องแสดงทศนิยม 2 ตำแหน่ง
