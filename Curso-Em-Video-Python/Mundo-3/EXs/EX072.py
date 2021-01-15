numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 
'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input("Escolha um número entre 0-20: "))
    if num >= 0 and num <= 20:
        break
    print("Tente novamente")
print(f"O númeoro {num} escrito por extenso: {numeros[num]}")
