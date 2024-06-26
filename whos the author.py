# น้องเจด เป็นคนที่ชอบอ่านหนังสือมากกกก แต่ไม่เคยจำได้เลยว่าผู้เขียนแต่ละคน มีผลงานชิ้นใดบ้าง พี่จึงอยากให้น้องๆสร้างโปรแกรมที่บันทึกชื่อหนังสือของผู้เขียนแต่ละคนให้น้องเจด หน่อย

# Jade
# โดยโปรแกรมจะรับค่าเป็น ชื่อผู้เขียน ชื่อหนังสือ (ใช้ช่องว่าง " " ระหว่างชื่อและหนังสือ) เรื่อยๆ จนกว่าจะเจอคำว่า ENDจากนั้นทำการบันทึกและแสดงผลให้หน่อยว่า ผู้เขียนคนนั้นๆ เขียนหนังสือชื่ออะไรบ้าง

# ปล. ในคลังหนังสือของผู้เขียน ห้ามมีหนังสือที่ชื่อซ้ำกันนะครับ

# โดยแสดงผลเป็น
# ชื่อผู้เขียน: หนังสือ1, หนังสือ2, ...., หนังสือเล่มสุดท้าย
# หากไม่มีข้อมูลเลย ให้แสดงผล
# No Information

# Input Specification
# n บรรทัด:
# บรรทัด 1: รับค่าเป็นข้อความ 2 ข้อความโดยคั่นด้วยช่องว่าง
# บรรทัด 2: รับค่าเป็นข้อความ 2 ข้อความโดยคั่นด้วยช่องว่าง
# บรรทัด 3: รับค่าเป็นข้อความ 2 ข้อความโดยคั่นด้วยช่องว่าง
# .
# .
# .
# บรรทัดสุดท้าย(n): END

# Output Specification
# บรรทัดตามจำนวนผู้เขียน หรือ 1 บรรทัด:
# บรรทัดที่ 1: ชื่อผู้เขียน1: [หนังสือ1, หนังสือ2, ..., หนังสือเล่มสุดท้าย]
# บรรทัดที่ 2: ชื่อผู้เขียน2: [หนังสือ1, หนังสือ2, ..., หนังสือเล่มสุดท้าย]
# .
# .
# .
# บรรทัดที่ n: ชื่อผู้เขียนคนสุดท้าย: [หนังสือ1, หนังสือ2, ..., หนังสือเล่มสุดท้าย]

# ถ้าหากไม่มีข้อมูล ให้แสดงผล: No Information

# Input
# In book1
# In book2
# In book3
# In book3
# In book3
# In book2
# END

# Expected Output
# In: ['book1', 'book2', 'book3']


# Input
# Prepro 66
# Prepro 67
# IT KMITL
# IT PSCP
# Prepro Prepro
# END

# Expected Output
# Prepro: ['66', '67', 'Prepro']
# IT: ['KMITL', 'PSCP']


# Input
# END

# Expected Output
# No Information
