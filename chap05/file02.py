def fopen1(filename):
    file = open(filename, "w")
    file.write("Hello Python Programming...")
    file.close()

def fopen2(filename):
    with open(filename, "w") as f:
        f.write("Hello Python Programming...!")

# read
def f_read(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents

c = f_read("basic3.txt")
print(c)

