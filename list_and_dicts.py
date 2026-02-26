"""
Data Structures for Data Analysis
===================================
Demonstrates practical use of Python lists and dictionaries
as a foundation for working with tabular and structured data.

Estructuras de datos para analisis
====================================
Uso practico de listas y diccionarios como base para
trabajar con datos tabulares y estructurados.
"""

# ---------------------------------------------------------------------------
# 1. Basic types in a list / Tipos basicos en una lista
# ---------------------------------------------------------------------------
mixed_list = [42, "revenue", True, 3.14]
print("Mixed list / Lista mixta:", mixed_list)

# ---------------------------------------------------------------------------
# 2. Records as dictionaries / Registros como diccionarios
# ---------------------------------------------------------------------------
records = [
    {"name": "Ana Torres",    "region": "Norte",  "sales": 15200},
    {"name": "Carlos Ruiz",   "region": "Sur",    "sales": 9800},
    {"name": "Laura Medina",  "region": "Este",   "sales": 22400},
    {"name": "Jorge Salazar", "region": "Oeste",  "sales": 17600},
    {"name": "Maria Llanos",  "region": "Norte",  "sales": 13900},
]

print("\nSales records / Registros de ventas:")
for r in records:
    print(f"  {r['name']:<18} | {r['region']:<6} | ${r['sales']:>8,}")

# ---------------------------------------------------------------------------
# 3. Aggregation by key / Agrupacion por clave
# ---------------------------------------------------------------------------
region_totals = {}
for r in records:
    region = r["region"]
    region_totals[region] = region_totals.get(region, 0) + r["sales"]

print("\nTotal sales by region / Ventas totales por region:")
for region, total in sorted(region_totals.items(), key=lambda x: x[1], reverse=True):
    print(f"  {region:<8}: ${total:>8,}")

# ---------------------------------------------------------------------------
# 4. Nested dictionary / Diccionario anidado
# ---------------------------------------------------------------------------
portfolio = {
    "numeric":  [1, 2, 3, 4, 5],
    "negative": [-3, -2, -1, 0, 1, 2],
    "decimal":  [0.5, 1.75, 3.14, 2.71],
}

print("\nPortfolio summary / Resumen del portafolio:")
for key, values in portfolio.items():
    avg = sum(values) / len(values)
    print(f"  {key:<10}: count={len(values)}, mean={avg:.2f}, min={min(values)}, max={max(values)}")

if __name__ == "__main__":
    pass