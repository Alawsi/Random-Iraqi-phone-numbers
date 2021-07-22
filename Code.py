#The script can be used for marketing in Iraq
#This script can be used for beginners in Python
#This script was created by : github.com/Alawsi
#t.me/awsi5
import random

t = '0123'
t2 = '78','77'

print("""
1 - Zain
2 - Asiacell
3 - Zain & Asiacell
""")
provider = int(input('Provider : '))
count = int(input('Enter The count : '))
choose = int(input("1 - Save to a file\n2 - Print here\n1 or 2 ? "))
if choose == 1:
    name = input('Choose the name of the text file : ')
    if provider == 1:
        for i in range(count):
            num = random.randint(1000000,9999999)
            tr = random.choice(t)
            with open(f'{name}.txt', 'a') as save:
                save.write(f'+964{t2[0]}{tr}{num}\n')
                save.close()
        input('Done , Press Enter to exit ..')
    elif provider == 2:
        for i in range(count):
            num = random.randint(1000000,9999999)
            tr = random.choice(t)
            with open(f'{name}.txt', 'a') as save:
                save.write(f'+964{t2[1]}{tr}{num}\n')
                save.close()
        input('Done , Press Enter to exit ..')
    else:
        for i in range(count):
            num = random.randint(1000000, 9999999)
            tr = random.choice(t)
            t2r = random.choice(t2)
            with open(f'{name}.txt', 'a') as save:
                save.write(f'+964{t2r}{tr}{num}\n')
                save.close()
        input('Done , Press Enter to exit ..')
elif choose == 2:
    if provider == 1:
        for i in range(count):
            num = random.randint(1000000, 9999999)
            tr = random.choice(t)
            print(f'+964{t2[0]}{tr}{num}')
    elif provider == 2:
        for i in range(count):
            num = random.randint(1000000, 9999999)
            tr = random.choice(t)
            print(f'+964{t2[1]}{tr}{num}')
    else:
        for i in range(count):
            num = random.randint(1000000, 9999999)
            tr = random.choice(t)
            t2r = random.choice(t2)
            print(f'+964{t2r}{tr}{num}')
