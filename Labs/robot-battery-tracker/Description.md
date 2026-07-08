# Robot Battery Tracker

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อจำลองการเคลื่อนที่ของ robot บนพิกัด 2 มิติ

robot เริ่มต้นที่ตำแหน่ง `(0, 0)` และมี battery `100` หน่วย

การเดิน 1 ก้าว ใช้ battery `4` หน่วย ถ้า battery ไม่พอสำหรับ command นั้น robot จะไม่เคลื่อนที่

Direction ที่รองรับ:

- `UP` เพิ่มค่า `y`
- `DOWN` ลดค่า `y`
- `RIGHT` เพิ่มค่า `x`
- `LEFT` ลดค่า `x`

## Input

บรรทัดแรกเป็นชื่อ robot

บรรทัดที่สองเป็นจำนวนเต็ม `N` แทนจำนวน movement command

แต่ละ command ใช้ข้อมูล 2 บรรทัด:

1. direction: `UP`, `DOWN`, `LEFT` หรือ `RIGHT`
2. จำนวนก้าว เป็นจำนวนเต็ม

## Output

หลังจาก move สำเร็จแต่ละครั้ง ให้แสดงผล:

```text
<name> moved to (<x>, <y>). Battery: <battery>
```

ถ้า battery ไม่เพียงพอ ให้แสดงผล:

```text
<name> has insufficient battery to move.
```

หลังจากทำครบทุก command ให้แสดงผล:

```text
Status: <name> at (<x>, <y>), Battery: <battery>
```
