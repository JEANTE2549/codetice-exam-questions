# Locker Log Analyzer

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อวิเคราะห์ rental log ของ locker และแสดง status ล่าสุดของ locker ทุกตู้ที่เคยปรากฏในข้อมูล

แต่ละ log record ประกอบด้วย:

- locker id
- member name
- action: `RENT` หรือ `RETURN`

กติกา:

- `RENT` หมายถึง locker ถูกเช่าโดย member คนนั้น
- `RETURN` หมายถึง locker ถูกคืนและ available
- final report ต้องแสดง locker ทุกตู้ที่เคยปรากฏอย่างน้อย 1 ครั้ง

## Input

บรรทัดแรกเป็นจำนวนเต็ม `N` แทนจำนวน log record

อีก `N` บรรทัดถัดมาเป็น log record ในรูปแบบ:

```text
<locker_id>,<member_name>,<action>
```

## Output

แสดงผล 1 บรรทัดต่อ 1 locker โดยเรียงตาม locker id:

```text
<locker_id>: Occupied (<member_name>)
```

หรือ

```text
<locker_id>: Available (None)
```

## Note

- โจทย์ข้อนี้ไม่ต้องอ่านหรือเขียนไฟล์
- ให้เรียง locker id แบบข้อความ
