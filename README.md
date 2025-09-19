# Text Analyzer Python

Este proyecto es una aplicación de escritorio en Python que permite analizar texto ingresado por el usuario. Incluye las siguientes funcionalidades:

- **Contar palabras**: Muestra el número total de palabras en el texto.
- **Frecuencia de términos**: Muestra cuántas veces aparece cada palabra.
- **Detección de palíndromos**: Identifica palabras que son palíndromos.
- **Interfaz gráfica**: Utiliza `tkinter` para mostrar una ventana con fondo negro y texto blanco.

## Uso

1. Ejecuta `main.py`.
2. Ingresa el texto en la ventana superior.
3. Haz clic en "Analyze" para ver los resultados en la ventana inferior.

## Requisitos
- Python 3.x
- Módulos estándar: `tkinter`, `collections`, `re`

## Ejemplo

```
Texto: "Debemos reconocer que el radar detecto anlinina en el oso."
Resultados:
Word count: 10

Term frequency:
  el: 2
  debemos: 1
  reconocer: 1
  que: 1
  radar: 1
  detecto: 1
  anlinina: 1
  en: 1
  oso: 1

Palindromes:
reconocer, oso, radar
```

## Autor
ricaramx77
