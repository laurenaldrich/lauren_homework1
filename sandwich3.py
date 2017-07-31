
def get_input():
    return input("How many sandwiches can you fit in your mouth? ")

def you_lose(count, bro):
    if count <0 :
        return
    if count <= 4:
        print "You said, ", count, "but my brother can eat ", bro
    else:
        print "You will get sick if you eat", count, "sandwiches!"


count = 0 
while count >= 0 :
    count = get_input()
    you_lose(count, count+1)

print "You should really try harder. Even a baby can eat zero sandwiches!"
