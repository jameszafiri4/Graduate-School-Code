import sys

print("The name of your program is " + sys.argv[0])
print("The number of command line arguements is ", len(sys.argv)-1)
argcount = len(sys.argv)-1

while (argcount >= 1):
    print("The " + str(argcount) + "st arg is " + sys.argv[argcount])
    argcount -= 1
