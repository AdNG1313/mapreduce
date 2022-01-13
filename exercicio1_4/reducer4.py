#!/usr/bin/python3

import sys

ventaAlta = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    dolarPago = data_mapped[0]

    if ventaAlta < float(dolarPago):
        ventaAlta = float(dolarPago)

print("A venda máis alta foi: ", ventaAlta)
