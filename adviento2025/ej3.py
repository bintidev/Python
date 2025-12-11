
def draw_gift(size, symbol):
    regalo = ''

    if (size >= 2):
        espacios = size - 2
        mitad = (size // 2) + 1
        # primera liena
        regalo += f'{symbol * size}\n'

        if (size > 2):
            for i in range(mitad - 1):
                regalo += (symbol + ' ' * espacios) * size + '\n'
            # ultima linea

        regalo += f'{symbol * size}'
        
    return regalo

print(draw_gift(5,'*'))