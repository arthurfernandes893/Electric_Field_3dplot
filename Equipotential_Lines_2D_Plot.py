import numpy as np
import matplotlib.pyplot as plt

# Constantes
k = 9*(10^9)
Q = 2*(10^(-6))
q1 = 5*Q
q2 = Q 

def potential(x, y):
    r1 = np.sqrt((x-10)**2 + y**2)
    r2 = np.sqrt((x+10)**2 + y**2)
    return k*((q1/r1)+(q2/r2))

# Espaço Vetorial definido
x_min, x_max, y_min, y_max = -30, 30, -30, 30
num_points = 100

# Criacao do espaço vetorial
x = np.linspace(x_min, x_max, num_points)
y = np.linspace(y_min, y_max, num_points)
X, Y = np.meshgrid(x, y)

# Calculo do potencial para cada ponto do espaco vetorial
Z = potential(X, Y)

#definicao da lista de cores
c = ('#ff0000', '#ffff00', '#0000FF', '0.6', 'c', 'm')

#criacao do grafico com 1000 niveis e configuracoes de cor "c"
grafico = plt.contour(X, Y, Z, 1000 , colors=c)

#plot 
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.title('Linhas Equipotenciais para uma carga Q e outra 5Q, ambas a 10cm da origem')
plt.show()
