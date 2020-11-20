
number = 23
for i in range(2,number/2):
        flag = 0
        if number%i == 0:
            flag = 0
            break
        else:
            flag = 1
        if flag == 1:
            print str(i) + "is prime"
        else:
            print str(i) + "not prime"
        