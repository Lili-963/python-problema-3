# Definimos el inventario como una lista de listas
inventario = [
    ["A001", "Teclado Mecánico", 5, 15],
    ["A002", "Mouse ", 15, 13],
    ["A003", "Monitor 24'", 5, 10],
    ["A004", "Auriculares Gamer", 10, 10],
    ["A005", "Cable HDMI 2m", 20, 15]
]
# 3: Aplicación de funciones y procedimientos
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Esta función recibe el stock actual y el mínimo requerido,
    y retorna la cantidad exacta que se debe solicitar.
    """
    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0
        
    return cantidad
# repetición (Ciclo For) y Salida
    print("=== LISTA DE PEDIDOS DE REABASTECIMIENTO ===")
print(f"{'Artículo':<25} | {'Cantidad a Pedir'}")
print("-" * 45)

# Recorremos la matriz fila por fila
for articulo in inventario:
    # Desempaquetamos los datos de la fila
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]
    
    # Llamamos a la función que creamos en el Paso 2
    pedido = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
    
    # Imprimimos solo si es necesario pedir (opcional, pero estético)
    # O imprimimos todo para cumplir con la lista de pedidos.
    print(f"{nombre:<25} | {pedido}")