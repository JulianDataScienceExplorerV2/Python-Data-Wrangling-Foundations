# Python Data Foundations / Fundamentos de Python para Datos

Core Python patterns applied to data analysis scenarios: data structures, aggregation, filtering, and list comprehensions.

Patrones fundamentales de Python aplicados a analisis de datos: estructuras de datos, agregacion, filtrado y comprensiones de listas.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![Focus](https://img.shields.io/badge/Focus-Data%20Wrangling-informational?style=flat-square)

---

## Contents / Contenido

### `list_and_dicts.py` — Data Structures for Analysis / Estructuras de Datos

Practical use of lists and dictionaries to represent, traverse, and aggregate structured records — a common pattern in data pipelines before using Pandas.

Uso practico de listas y diccionarios para representar, recorrer y agregar registros — patron comun en pipelines de datos antes de usar Pandas.

Topics covered / Temas cubiertos:
- Mixed-type lists / Listas de tipos mixtos
- Records as list-of-dicts / Registros como lista de diccionarios
- Aggregation by key / Agrupacion por clave
- Nested dictionaries with descriptive stats / Diccionarios anidados con estadisticas

---

### `lista_cuadrados.py` — List Comprehensions and Filtering / Comprensiones y Filtrado

Concise transformation and filtering patterns that translate directly to Pandas `.apply()`, `.query()`, and `.groupby()` logic.

Patrones concisos de transformacion y filtrado que se traducen directamente a `.apply()`, `.query()` y `.groupby()` de Pandas.

Topics covered / Temas cubiertos:
- Divisibility filters / Filtros de divisibilidad
- Even squares / Cuadrados de numeros pares
- Revenue calculation from transaction records / Calculo de ingresos desde registros
- Flattening nested lists / Aplanamiento de listas anidadas

---

## How to Run / Como ejecutar

```bash
git clone https://github.com/JulianDataScienceExplorerV2/Python-Data-Foundations.git
cd Python-Data-Foundations

# No external dependencies required / Sin dependencias externas
python list_and_dicts.py
python lista_cuadrados.py
```

---

## Context / Contexto

These exercises form the procedural foundation that underpins library-based data analysis. Understanding how aggregation and filtering work at the Python level makes Pandas and SQL patterns significantly more intuitive.

Estos ejercicios forman la base procedimental que sustenta el analisis de datos con librerias. Comprender como funcionan la agregacion y el filtrado a nivel de Python hace que Pandas y SQL sean significativamente mas intuitivos.

---

## Author / Autor

**Julian David Urrego** — Data Analyst
Python · Pandas · Scikit-learn · Data Wrangling

[![GitHub](https://img.shields.io/badge/GitHub-JulianDataScienceExplorerV2-181717?style=flat-square&logo=github)](https://github.com/JulianDataScienceExplorerV2)