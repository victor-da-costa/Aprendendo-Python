from time import sleep


def contador(início, fim, passo):
    if passo < 0:
        passo * (-1)
    if passo == 0:
        passo = 1

    if início < fim:
        cont = início
        while cont <= fim:
            print(f' {cont}', end='', flush=True)
            sleep(0.5)
            cont += passo
        print()
    else:
        cont = início
        while cont >= fim:
            print(f' {cont}', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print()


início = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(1, 10, 1)
contador(10, 0, 2)
contador(início, fim, passo)
