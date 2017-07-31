
def get_input():
    return input("How many sandwiches can you fit in your mouth? ")

def you_lose(count, bro):
    if count <= 4:
        print "You said, ", count, "but my brother can eat ", bro
    else:
        print "You will get sick if you eat", count, "sandwiches!"
    print "Therefore, you lost!!! :("

count = get_input()
my_brother = count + 1
you_lose(count, my_brother)



