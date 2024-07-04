import numpy as np
from braket.devices import LocalSimulator
from braket.circuits import Circuit
from collections import Counter

shots = 1024

circuit = Circuit()
circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.h(3)
circuit.ccnot(1, 0, 3)
circuit.cnot(0, 1)
circuit.ccnot(1, 2, 3)
circuit.cnot(1, 2)
circuit.cnot(0, 1)
