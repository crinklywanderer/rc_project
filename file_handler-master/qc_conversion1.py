from pyqc import *

circuit_image = open('alpha.txt', 'w')
print(Circuit.from_wires([H, CNOT.c, H], [H, CNOT.t, H]))
circuit_image.write(str(Circuit.from_wires([H, CNOT.c, H], [H, CNOT.t, H])))
circuit_image.close()

alpha_n = Circuit([(H, 0)])
