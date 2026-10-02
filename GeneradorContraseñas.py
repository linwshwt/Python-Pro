import random

caracteres = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Longitud de la contraseña?"))

contra = ""

for i in range(longitud):
    character = random.choice(caracteres)
    contra = contra + caracteres
    

print (contra)