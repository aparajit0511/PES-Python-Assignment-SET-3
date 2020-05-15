N = 10
with open("test.txt", "a") as file:
    for i in range(N):
        line = next(file).strip()
        print(line)


file.seek(100)

lines = file.readlines()
for line in range(5,len(lines)):
    print lines[line]