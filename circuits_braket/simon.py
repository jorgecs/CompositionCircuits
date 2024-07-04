import numpy as np
from braket.devices import LocalSimulator
from braket.circuits import Circuit
from collections import Counter

shots = 1024

circuit = Circuit()
circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.cnot(0, 3)
circuit.h(0)
circuit.cnot(1, 4)
circuit.cnot(2, 5)
circuit.cnot(1, 4)
circuit.cnot(1, 5)
circuit.h(1)
circuit.h(2)
