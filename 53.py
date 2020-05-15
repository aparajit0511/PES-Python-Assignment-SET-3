file = open("test.txt",'r', encoding = 'utf-8')

with open("test.txt",'w',encoding = 'utf-8') as file:
   file.write("my first file\n")

with open("test.txt", "a") as file:
    for i in range(N):
        line = next(file).strip()
        print(line)

file.seek(0)

lines = file.readlines()
for line in lines:
    print line


file.close()