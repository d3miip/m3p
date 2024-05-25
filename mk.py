import random
contra = ""
carc = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
num = int(input("Ingrese un número:"))
for i in range(num):
    contra += random.choice(carc)
print(contra)
