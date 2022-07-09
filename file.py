

def write_file():
    fd = open("1.txt","a+")
    fd.write("hah jaja\n")
    fd.flush()
    fd.close()

def read_file():
    with open("1.txt","r") as fds:
        for fd in fds:
            print("readed:",fd)
# write_file()
read_file()