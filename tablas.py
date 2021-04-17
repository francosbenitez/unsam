"""
Ejercicio 1.10: Tablas
Modicá tu programa para que imprima una tabla mostrando el mes, el total pagado hasta el momento y el saldo restante. La salida debería verse aproximadamente así:

1 2684.11 499399.22
2 5368.22 498795.94
3 8052.33 498190.15
4 10736.44 497581.83
5 13420.55 496970.98
...
308 874705.88 3478.83
309 877389.99 809.21
310 880074.1 -1871.53
Total pagado:  880074.1
Meses:  310
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
    print(mes, round(total_pagado, 2), round(saldo, 2))
      
print('Total pagado:', round(total_pagado, 2), '\nMeses:', mes)

