

import sys

for i in range(12) :
    if i >5 :
        for j in range(45) :
            sys.stdout.write("=")
    else :
        for stars in range(8) :
            sys.stdout.write("* ")
        for lines in range(29) :
            sys.stdout.write("=")
    sys.stdout.write('\n')
