#!/usr/bin/python3

import sys

ventaAlta = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    tipoPago, dolarPago = data_mapped

    if ventaAlta < float(dolarPago):
        ventaAlta = float(dolarPago)

print("A venda máis alta foi: ", ventaAlta)
