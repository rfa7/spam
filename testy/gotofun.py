a = raw_input("1 or 2")
def print_chocolate():
    print("chocolate")

if a == "1" :
    a = raw_input("3 or 4")
    if a == "3" or a == "4" :
        print_chocolate()

if a == "2" :
    a = raw_input("5 or 6")
    if a == "5" or a == "6":
        print_chocolate()
