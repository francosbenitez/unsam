"""
Ejercicio 1.7: La hipoteca de David
David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.

El siguiente es un programa que calcula el monto total que pagará David a lo largo de los años:

# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
   saldo = saldo * (1+tasa/12) - pago_mensual
   total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))
Copiá este código y correlo. Deberías obtener 966279.6 como respuesta.

Ejercicio 1.8: Adelantos
Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.

Modificá el programa para incorporar estos pagos extra y que imprima el monto total pagado junto con la cantidad de meses requeridos.

Cuando lo corras, este nuevo programa debería dar un pago total de 929965.62 en 342 meses.

Aclaración: aunque puede parecer sencillo, este ejercicio requiere que agregues una variable mes y que prestes bastante atención a cuándo la incrementás, con qué valor entra al ciclo y con qué valor sale del ciclo. Una posiblidad es inicializar mes en 0 y otra es inicializarla en 1. En el primer caso es problable que la variable salga del ciclo contando la cantidad de pagos que se hicieron, en el segundo, ¡es probable que salga contando la cantidad de pagos más uno!
"""

saldo = 500000
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0
pago_extra = 1000
mes = 0

while saldo > 0:
    if mes < 12:
      saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
      total_pagado = total_pagado + pago_mensual + pago_extra
      mes = mes + 1
    else:
      saldo = saldo * (1+tasa/12) - pago_mensual
      total_pagado = total_pagado + pago_mensual
      mes = mes + 1

print('Total pagado', round(total_pagado, 2), 'en', mes, 'meses')



