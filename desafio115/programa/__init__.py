def linha(l=40):
    return '-' * l


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lst):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lst:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    resp = leiaint('\033[32mSua Opção:\033[m ')
    return resp


def leiaint(msg):
    while True:
        try:
            i = int(input(msg))
        except KeyboardInterrupt:
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
