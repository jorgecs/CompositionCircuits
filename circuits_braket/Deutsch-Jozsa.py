import numpy as np
from braket.devices import LocalSimulator
from braket.circuits import Circuit
from collections import Counter

shots = 1024

circuit = Circuit()
circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.x(3)
circuit.x(0)
circuit.x(2)
circuit.h(3)
circuit.cnot(0, 3)
circuit.x(0)
circuit.cnot(1, 3)
circuit.h(0)
circuit.h(1)
circuit.cnot(2, 3)
circuit.x(2)
circuit.h(2)
