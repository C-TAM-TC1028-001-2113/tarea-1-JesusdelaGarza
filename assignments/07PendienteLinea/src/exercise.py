def main():
    # escribe tu código abajo de esta línea
    x1 = float(input('Dame el x1: '))
    y1 = float(input('Dame el y1: '))
    x2 = float(input('Dame el x2: '))
    y2 = float(input('Dame el y2: '))
    n = (y2 - y1) / (x2 - x1)
    print('Pendiente:', n)


if __name__ == '__main__':
    main()
