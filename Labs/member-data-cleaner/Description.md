# Member Data Cleaner

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อตรวจสอบ member data และแยก valid member ออกจาก invalid member

member จะถือว่า valid เมื่อผ่านเงื่อนไขทั้ง 2 ข้อนี้:

1. email ต้องมี `@` และลงท้ายด้วย `.com`, `.co.th` หรือ `.ac.th`
2. age เป็นจำนวนเต็มตั้งแต่ `18` ถึง `60`

## Input

บรรทัดแรกเป็นจำนวนเต็ม `N` แทนจำนวน member

member แต่ละคนใช้ข้อมูล 3 บรรทัด:

1. ชื่อ
2. email
3. age

## Output

ให้แสดง valid member ก่อน:

```text
Valid Members:
<name> (<email>, <age>)
```

ถ้าไม่มี valid member ให้แสดง `None` ใต้บรรทัด `Valid Members:`

จากนั้นแสดง error list:

```text
Errors:
Row for <name>: <reason>
```

ถ้าไม่มี error ให้แสดง `None` ใต้บรรทัด `Errors:`

สุดท้ายให้แสดงผลสรุป:

```text
Summary: <valid_count> valid, <invalid_count> invalid
```

## Note

- ถ้า email ไม่ถูกต้อง ให้ใช้เหตุผล `Invalid email`
- ถ้า age ไม่ใช่จำนวนเต็ม ให้ใช้เหตุผล `Age '<age>' is not a valid integer`
- ถ้า age อยู่นอกช่วงที่กำหนด ให้ใช้เหตุผล `Age <age> is out of valid range (18-60)`
- โจทย์ข้อนี้ไม่ต้องอ่านหรือเขียนไฟล์
