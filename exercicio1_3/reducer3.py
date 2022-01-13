#!/usr/bin/python3

import sys

ventaAlta = 0
tipoAnterior = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    tipoPago, dolarPago = data_mapped

    if tipoAnterior and tipoAnterior != tipoPago:
        print(tipoAnterior, "\t", ventaAlta)
        ventaAlta = 0

    tipoAnterior = tipoPago
    if ventaAlta < float(dolarPago):
        ventaAlta = float(dolarPago)

if tipoAnterior != None:
    print(tipoAnterior, "\t", ventaAlta)
