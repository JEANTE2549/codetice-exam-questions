# Flight Seat Reservation

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อจัดการ seat reservation request สำหรับ flight 1 เที่ยว

โปรแกรมจะได้รับข้อมูลดังนี้:

- seat ทั้งหมดที่เปิดให้จองใน flight
- seat ที่ถูก reserved ไปแล้ว
- price ของ seat แต่ละ zone
- รายการ reservation request

zone ของ seat คืออักษรตัวแรกของ seat code เช่น zone ของ `A1` คือ `A`

## Input

บรรทัดแรกเป็นจำนวนเต็ม `A` แทนจำนวน seat ทั้งหมดที่เปิดให้จอง

อีก `A` บรรทัดถัดมาเป็น seat code บรรทัดละ 1 code

บรรทัดถัดมาเป็นจำนวนเต็ม `B` แทนจำนวน seat ที่ถูก reserved ไปแล้ว

อีก `B` บรรทัดถัดมาเป็น seat code ที่ถูก reserved ไปแล้ว บรรทัดละ 1 code

บรรทัดถัดมาเป็นจำนวนเต็ม `P` แทนจำนวนข้อมูล price ของแต่ละ zone

ข้อมูล price แต่ละ zone ใช้ 2 บรรทัด:

1. ตัวอักษร zone
2. price เป็นจำนวนทศนิยม

บรรทัดถัดมาเป็นจำนวนเต็ม `Q` แทนจำนวน reservation request

อีก `Q` บรรทัดถัดมาเป็น seat code ที่ต้องการจอง บรรทัดละ 1 code

## Output

สำหรับแต่ละ request ให้แสดงผล 1 บรรทัด

ถ้า seat ไม่มีอยู่จริง ให้แสดงผล:

```text
Failed: Seat <seat_no> does not exist on this flight.
```

ถ้า seat ถูก reserved ไปแล้ว ให้แสดงผล:

```text
Failed: Seat <seat_no> is already reserved by another passenger.
```

ถ้า reservation สำเร็จ ให้แสดงผล:

```text
Success: Reserved seat <seat_no>. Price: <price> Baht.
```

price ต้องแสดงทศนิยม 2 ตำแหน่ง
