# World Cup: The Match Tactics

ในระหว่างการแข่งขันฟุตบอลโลก นักเตะจะต้องใช้พลังกาย (Stamina) ในการทำกิจกรรมต่างๆ 
เราจะจำลองระบบค่าพลังนักเตะในสนาม โดยใช้ความรู้เรื่อง Class และ Inheritance

**คำสั่ง:**
ให้สร้างโครงสร้าง Class ดังนี้:
1. `Player` (Base Class)
   - มี attribute: `name` (ชื่อ), `stamina` (ค่าพลังกาย)
2. `Attacker` (Inherits from `Player`)
   - มี method `shoot()` 
   - ทุกครั้งที่ใช้ จะเช็คว่าถ้า `stamina >= 10` ให้ลด `stamina` ลง 10 แล้วแสดงข้อความ `<name> shoots the ball! Stamina left: <stamina_ที่เหลือ>`
   - แต่ถ้า `stamina < 10` ให้แสดงข้อความ `<name> is too tired to shoot.`
3. `Defender` (Inherits from `Player`)
   - มี method `tackle()`
   - ทุกครั้งที่ใช้ จะเช็คว่าถ้า `stamina >= 15` ให้ลด `stamina` ลง 15 แล้วแสดงข้อความ `<name> tackles! Stamina left: <stamina_ที่เหลือ>`
   - แต่ถ้า `stamina < 15` ให้แสดงข้อความ `<name> is too tired to tackle.`

**ข้อมูลนำเข้า (Input):**
- บรรทัดแรก: จำนวนเต็ม $N$ หมายถึงจำนวนคำสั่ง
- $N$ บรรทัดถัดไป: คำสั่งต่างๆ ซึ่งมี 2 ประเภท
  - `CREATE <Role> <Name> <Stamina>`: สร้างนักเตะ (Role คือ `Attacker` หรือ `Defender`)
  - `ACTION <Name> <Action>`: สั่งให้นักเตะทำงาน (Action คือ `shoot` หรือ `tackle`)

**ข้อมูลส่งออก (Output):**
- แสดงผลลัพธ์ของคำสั่ง `ACTION` ออกมาตามข้อกำหนดของ Class ดังกล่าว (ระบบรับประกันว่าชื่อนักเตะที่ถูกสั่ง ACTION จะถูก CREATE ไว้ก่อนแล้วเสมอ)

**ตัวอย่าง Input 1:**
```text
5
CREATE Attacker Messi 25
CREATE Defender Silva 20
ACTION Messi shoot
ACTION Silva tackle
ACTION Messi shoot
```

**ตัวอย่าง Output 1:**
```text
Messi shoots the ball! Stamina left: 15
Silva tackles! Stamina left: 5
Messi shoots the ball! Stamina left: 5
```
