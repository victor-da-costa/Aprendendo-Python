numeros = (int(input("Informe o 1° número: ")), int(input("Informe o 2° número: ")), 
int(input("Informe o 3° número: ")), int(input("Informe o 4° número: ")))


print(f"O número 9 apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O número 3 aparece na posição {numeros.index(3)} da lista")
else:
    print("O numero 3 não foi inserido na lista")
for num in numeros:
    if num % 2 == 0:
        print(num, end='')