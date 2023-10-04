import random

abcdMin = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p' 'q','r','s','t','u','v','w','x','y','z']
ABCDmaiusc =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numeros = ['1','2','3','4','5','6','7','8','9','0']
simbol = ['!','@','#','$','%','^','*','(',')','_','+','=','/','*','-','+',',','.','/',';','[',']']
senha = list()
while True:
    minCharacter = int(input('Quantos caracteres você deseja na sua senha?(Min 8 caracteres e maxim 14 caracteres): '))
    if minCharacter <= 7 or minCharacter > 14:
        print('\33[31mMínimo 8 caracteres! Maximo 14 caracteres\33[m')
        continue
    else:
        break

print('\nCaso todas as opcoes sejam 1 caracter, sera preenchido com minusculas.\n')

while True:
    qtdLetraMaiuscula = int(input('Quantas letras maiusculas ?(minimo 1 maiuscula, maximo 4): '))
    if qtdLetraMaiuscula <= 0 or qtdLetraMaiuscula  > 4 :
        print('\33[31mMínimo 1 caractere! Maximo 4 caracteres\33[m')
        continue
    else :
        for letra in range(0, qtdLetraMaiuscula):
            senha.append(random.choice(ABCDmaiusc))
        break

while True :
    qtdLetraMinuscula = int(input('\nQuantas letras minusculas (minimo 1 minuscula, maximo 4)?: '))
    if qtdLetraMinuscula <= 0 or qtdLetraMinuscula > 4 :
        print('\33[31mMínimo 1 caractere! Maximo 4 caracteres\33[m')
    else:
        for letra in range (0, qtdLetraMinuscula):
            senha.append(random.choice(abcdMin))
        break

while True:
    qtdNumeros = int(input('\nQuantos numeros ? (minimo 1 numero, maximo 4): '))
    if qtdNumeros <= 0 or qtdNumeros > 4:
        print('\33[31mMínimo 1 caractere! Maximo 4 caracteres\33[m')
        continue
    else :
        for letra in range(0, qtdNumeros):
            senha.append(random.choice(numeros))
        break

while True :
    qtdSimbolos = int(input('\nQuantos simbolos? (minimo 1 simbolo, maximo 2): '))
    if qtdSimbolos <= 0 or qtdSimbolos > 4 :
        print('\33[31mMínimo 1 caractere! Maximo 4 caracteres\33[m')
        continue
    else :
        for letra in range(0, qtdSimbolos):
            senha.append(random.choice(simbol))
        break

random.shuffle(senha)
for l in senha:
    print(f'{l}',end='')