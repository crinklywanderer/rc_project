from qutip import *
from math import *

# operator arithmetic
H = 2 * sigmaz() + 0.5 * sigmax()  # operators
print('H :-', H, '\n')

# superposition states
psi = (basis(2, 0) + basis(2, 1)) / sqrt(2)
print('PSI :- ', psi, '\n')

a = sigmax()
print('a :- ', a, '\n')

b = coherent(5, 0.5)
print('b :- ', b, '\n')


g = 1.0 * 2 * pi  # coupling strength
g1 = 0.75
# relaxation rate
g2 = 0.25
# dephasing rate
n_th = 1.5
# environment temperature
T = pi / (4 * g)
H = g * (tensor(sigmax(), sigmax()) + tensor(sigmay(), sigmay()))
c_ops = []
# qubit 1 collapse operators
sm1 = tensor(sigmam(), qeye(2))
sz1 = tensor(sigmaz(), qeye(2))
c_ops.append(sqrt(g1 * (1 + n_th)) * sm1)
c_ops.append(sqrt(g1 * n_th) * sm1.dag())
c_ops.append(sqrt(g2) * sz1)
# qubit 2 collapse operators
sm2 = tensor(qeye(2), sigmam())
sz2 = tensor(qeye(2), sigmaz())
c_ops.append(sqrt(g1 * (1 + n_th)) * sm2)
c_ops.append(sqrt(g1 * n_th) * sm2.dag())
c_ops.append(sqrt(g2) * sz2)
U = propagator(H, T, c_ops)
print(U)
# qpt_plot(qpt(U, op_basis), op_labels)
