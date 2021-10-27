ano = int(input('Informe um ano: '))

if ano <= 1964:
    print('Geração: Baby Boomer')
elif ano <= 1979:
    print('Geração: X')
elif ano <= 1994:
    print('Geração:Y')
else:
    print('Geração: Z')
