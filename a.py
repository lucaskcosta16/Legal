import random
elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_lengh = int(input('Insira o comprimento da senha'))

password = ''
for i in range(pass_lengh):
    password += random.choice(elements)

print("Sua senha é:", password)
