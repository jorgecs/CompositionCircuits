import numpy as np
from braket.devices import LocalSimulator
from braket.circuits import Circuit
from collections import Counter

shots = 1024

circuit = Circuit()
circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.h(2)
circuit.cphaseshift(2,1,np.pi/2)
circuit.cphaseshift(2,0,np.pi/4)
circuit.h(1)
circuit.cphaseshift(1,0,np.pi/2)
circuit.h(0)
circuit.swap(0, 2)
