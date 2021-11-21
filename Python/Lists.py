lst = []
run = True

def parse(cmd):
    cmd = cmd.split()
    
    if cmd[0].isdigit():
        pass
    elif cmd[0] == "insert":
        lst.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == "append":
        lst.append(int(cmd[1]))
    elif cmd[0] == "remove":
        lst.remove(int(cmd[1]))
    elif cmd[0] == "sort":
        lst.sort()
    elif cmd[0] == "reverse":
        lst.reverse()
    elif cmd[0] == "pop":
        lst.pop()
    elif cmd[0] == "print":
        print(lst)

while run:
    try:
        parse(input())
    except:
        run = False