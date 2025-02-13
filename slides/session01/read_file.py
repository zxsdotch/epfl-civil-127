with open("poem.txt") as lines:
    for line in lines:
        print("> {}".format(line.rstrip("\r\n")))
