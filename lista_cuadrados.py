"""
List Comprehensions and Filtering
====================================
Common patterns used in data wrangling and pipeline transformations.

Comprensiones de listas y filtrado
=====================================
Patrones comunes en limpieza de datos y transformaciones de pipelines.
"""

# ---------------------------------------------------------------------------
# 1. Multiples of 12 up to 1000 / Multiplos de 12 hasta 1000
# (original: multiples common to 4, 6, and 9)
# ---------------------------------------------------------------------------
multiples_of_12 = [n for n in range(1, 1001) if n % 12 == 0]
print(f"Multiples of 12 up to 1,000 / Multiplos de 12 hasta 1,000:")
print(f"  Count: {len(multiples_of_12)} | First 5: {multiples_of_12[:5]} | Last 5: {multiples_of_12[-5:]}")

# ---------------------------------------------------------------------------
# 2. Even squares / Cuadrados de numeros pares
# ---------------------------------------------------------------------------
even_squares = [n ** 2 for n in range(1, 21) if n % 2 == 0]
print(f"\nEven squares (1-20) / Cuadrados pares (1-20):")
print(f"  {even_squares}")

# ---------------------------------------------------------------------------
# 3. Filtering and transforming records / Filtrado y transformacion
# ---------------------------------------------------------------------------
transactions = [
    {"product": "Laptop Pro",   "units": 12, "price": 1200.0},
    {"product": "Monitor 4K",   "units": 0,  "price": 450.0},
    {"product": "Keyboard",     "units": 35, "price": 85.0},
    {"product": "USB Hub",      "units": 0,  "price": 28.5},
    {"product": "Webcam HD",    "units": 20, "price": 95.0},
    {"product": "Desk Lamp",    "units": 5,  "price": 40.0},
]

# Only active products / Solo productos con ventas activas
active = [t for t in transactions if t["units"] > 0]

# Revenue per product / Ingreso por producto
revenue = [
    {"product": t["product"], "revenue": round(t["units"] * t["price"], 2)}
    for t in active
]

print("\nRevenue per active product / Ingreso por producto activo:")
for item in sorted(revenue, key=lambda x: x["revenue"], reverse=True):
    print(f"  {item['product']:<16}: ${item['revenue']:>8,.2f}")

total = sum(item["revenue"] for item in revenue)
print(f"\n  Total revenue / Ingreso total: ${total:>10,.2f}")

# ---------------------------------------------------------------------------
# 4. Flattening nested lists / Aplanando listas anidadas
# ---------------------------------------------------------------------------
weekly_sales = [[120, 95, 110], [88, 102, 134], [99, 115, 107]]
flat_sales   = [day for week in weekly_sales for day in week]
print(f"\nFlattened daily sales / Ventas diarias aplanadas:")
print(f"  {flat_sales}")
print(f"  Average / Promedio: {sum(flat_sales)/len(flat_sales):.1f}")

if __name__ == "__main__":
    pass