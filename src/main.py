import os

from generador import generar_reporte
from procesador import procesar_datos

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "ventas.xlsx")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "reporte.txt")


def main():
    total, region, tienda, pagos, fechas = procesar_datos(DATA_PATH)
    reporte = generar_reporte(total, region, tienda, pagos, fechas)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(reporte)

    print("Reporte generado correctamente")


if __name__ == "__main__":
    main()
