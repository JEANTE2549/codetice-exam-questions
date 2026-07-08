# Word Frequency Grouper

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อ analyze text 1 บรรทัด

โปรแกรมต้องทำงานดังนี้:

1. แปลง text ทั้งหมดเป็น lowercase
2. ลบ period (`.`) ออกจาก text
3. นับ frequency ของแต่ละ word
4. group unique word ตาม word length

ตอนแสดง word frequency และตอนแสดง word ในแต่ละ length group ให้เรียง word ตามลำดับที่ word นั้นปรากฏครั้งแรกใน text

## Input

input มี 1 บรรทัด:

1. text ที่ต้องการ analyze

## Output

ให้แสดง word frequency report ก่อน:

```text
Word Frequencies:
<word>: <count>
```

จากนั้นแสดง length group report:

```text
Grouped By Length:
<length>: <word1>, <word2>, ...
```

length group ต้องเรียงจากความยาวน้อยไปมาก

## Note

- ลบเฉพาะ period (`.`) เท่านั้น
- หลังจาก clean text แล้ว ให้ถือว่า word ถูกคั่นด้วยช่องว่าง
