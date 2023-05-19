# Definindo nossa função
def f(x, y):
    return 3*x**2 + 3*x*y + 2*y**2 + x - y

# Definindo nosso vetor gradiente
def gradiente(x, y):
    return 6*x + 3*y + 1, 3*x + 4*y - 1

# Calculando o ponto de mínimo da nossa função com passo variável usando backtracking line search
def ponto_minimo(passo, x0, y0, precisao, reducao=0.5, max_iter=1000):

    # Valores iniciais
    x = x0
    y = y0

    iteracao = 0

    while iteracao < max_iter:

        # Definindo as componentes do valor gradiente
        grad_x, grad_y = gradiente(x, y)

        # Calculando o valor da função no ponto atual
        f_atual = f(x, y)

        # Inicializando o tamanho do passo
        tamanho_passo = passo

        while True:
            # Calculando os novos valores de x e y com o tamanho do passo
            x1 = x - tamanho_passo * grad_x
            y1 = y - tamanho_passo * grad_y

            # Calculando o valor da função nos novos pontos
            f_novo = f(x1, y1)

            # Verificando a condição de redução do backtracking
            if f_novo <= f_atual - precisao * tamanho_passo * (grad_x**2 + grad_y**2):
                break

            # Reduzindo o tamanho do passo
            tamanho_passo *= reducao

        # Atualizando os valores de x e y
        x = x1
        y = y1

        iteracao += 1

    return (x, y), tamanho_passo, iteracao

ponto_minimo, tamanho_passo, num_iteracoes = ponto_minimo(1, 0, 0, 1e-5)
print("Ponto de mínimo:", ponto_minimo)
print("Passo final:", tamanho_passo)
print("Número de iterações:", num_iteracoes)

