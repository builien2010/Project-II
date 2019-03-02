from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp,'lxml')

print(soup.text)

print(soup.text.split())

# Mở file
file = open("plc.txt", "wt")
file.write(soup.text)

# Đóng file
file.close()

