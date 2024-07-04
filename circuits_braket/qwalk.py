import numpy as np
from braket.devices import LocalSimulator
from braket.circuits import Circuit
from collections import Counter

shots = 1024

circuit = Circuit()
circuit.h(2)
circuit.cnot(2, 1)
circuit.ccnot(2, 1, 0)
circuit.x(2)
circuit.cnot(2, 1)
circuit.x(1)
circuit.ccnot(2, 1, 0)
circuit.x(1)
circuit.x(2)
circuit.cnot(2, 1)
circuit.ccnot(2, 1, 0)
circuit.x(2)
circuit.cnot(2, 1)
circuit.x(1)
circuit.ccnot(2, 1, 0)
circuit.x(1)
circuit.x(2)
