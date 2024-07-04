import numpy as np
from braket.devices import LocalSimulator
from braket.circuits import Circuit
from collections import Counter

shots = 1024

circuit = Circuit()
# Unsupported gate "reset".
# Unsupported gate "reset".
# Unsupported gate "reset".
# Unsupported gate "reset".
circuit.x(0)
circuit.x(1)
circuit.x(2)
circuit.x(3)
circuit.x(0)
circuit.cnot(1, 2)
circuit.cnot(2, 1)
circuit.cnot(1, 2)
circuit.cnot(2, 3)
circuit.cnot(3, 2)
circuit.cnot(2, 3)
circuit.cnot(0, 3)
circuit.cnot(3, 0)
circuit.cnot(0, 3)
