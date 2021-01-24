import sys
from datetime import date
import os
usage = """Usage :-\n$ ./todo add \"todo item\"  # Add a new todo\n$ ./todo ls\t\t      # Show remaining todos\n$ ./todo del NUMBER\t      # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help\t      # Show usage\n$ ./todo report\t      # Statistics"""
if(len(sys.argv) < 2):  # check if there is any argument present
    print(usage, end="")

else:
    # todo help
    if(sys.argv[1] == "help"):
        print(usage, end="")

    # todo ls
    if(sys.argv[1] == "ls"):
        if(not(os.path.isfile("todo.txt"))):
            fp = open("todo.txt", "x")
        fp = open("todo.txt")
        lines = fp.readlines()
        if(len(lines) > 0):
            for i in range(len(lines)-1, -1, -1):
                print("["+str(i+1)+"] "+lines[i], end="")
            fp.close()
        else:
            print("There are no pending todos!", end="")

    # todo add "item"
    if(sys.argv[1] == "add"):
        if(len(sys.argv) > 2):
            fp = open("todo.txt", "a")
            fp.write(sys.argv[2])
            fp.write("\n")
            fp.close()
            print("Added todo: \""+sys.argv[2]+"\"", end="")
        else:
            print("Error: Missing todo string. Nothing added!", end="")

    # todo add "item"
    if(sys.argv[1] == "del"):  # todo del NUMBER
        if(len(sys.argv) > 2):
            if(not(os.path.isfile("todo.txt"))):
                fp = open("todo.txt", "x")
            fp = open("todo.txt")
            lines = fp.readlines()
            if(len(lines) > 0):
                if (int(sys.argv[2])-1 < len(lines)) and (int(sys.argv[2]) > 0):
                    l = lines[int(sys.argv[2])-1]
                    fp1 = open("todo.txt", "w")
                    for line in lines:
                        l1 = line.strip("")
                        if l1 != l:
                            fp1.write(line)
                    fp1.close()
                    fp.close()
                    print("Deleted todo #"+sys.argv[2], end="")
                else:
                    print("Error: todo #" +
                          sys.argv[2]+" does not exist. Nothing deleted.", end="")
            else:
                print("error")
        else:
            print("Error: Missing NUMBER for deleting todo.", end="")

    # todo done NUMBER
    if(sys.argv[1] == "done"):
        if(len(sys.argv) > 2):
            if(not(os.path.isfile("todo.txt"))):
                fp = open("todo.txt", "x")
            fp = open("todo.txt")
            lines = fp.readlines()
            if(len(lines) > 0):
                if (int(sys.argv[2])-1 < len(lines)) and (int(sys.argv[2]) > 0):
                    l = lines[int(sys.argv[2])-1]
                    fp1 = open("todo.txt", "w")
                    for line in lines:
                        l1 = line.strip("")
                        if l1 != l:
                            fp1.write(line)
                    fp1.close()
                    fp.close()
                    fp2 = open("done.txt", "a")
                    fp2.write("x ")
                    fp2.write(str(date.today()))
                    fp2.write(" ")
                    fp2.write(l)
                    fp2.close()
                    print("Marked todo #"+sys.argv[2]+" as done.", end="")
                else:
                    print("Error: todo #" +
                          sys.argv[2]+" does not exist.", end="")
            else:
                print("error")
        else:
            print("Error: Missing NUMBER for marking todo as done.", end="")

    # todo report
    if(sys.argv[1] == "report"):
        c = 0
        if(not(os.path.isfile("done.txt"))):
            fp = open("done.txt", "x")
        fp = open("done.txt")
        lines = fp.readlines()
        d = str(date.today())
        if(len(lines) > 0):
            for line in lines:
                l1 = list(line.split(" "))
                if(d == l1[1]):
                    c = c+1
                else:
                    break

        fp1 = open("todo.txt")
        lines = fp1.readlines()
        p = len(lines)
        print(d, "Pending : "+str(p)+" Completed : "+str(c), end="")
