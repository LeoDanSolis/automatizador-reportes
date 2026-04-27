def generar_reporte(total, region, tienda, pagos, fechas):
    reporte = f"""
REPORTE DE VENTAS

TOTAL GENERAL: ${total}

VENTAS POR REGION:
{region.head(5).to_string()}

VENTAS POR TIENDA:
{tienda.head(5).to_string()}

METODOS DE PAGO:
{pagos.to_string()}

VENTAS POR FECHA:
{fechas.head(5).to_string()}
"""
    return reporte
