def maior(*num):
    mai = 0
    for numero in num:
        print(f' {numero}', end='', flush=True)
        if num[0] == 0:
            mai = numero
        else:
            if numero > mai:
                mai = numero

    print(f'\n >> O maior número é {mai} <<')


maior(5, 8, 3, 12, 68, 2, 0, 78)