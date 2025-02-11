estado = 0

entradaStr = input('Identificador para validar: ')

for character in entradaStr:
    print('PRE:', character, '-Estado:', estado, '-Es Alpha:', character.isalpha(), '-Es dígito', character.isdigit())
    if estado == 0:
        if character.isalpha():
            estado = 1
        else:
            estado = 2
    elif estado == 1:
        if not (character.isalpha() or character.isdigit()):
            estado = 2
    else:
        estado = 2
    print('POST:', estado, '\n')

if estado == 1:
    print('La secuencia', entradaStr, 'es un identificador válido')
else:
    print('La secuencia', entradaStr, 'no es un identificador válido')