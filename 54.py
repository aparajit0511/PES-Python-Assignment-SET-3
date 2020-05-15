try:
    print(a)
    raise NameError("NameError")



try:
    inp = input()
    print ('Press Ctrl+C or Interrupt the Kernel:')
except KeyboardInterrupt:
    print ('Caught KeyboardInterrupt')
else:
    print ('No exception occurred')



import sys
try:
7/0
except ArithmeticError as e:
print e
print sys.exc_type
print 'This is an example of catching ArithmeticError'