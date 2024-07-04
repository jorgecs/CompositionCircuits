import numpy as np
from braket.devices import LocalSimulator
from braket.circuits import Circuit
from collections import Counter

shots = 1024

circuit = Circuit()
circuit.h(0)
circuit.h(1)
circuit.x(1)
circuit.h(1)
circuit.cnot(0, 1)
circuit.h(1)
circuit.x(1)
circuit.h(1)
