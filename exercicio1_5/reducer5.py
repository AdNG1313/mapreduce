#!/usr/bin/python3

import sys

numeroVendas = 0
totalVendas = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    tipoPago, dolarPago = data_mapped

    numeroVendas += 1
    totalVendas += float(dolarPago)

print("O ingreso total das ", numeroVendas," vendas foi: ", totalVendas)

