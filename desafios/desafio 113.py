def leiaint(msg):
    while True:
        try:
            i = int(input(msg))
        except (KeyboardInterrupt):
            print('\033[0;31m Usuário preferiu não digitar esse número.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31m ERRO! Tivemos um probleam com os tipos de dados que voce digitou.\033[m')
        except:
            print('\033[0;31m ERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            break
    return i


def leiaReal(msg):
    while True:
        try:
            r = float(input(msg))
        except KeyboardInterrupt:
            print('\033[0;31m Usuário preferiu não digitar esse número.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31m Tivemos um probleam com os tipos de dados que voce digitou.\033[m')
        except:
            print('\033[0;31m ERRO! Digite um número real válido.\033[m')
            continue
        else:
            break
    return r


i = leiaInt('Digite um número Inteiro: ')
r = leiaReal('Digite um número Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
