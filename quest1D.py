# Definindo nossa função
def f(x, y):
    return 3*x**2 + 3*x*y + 2*y**2 + x - y

# Definindo nosso vetor gradiente
def gradiente(x, y):
    return 6*x + 3*y + 1, 3*x + 4*y - 1

# Calculando o ponto de mínimo da nossa função
def ponto_minimo(passo, x0, y0, precisao):

    # Valores iniciais
    x = x0
    y = y0
    contador = 0
    menorX = [0]
    menorY = [0]
    while True:

        # Definindo as componentes do valor gradiente
        grad_x, grad_y = gradiente(x, y)

        # Fórmula dada no enunciado
        x1 = x - passo * grad_x
        y1 = y - passo * grad_y

        # SE a o valor da função no ponto atual menos o ponto anterior for menor que a precisão definida, encontramos o nosso ponto de mínimo
        if abs(f(x1, y1) - f(x, y)) < precisao or contador > 200:
            break

        # SENÃO, atualizamos os valores de x e y para os valores calculados acima
        x = x1
        y = y1
        contador += 1

        # Analisamos o valor da função no ponto atual e no ponto de mínimo anterior e atualizamos o ponto de mínimo caso necessário
        if f(x1, y1) < f(menorX[0], menorY[0]):
            menorX[0] = x1
            menorY[0] = y1
    
    print(f"Valor da função no ponto de mínimo com passo {passo} :", f(menorX[0], menorY[0]))

    # Retornamos o ponto de mínimo
    return menorX[0], menorY[0]


# COLOQUE O PASSO DESEJADO NA ENTRADA DA FUNÇÃO
ponto_minimo_03 = ponto_minimo(0.3, 0, 0, 1e-5)
print("Ponto de mínimo com passo 0.3:", ponto_minimo_03)
ponto_minimo_05 = ponto_minimo(0.5, 0, 0, 1e-5)
print("Ponto de mínimo com passo 0.5:", ponto_minimo_05)

