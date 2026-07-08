# Stock Portfolio Simulator

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อจำลองการซื้อขาย stock อย่างง่ายใน portfolio

initial portfolio ประกอบด้วย:

- cash
- stock ticker และจำนวน stock ที่ถืออยู่

จากนั้นโปรแกรมต้อง process command:

- `BUY <ticker> <qty> <price>`
- `SELL <ticker> <qty> <price>`
- `SHOW`

## Input

บรรทัดแรกเป็น cash ของ initial portfolio เป็นจำนวนทศนิยม

บรรทัดที่สองเป็นจำนวนเต็ม `S` แทนจำนวน stock ticker ที่ถืออยู่ตอนเริ่มต้น

อีก `S` บรรทัดถัดมาเป็นข้อมูล stock ในรูปแบบ `<ticker> <qty>`

บรรทัดถัดมาเป็นจำนวนเต็ม `N` แทนจำนวน command

อีก `N` บรรทัดถัดมาเป็น command บรรทัดละ 1 command

## Output

ถ้า buy stock สำเร็จ ให้แสดงผล:

```text
Bought <qty> <ticker> for <cost> Baht. Cash: <cash> Baht.
```

ถ้า buy stock ไม่สำเร็จ ให้แสดงผล:

```text
Failed: Not enough cash to buy <qty> <ticker>.
```

ถ้า sell stock สำเร็จ ให้แสดงผล:

```text
Sold <qty> <ticker> for <income> Baht. Cash: <cash> Baht.
```

ถ้า sell stock ไม่สำเร็จ ให้แสดงผล:

```text
Failed: Not enough <ticker> shares to sell <qty>.
```

เมื่อเจอ command `SHOW` ให้แสดงผล:

```text
Cash: <cash> Baht
Stocks:
<ticker>: <qty>
```

ถ้าไม่มี stock ใน portfolio ให้แสดง `None` ใต้บรรทัด `Stocks:`

จำนวนเงินต้องแสดงทศนิยม 2 ตำแหน่ง

โจทย์ข้อนี้ไม่ต้องใช้ `import`
