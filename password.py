import random
import os

letras_mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
numeros = "1234567890"
simbolos = ",./<>?;':[]{}-=_+()*&^%$#@!"
password = []
count = 0
case = 0
cantidad_digitos = int(input("Longitud deseada: "))
s_mayus = input("Mayusculas(s/n): ")
s_minus = input("Minusculas(s/n): ")
s_num = input("Numeros(s/n): ")
s_simbolos = input("Simbolos(s/n): ")
segura = False


while count != cantidad_digitos:
    case = random.randint(1, 4)
    if case == 1 and s_mayus.lower() == "s":
        password.append(letras_mayusculas[random.randint(0, 25)])
        count += 1

        if cantidad_digitos == count:
            break
    elif case == 2 and s_minus.lower() == "s":
        password.append(letras_minusculas[random.randint(0, 25)])
        count += 1
        if cantidad_digitos == count:
            break
    elif case == 3 and s_num.lower() == "s":

        password.append(numeros[random.randint(0, 9)])
        count += 1
        if cantidad_digitos == count:
            break
    elif case == 4 and s_simbolos.lower() == "s":
        password.append(random.choice(simbolos))
        count += 1
        if cantidad_digitos == count:
            break
os.system("cls")
password = "".join(password)
print("Su contraseña es:", password)
if len(password) < 8:
    print("su contraseña no es segura")
elif s_mayus != "s" or s_minus != "s" or s_num != "s" or s_simbolos != "s":
    print("su contraseña no es segura")
    print("Deberia de tener caracteres de todos los tipos")
else:
    print("su contraseña es segura")
    print("mientras mas larga sea la contraseña menos comprometida sera tu informacion")
save = open("password.txt", "a")
save.write(password + "\n")
save.close()
