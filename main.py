from random import  choice

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
while True:
        letrasMinusculas = str(input('Deseja letras minusculas ? [S/N]: ').lower().strip())
        letrasMaiusculas = str(input('Deseja letras maiusculas ? [S/N]: ').lower().strip())
        numeros = str(input('Deseja numeros ? [S/N]: ').lower().strip())
        simbolos = str(input('Deseja simbolos ? [S/N]: ').lower().strip())

        alfabetoTemp = list()

        senha = list()

        if letrasMinusculas == 's' and letrasMaiusculas == 's' and numeros == 's' and simbolos == 's':
            for s in range(0, qtdCaracteres):
                senha.append(choice(alfabeto))

        if letrasMinusculas and letrasMaiusculas and numeros and simbolos not in "SsNn" :
            print('\33[31mColoque apenas as opcoes solicitadas!\33[m')
            continue

        elif letrasMinusculas == 's' and letrasMaiusculas == 's' and numeros == 'n' and simbolos == 'n':
            for char in alfabeto:
                if not char.isdigit() and char.isalnum() == True:
                    alfabetoTemp.append(char)
            for s in range(0, qtdCaracteres):
                senha.append(choice(alfabetoTemp))

        elif letrasMinusculas == 'n' and letrasMaiusculas == 's' and numeros == 's' and simbolos == 'n':
            for char in alfabeto:
                if char == char.upper() and char.isalnum() == True:
                    alfabetoTemp.append(char)
            for s in range(0, qtdCaracteres):
                senha.append(choice(alfabetoTemp))


        elif letrasMinusculas == 'n' and letrasMaiusculas == 's' and numeros == 'n' and simbolos == 's':
            for char in alfabeto:
                if char == char.upper() and not char.isdigit():
                    alfabetoTemp.append(char)
            for s in range(0, qtdCaracteres):
                senha.append(choice(alfabetoTemp))


        elif letrasMinusculas == 's' and letrasMaiusculas == 'n' and numeros == 's' and simbolos == 'n':
            for char in alfabeto:
                if char == char.lower() and char.isalnum() == True:
                    alfabetoTemp.append(char)
            for s in range(0, qtdCaracteres):
                senha.append(choice(alfabetoTemp))


        elif letrasMinusculas == 's' and letrasMaiusculas == 'n' and numeros == 'n' and simbolos == 's':
            for char in alfabeto:
                if char == char.lower() and not char.isdigit():
                    alfabetoTemp.append(char)
            for s in range(0, qtdCaracteres):
                senha.append(choice(alfabetoTemp))


        elif letrasMinusculas == 'n' and letrasMaiusculas == 'n' and numeros == 's' and simbolos == 's':
            for char in alfabeto:
                if char == char.lower() and char == char.upper():
                    alfabetoTemp.append(char)
            for s in range(0, qtdCaracteres):
                senha.append(choice(alfabetoTemp))


        elif letrasMinusculas == 'n':
            for char in alfabeto:
                if char == char.upper():
                    alfabetoTemp.append(char)
            for s in range(0, qtdCaracteres):
                senha.append(choice(alfabetoTemp))

        elif letrasMaiusculas == 'n':
            for char in alfabeto:
                if char == char.lower():
                    alfabetoTemp.append(char)
            for s in range(0, qtdCaracteres):
                senha.append(choice(alfabetoTemp))

        elif numeros == 'n':
            for char in alfabeto:
                if not char.isdigit() == True:
                    alfabetoTemp.append(char)
            for s in range(0, qtdCaracteres):
                senha.append(choice(alfabetoTemp))

        elif simbolos == 'n':
            for char in alfabeto:
                if char.isalnum() == True:
                    alfabetoTemp.append(char)
            for s in range(0, qtdCaracteres):
                senha.append(choice(alfabetoTemp))

        print('\n\33[32mSua nova senha é:\33[m ',end='')
        for item in senha:
            print(f'\33[33m{item}',end='')
        break