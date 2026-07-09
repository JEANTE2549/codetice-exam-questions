# Return of Discrete 2

**Difficulty:** Easy

## Problem

จงเขียนโปรแกรมภาษา Python เพื่อคำนวณค่าของ Combination `C(n, r)` และ Permutation `P(n, r)` จากค่านำเข้าที่กำหนด

Combination คือจำนวนวิธีเลือกของ `r` ชิ้นจากทั้งหมด `n` ชิ้น โดยไม่สนใจลำดับ

```text
C(n, r) = n! / (r! * (n - r)!)
```

Permutation คือจำนวนวิธีเรียงของ `r` ชิ้นจากทั้งหมด `n` ชิ้น โดยสนใจลำดับ

```text
P(n, r) = n! / (n - r)!
```

## Input

บรรทัดเดียว: จำนวนเต็ม 2 ค่า `n` และ `r`

กำหนดให้:

- `0 <= n <= 10`
- `0 <= r <= n`

## Output

บรรทัดแรก: ค่าของ Combination `C(n, r)`

บรรทัดที่สอง: ค่าของ Permutation `P(n, r)`
