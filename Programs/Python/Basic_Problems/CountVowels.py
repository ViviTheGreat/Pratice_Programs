#Calculate Vowels in a string

stat = input("Eenter the string")
vowels = "aeiou"
count = 0
for i in stat:
    if i.lower() in vowels:
        count += 1

print("Vowels conut is " + format(count))


#### Different way in which it also calculate occurrence 
countOcc = {}
for i in stat:
    if i.lower() in vowels:
            if not countOcc.get(i):
                 countOcc[i] = 1
            else:
                 value= countOcc.get(i)
                 value += 1
                 countOcc[i] = value

print(countOcc)
