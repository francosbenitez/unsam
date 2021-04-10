"""
Ejercicio 1.11: Bonus
Ya que estamos, corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado.

Asegurate de guardar en el archivo hipoteca.py esta última versión en tu directorio ejercicios_python/Clase01/. Vamos a volver a trabajar con él.
"""

saldo = 500000
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0
pago_extra = 1000
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108

while saldo > 0:
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
      saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
      total_pagado = total_pagado + pago_mensual + pago_extra
      mes = mes + 1
    else:
      saldo = saldo * (1+tasa/12) - pago_mensual
      total_pagado = total_pagado + pago_mensual
      mes = mes + 1
    if saldo < 0:
       saldo = 0
    print(mes, round(total_pagado, 2), round(saldo, 2))
      
print('Total pagado:', round(total_pagado, 2), '\nMeses:', mes)

