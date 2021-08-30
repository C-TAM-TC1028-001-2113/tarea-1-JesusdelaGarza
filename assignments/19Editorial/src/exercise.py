def main():
    # escribe tu código abajo de esta línea
    from math import ceil
    palabras = int(input('Dame el número de palabras: '))
    costo = (ceil(palabras / 475 ) * 60) * 0.90
    print('El costo de la publicación es:', costo)


if __name__ == '__main__':
    main()
