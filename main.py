while True:
    print('Entre com um número:')
    numberStr = input()
    numberStr_without_comma = numberStr.replace(',', '')

    if not numberStr_without_comma.isnumeric():
       print('Número inválido')
       continue

    number = float(numberStr.replace(',', '.'))

    if number == 1 or number == 10:
        print(number)
        break
    #expoente positivo
    if number > 1:
        notation = f'{numberStr_without_comma[0]},{numberStr_without_comma[1:]}x10^{len(numberStr_without_comma[1:])}'
        print(notation)
        break
    
    #expoente negativo
    elif number < 1 and number > 0:
        for i in range(0, len(numberStr_without_comma)):
            current_num = int(numberStr_without_comma[i])
            if current_num > 0:
                notation = f'{current_num},{numberStr_without_comma[i + 1:] if len(numberStr_without_comma) > (i + 1) else 0}x10^-{len(numberStr_without_comma[:i])}'
                print(notation)
                break
        break
    else:
        print('Número inválido')
        continue
        
