import random
sim = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
a = int(input("Введите длину пароля:"))
password = ""
for i in range(a):
    y = random.randint(0,len(sim) - 1)
    password += sim[y]
print(password)



