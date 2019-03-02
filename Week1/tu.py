

cau = " 'Hello, I am Lien"

cau = cau.split()

print(cau) # tách các từ trong câu bằng khoảng trắng , lưu vào mảng


for i in range(0,len(cau)):
    cau[i] = cau[i].lower()


print(cau)