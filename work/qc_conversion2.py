from pyqc import *

C_S = ControlledGate(S)
C_T = ControlledGate(T)

QFT_3 = Circuit([
    (H, 0),
    (C_S, (1, 0)),
    (C_T, (2, 0)),
    (H, 1),
    (C_S, (2, 1)),
    (H, 2),
    (SWAP, (0, 2))
])
QFT_3



with open('test12.qasm', 'r') as f:
    circ = Circuit.from_qasm(f.read())
