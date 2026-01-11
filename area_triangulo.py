"""
Descripción: Este programa calcula el área de un triángulo.
Cumple con las reglas de identificadores, tipos de datos y nomenclatura.
"""

# Las funciones deben usar la convención snake_case
def calcular_area_triangulo(base, altura):
    # El identificador representa una variable que almacena el cálculo
    area_final = (base * altura) / 2
    return area_final

# --- Definición de Variables (Tipos de Datos) ---

# Los tipos de datos definen la información que almacena la variable
nombre_figura = "Triángulo"    # Tipo: string
base_triangulo = 12.5          # Tipo: float (decimal)
altura_triangulo = 8           # Tipo: integer (entero)
es_area_grande = False         # Tipo: boolean (lógico)

# Los identificadores deben comenzar con letra o guion bajo
resultado = calcular_area_triangulo(base_triangulo, altura_triangulo)

# Lógica adicional para usar el tipo boolean
if resultado > 30:
    es_area_grande = True

# Salida de resultados
print(f"Figura: {nombre_figura}")
print(f"El área calculada es: {resultado}")
print(f"¿Es un área grande?: {es_area_grande}")