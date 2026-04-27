import os

import matplotlib.pyplot as plt
import pandas as pd


def procesar_datos(ruta):
    df = pd.read_excel(ruta)
    df["fecha"] = pd.to_datetime(df["fecha"])

    total_general = df["precio"].sum()
    ventas_region = df.groupby("region")["precio"].sum().sort_values(ascending=False)
    ventas_tienda = df.groupby("tienda")["precio"].sum().sort_values(ascending=False)
    metodos_pago = df["forma_pago"].value_counts()
    ventas_fecha = df.groupby(df["fecha"].dt.date)["precio"].sum()

    output_dir = os.path.join(os.path.dirname(ruta), "..", "output")
    os.makedirs(output_dir, exist_ok=True)

    ventas_region.head(5).plot(kind="bar")
    plt.title("Ventas por region")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "grafica.png"))
    plt.close()

    return total_general, ventas_region, ventas_tienda, metodos_pago, ventas_fecha
