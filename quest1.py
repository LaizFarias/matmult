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

    while True:

        # Definindo as componentes do valor gradiente
        grad_x, grad_y = gradiente(x, y)

        # Fórmula dada no enunciado
        x1 = x - passo * grad_x
        y1 = y - passo * grad_y

        # SE a o valor da função no ponto atual menos o ponto anterior for menor que a precisão definida, encontramos o nosso ponto de mínimo
        if abs(f(x1, y1) - f(x, y)) < precisao:
            break

        # SENÃO, atualizamos os valores de x e y para os valores calculados acima
        x = x1
        y = y1

    return x, y

ponto_minimo = ponto_minimo(0.1, 0, 0, 1e-5)
print("Ponto de mínimo:", ponto_minimo)