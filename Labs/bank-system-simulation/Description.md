# Bank Command Simulation

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อจำลองการทำงานของ bank account ผ่านชุด command

แต่ละ account มีข้อมูลดังนี้:

- เลขบัญชี
- ชื่อเจ้าของบัญชี
- ยอดเงินคงเหลือ

Command ที่รองรับ:

- `REGISTER <acc_no> <name> <initial_balance>`
- `DEPOSIT <acc_no> <amount>`
- `WITHDRAW <acc_no> <amount>`
- `TRANSFER <from_acc> <to_acc> <amount>`

## Input

บรรทัดแรกเป็นจำนวนเต็ม `N` แทนจำนวน command

อีก `N` บรรทัดถัดมาเป็น command บรรทัดละ 1 command

ชื่อเจ้าของบัญชีจะไม่มีช่องว่าง

## Output

ให้แสดง output 1 บรรทัดต่อ 1 command

ถ้า register account สำเร็จ ให้แสดงผล:

```text
Registered <acc_no> <name> with balance <balance> Baht.
```

ถ้า deposit สำเร็จ ให้แสดงผล:

```text
Deposited <amount> Baht to <acc_no>. Balance: <balance> Baht.
```

ถ้า withdraw สำเร็จ ให้แสดงผล:

```text
Withdrew <amount> Baht from <acc_no>. Balance: <balance> Baht.
```

ถ้า transfer สำเร็จ ให้แสดงผล:

```text
Transferred <amount> Baht from <from_acc> to <to_acc>.
```

ถ้าไม่พบ account ให้แสดงผล:

```text
Failed: Account <acc_no> not found.
```

ถ้า source account มียอดเงินไม่พอ ให้แสดงผล:

```text
Failed: Insufficient balance in <acc_no>.
```

หลังจากทำครบทุก command ให้แสดงผล:

```text
Final Accounts:
<acc_no> <name>: <balance> Baht
```

จำนวนเงินต้องแสดงทศนิยม 2 ตำแหน่ง
