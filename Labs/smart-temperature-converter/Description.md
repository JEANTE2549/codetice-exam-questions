# Smart Temperature Converter

## Problem

ให้เขียนโปรแกรมภาษา Python เพื่อ convert ค่า temperature 1 ค่า จาก unit หนึ่งไปเป็นอีก unit หนึ่ง

Unit ที่รองรับมีดังนี้:

- `C` คือ Celsius
- `F` คือ Fahrenheit
- `K` คือ Kelvin

โปรแกรมต้องตรวจสอบด้วยว่า input temperature อยู่ในระดับ danger หรือไม่ โดยให้นำ input temperature ไปคิดเป็น unit Celsius ก่อน ถ้ามีค่ามากกว่า `100` ให้ถือว่าเป็น high temperature

## Input

input มีทั้งหมด 3 บรรทัด:

1. temperature value เป็นจำนวนทศนิยม
2. source unit: `C`, `F` หรือ `K`
3. target unit: `C`, `F` หรือ `K`

## Output

แสดงผลทั้งหมด 2 บรรทัด:

```text
Converted: <converted_value> <target_unit>
Status: <status>
```

converted value ต้องแสดงทศนิยม 2 ตำแหน่ง

ค่า status เป็นดังนี้:

- `Danger: High Temperature!` ถ้าค่า Celsius มากกว่า `100`
- `Normal` ในกรณีอื่น

## Note

- Fahrenheit เป็น Celsius: `(F - 32) * 5 / 9`
- Celsius เป็น Fahrenheit: `(C * 9 / 5) + 32`
- Celsius เป็น Kelvin: `C + 273.15`
- Kelvin เป็น Celsius: `K - 273.15`
