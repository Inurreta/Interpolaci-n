'''
Nadie responde la pregunta? El editor en jefe creó un grupo QQ de aprendizaje y comunicación de Python: 579817333 
 Buscando amigos con ideas afines para ayudarse entre sí, ¡también hay buenos tutoriales de aprendizaje en video y libros electrónicos en PDF en el grupo!
'''
import matplotlib.pyplot as plt
import math

from numpy import array


# ================================================= == interpolación lagrange ================================================== ===================
def lagrange(x_, y, a):
    """
         Obtenga la interpolación de Lagrange
         : param x_: valor de lista de x
         : param y: valor de lista de y
         : param a: número a interpolar
         : return: devuelve el resultado de la interpolación
    """
    ans = 0.0
    for i in range(len(y)):
        t_ = y[i]
        for j in range(len(y)):
            if i != j:
                t_ *= (a - x_[j]) / (x_[i] - x_[j])
        ans += t_
    return ans


# ================================================= == interpolación newton ================================================== ===================
def table(x_, y):
    """
         Obtener la tabla de interpolación de Newton
         : param x_: valor de la lista x
         : param y: valor de la lista y
         : return: vuelve a la tabla de interpolación
    """
    quotient = [[0] * len(x_) for _ in range(len(x_))]
    for n_ in range(len(x_)):
        quotient[n_][0] = y[n_]
    for i in range(1, len(x_)):
        for j in range(i, len(x_)):
            # j-i determina los elementos diagonales
            quotient[j][i] = (quotient[j][i - 1] - quotient[j - 1][i - 1]) / (x_[j] - x_[j - i])
    return quotient


def get_corner(result):
    """
         Obtenga elementos diagonales a través de la tabla de interpolación
         : resultado del parámetro: resultado de la tabla de interpolación
         : return: elemento diagonal
    """
    link = []
    for i in range(len(result)):
        link.append(result[i][i])
    return link


def newton(data_set, x_p, x_7):
    """
         Resultados de la interpolación de Newton
         : param data_set: diagonal del problema resuelto
         : param x_p: valor de entrada
         : param x_7: el valor de lista original de x
         : return: resultado de la interpolación de Newton
    """
    result = data_set[0]
    for i in range(1, len(data_set)):
        p = data_set[i]
        for j in range(i):
            p *= (x_p - x_7[j])
        result += p
    return result


# ================================================= ============= Dibujo de imágenes ==================================== =================
def draw_picture(x_list, y_list, node):
    plt.title("newton")
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.plot(x_list, y_list, color="red")
    for i in range(len(x_list)):
        plt.scatter(x_list[i], y_list[i], color="purple", linewidths=2)
    plt.scatter(node[0], node[1], color="blue", linewidth=2)
    plt.show()
    

if __name__ == '__main__':
    x =  float(input("ingrese valor de x"))
    temp1 = input("ingrese los valores de x1 uno por uno separados por espacios: ")
    x_1=list(map(float,temp1.split(' ')))
    #print(temp1a)
    temp2 = input("ingrese los valores de y1 uno por uno separados por espacios: ")
    y_1=list(map(float,temp2.split(' ')))
    
    """
    x_1 = [0.4, 0.5, 0.6, 0.7, 0.8] 0.4 0.5 0.6 0.7 0.8
    y_1 = [-0.9163, -0.6931, -0.5108, -0.3567, -0.2231] -0.9163 -0.6931 -0.5108 -0.3567 -0.2231
    """
    middle = table(x_1, y_1)
    n = get_corner(middle)
    newton = newton(n, x, x_1)
    lagrange = lagrange(x_1, y_1, 0.54)
    print("Verdadero valor: {}".format(math.log(0.54, math.e)))
    print("Interpolación de Lagrange: {}".format(lagrange))
    print("Interpolación de Newton: {}".format(newton))
    # Dibujar
    draw_picture(x_1, y_1, (x, newton))