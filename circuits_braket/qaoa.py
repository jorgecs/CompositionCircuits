import numpy as np
from braket.devices import LocalSimulator
from braket.circuits import Circuit
from collections import Counter

shots = 1024

circuit = Circuit()
circuit.rx(0, 0.5)
circuit.rx(1, 0.5)
circuit.cnot(0, 1)
circuit.rx(0, 0.5)
circuit.rx(1, 0.5)
circuit.rx(1, 0.5)
circuit.cnot(0, 1)
circuit.rx(0, 0.5)
