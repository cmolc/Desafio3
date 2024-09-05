import math
import sympy as sp

# Definir valores
x0 = math.pi / 4
x1 = math.pi / 3
h = x1 - x0
tolerancia = 0.0005

# Definir variable simbólica
x = sp.Symbol('x')


# Definir la función f(x) = cos(x)
def f(x):
    return sp.cos(x)


# Función para calcular la expansión en serie de Taylor
def taylor_expansion(f, x0, h, tolerancia):
    # Inicialización de la serie con f(x0)
    series = f.subs(x, x0)
    ef = float('inf')  # Inicializamos el error con un valor grande
    i = 1

    print('f(x) = cos(x)')
    print('X0 =', x0, '≈ pi/4')
    print('cos(X0) =', series)
    print('X1 =', x1, '≈ pi/3')
    print('cos(X1) =', f.subs(x, x1))
    print('H =', h)
    print('-----------------------------------------------------')

    # Iteramos hasta que el error sea menor que la tolerancia
    while ef > tolerancia:
        deriv_i = f.diff(x, i)  # Derivada i-ésima
        deriv_i_val = deriv_i.subs(x, x0)  # Valor de la derivada evaluada en x0
        term = (deriv_i_val / math.factorial(i)) * h ** i  # Término de la serie

        # Actualizamos la serie de Taylor con el término actual
        series += term

        print(f"Iteración {i}: {series}")
        print(f"Derivada {i} = {deriv_i}, valor = {deriv_i_val}")

        # Calculamos el error estimado
        ef = abs(term)
        print(f"Error estimado en iteración {i}: {ef}")
        print('-----------------------------------------------------')

        # Incrementamos el contador de iteraciones
        i += 1

    return series


# Llamamos a la función para calcular la expansión de Taylor

if __name__ == '__main__':
    expansion = taylor_expansion(f(x), x0, h, tolerancia)
    print(f"\nAproximación de Taylor en x = {x1} es: {expansion}")