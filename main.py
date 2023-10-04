import random

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            '1','2','3','4','5','6','7','8','9','0',
            '!','@','#','$','%','^','*','(',')','_','+','=','/','*','-','+',',','.','/',';','[',']']
alfabetoTemp = list()
senha = list()

print('\33[32m------Bem vindo ao programa de geracao de senhas aleatorias!-------\33[m')

while True:
    try:
        qtdCaracteres = int(input('\nQuandos caracteres deseja?: '))

        if qtdCaracteres <= 7 :
            print('\33[31mQuantidade minima de caracteres é 8!\33[m')
            continue
        elif qtdCaracteres > 14:
            print('\33[31mQuantidade maxima de caracteres é 14!\33[m')
            continue
        else:
            break
    except:
        print('\33[31mApenas numeros, por favor!\33[m')

letrasMaiusculas = str(input('Deseja letras maiusculas ?: [S/N]').upper().strip())
letrasMinusculas = str(input('Deseja letras minusculas ?: [S/N]').upper().strip())
numeros = str(input('Deseja numeros ?: [S/N]').upper().strip())
simbolos = str(input('Deseja simbolos ?: [S/N]').upper().strip())

if letrasMinusculas == 'S' and letrasMaiusculas == 'S' and numeros == 'S' and simbolos == 'S':
    for l in range(0, qtdCaracteres):
        senha.append(random.choice(alfabeto))

elif letrasMinusculas == 'N':
    for l in alfabeto:
        if l == l.upper():
            alfabetoTemp.append(l)
    for l in range(0, qtdCaracteres):
        senha.append(random.choice(alfabetoTemp))

elif letrasMaiusculas == 'N':
    for l in alfabeto:
        if l == l.lower():
            alfabetoTemp.append(l)
    for l in range(0, qtdCaracteres):
        senha.append(random.choice(alfabetoTemp))

elif numeros == 'N':
    alfabetoTemp = ''.join(l for l in alfabeto if not l.isdigit())
    for l in range(0, qtdCaracteres):
        senha.append(random.choice(alfabetoTemp))

elif simbolos == 'N':
    alfabetoTemp = ''.join(l for l in alfabeto if l.isalnum())
    for l in range(0, qtdCaracteres):
        senha.append(random.choice(alfabetoTemp))
print('Sua nova senha é: ',end='')
for item in senha:
    print(f'{item}',end='')