def do_stuff(command):
    eval(command)


if __name__ == "__main__":
    user_input = input()
    do_stuff(user_input)
