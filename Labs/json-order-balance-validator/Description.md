# Order Balance Validator

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่ออ่านข้อมูล order 1 รายการ แล้วตรวจสอบว่า customer มี balance เพียงพอสำหรับซื้อ item ทั้งหมดหรือไม่

order ประกอบด้วย:

- customer name
- balance
- item list

แต่ละ item ประกอบด้วย:

- item name
- price
- qty

## Input

input มีรูปแบบดังนี้:

1. customer name
2. balance เป็นจำนวนทศนิยม
3. item count เป็นจำนวนเต็ม
4. สำหรับแต่ละ item ให้รับข้อมูล 3 บรรทัด:
   - item name
   - price เป็นจำนวนทศนิยม
   - qty เป็นจำนวนเต็ม

## Output

ถ้า balance เพียงพอ ให้แสดงผล:

```text
<customer> bought everything. Remaining balance: <remaining> Baht
```

ถ้า balance ไม่เพียงพอ ให้แสดงผล:

```text
Purchase Failed! Missing <missing> Baht
```

จำนวนเงินต้องแสดงทศนิยม 2 ตำแหน่ง

## Note

- ราคารวมคือผลรวมของ `price * qty` ของ item ทุกรายการ
- โจทย์ข้อนี้ไม่ต้องอ่านหรือเขียนไฟล์
- โจทย์ข้อนี้ไม่ต้องใช้ `import`
