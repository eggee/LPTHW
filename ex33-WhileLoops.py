
numbers = []

def while_loop_function(i, y):
    while i < y:
        print "At the top i is", i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

while_loop_function(0, 5)

for num in numbers:
    print num