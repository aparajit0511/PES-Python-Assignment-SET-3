f = open("test.txt",'r', encoding = 'utf-8')

with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
   f.write("gibberish\n")
   f.write("bye")

with open("test.txt",'a+',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
   f.write("gibberish\n")
   f.write("bye")

f.close()