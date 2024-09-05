def espelhos():
    print("Espelhos esféricos:")
    while True:
        try:
            f = float(input("Qual é o valor do Foco? "))
            if f > 0:
                print("Espelho côncavo")
            elif f == 0:
                print("Espelho Plano")
            elif f < 0:
                print("Espelho Convexo")
            else:
                print("Por favor coloque valores válidos")
                continue
            break
        except ValueError:
            print("Por favor, insira um valor numérico.")

    while True:
        try:
            p = float(input("Qual é a posição? "))
            if p > 0:
                print("Valor válido")
            else:
                print("Por favor coloque um valor válido")
                continue
            break
        except ValueError:
            print("Por favor, insira um valor numérico.")

    while True:
        try:
            y = float(input("Qual é a altura do objeto? "))
            if y > 0:
                print("")
                print("O objeto está para cima")
            elif y == 0:
                print("")
                print("O objeto não existe, coloque valores válidos")
            elif y < 0:
                print("")
                print("O objeto está para baixo")
            break
        except ValueError:
            print("Por favor, insira um valor numérico.")

    if f != p:
        p1 = (f * p) / (p - f)
        if p1 > 0:
            print("Imagem real (fora do espelho)")
        elif p1 < 0:
            print("Imagem virtual (dentro do espelho)")

    if f == p:
        print("Imagem imprópria (imagem não foi formada)")

    a = (f) / p
    if a > 0:
        print("Imagem direita")
    elif a < 0:
        print("Imagem invertida")

    y1 = a * y
    print("")
    print("A imagem tem altura:", y1)
    print("Aumento linear:", a,)
    print("Posição da imagem:", p1,)

espelhos()