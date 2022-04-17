def calc(data):
    import utime
    mmExit = False
    while not mmExit:
        inp = input("Operation(+,-,*,/): ")
        if inp == "+":
            inp = int(input("Num 1: "))
            inp2 = int(input("Num 2: "))
            print(inp + inp2)

        if inp == "-":
            inp = int(input("Num 1: "))
            inp2 = int(input("Num 2: "))
            print(inp - inp2)

        if inp == "*":
            inp = int(input("Num 1: "))
            inp2 = int(input("Num 2: "))
            print(inp * inp2)

        if inp == "/":
            inp = int(input("Num 1: "))
            inp2 = int(input("Num 2: "))
            print(inp / inp2)

        if inp == "exit":
            mmExit = True
        utime.sleep(1)
    return 0


def mpyterm(data):
    import uos
    print("""
    MicroPython Terminal For MicroPyOs
    V1.0.0 
    """)
    mmExit = False
    while not mmExit:
        cmd = input(uos.getcwd() + "> ")
        if cmd == "exit" or cmd == "exit()":
            mmExit = True
        else:
            try:
                exec(cmd)
            except Exception as e:
                print(e)
    return 0

