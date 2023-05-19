import numpy as np
import math
def g(x,y):
    g = math.sqrt(x**2+y**2+2)+2*(x**2)*math.exp(-y^2 )+(x-2)^2
    return g
def gradiente_de_g(x, y):
    df_dx = (4*x*math.exp(-y**2) + x*((x**2+y**2+2)**(-0.5)) + 2*(x-2))
    df_dy = (-4*(x**2)*y*math.exp(-y**2) + y*((x**2 + y**2 + 2)**(-0.5)))
    return np.array([df_dx, df_dy])

def grad_descend(x0, y0, alpha):
    x, y = x0, y0
    #conta o numero de iterações para chegar no mínimo
    cont = 0
    while True:
        gradiente = gradiente_de_g(x, y)
        if np.linalg.norm(gradiente) <= 1e-5:
            break
        x -= alpha*gradiente[0]
        y -= alpha*gradiente[1]
        cont += 1
    return (x, y),cont

# primeiro ponto mínimo de g
x1 = -2
y1 = -2

ponto1 , cont1 = grad_descend(x1, y1,0.1)

print("Primeiro ponto mínimo: ({:.5f}, {:.5f}) e o numero de iteções pra chegar no mínimo foi de {}".format(ponto1[0],ponto1[1],cont1))

# Procurando o segundo ponto mínimo da função g
x2 = 2
y2 = 2

ponto2 , cont2 = grad_descend(x2, y2,0.1)

print("Segundo ponto mínimo: ({:.5f}, {:.5f}) e o numero de iteções pra chegar no mínimo foi de {}".format(ponto2[0],ponto2[1],cont2))

# para diferentes passos: 
passo_values = [0.15, 0.2, 0.3, 0.5]
for i in range(len(passo_values)):
    x1, y1 = 2, 2
    ponto1 , cont1 = grad_descend(x1, y1,passo_values[i])

    print("Primeiro ponto mínimo para alpha = {}: ({:.5f}, {:.5f}) e o numero de iteções pra chegar no mínimo foi de {}".format(passo_values[i],ponto1[0],ponto1[1],cont1))


for i in range(len(passo_values)):
    x2, y2 = -2, -2
    ponto2 , cont2 = grad_descend(x2, y2,passo_values[i])

    print("Segundo ponto mínimo para alpha = {}: ({:.5f}, {:.5f}) e o numero de iteções pra chegar no mínimo foi de {}".format(passo_values[i],ponto2[0],ponto2[1],cont2))


