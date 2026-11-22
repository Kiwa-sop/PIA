import re

def contar_frecuencias(palabras, ruta_fichero):
    with open(ruta_fichero, "r", encoding="utf-8") as f:
        texto = f.read().lower()

    texto_limpio = re.sub(r"[^\w\s]", " ", texto)
    palabras_texto = texto_limpio.split()

    palabras_ordenadas = sorted(set(p.lower() for p in palabras))
    frecuencias = {}

    for palabra in palabras_ordenadas:
        frecuencias[palabra] = palabras_texto.count(palabra)

    for palabra, cantidad in frecuencias.items():
        print(f"{palabra}: {cantidad}")

    return frecuencias


palabras_buscar = ["hola", "Mundo", "python", "prueba"]
resultado = contar_frecuencias(palabras_buscar, "texto.txt")
print("Diccionario:", resultado)