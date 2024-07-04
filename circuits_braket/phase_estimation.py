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
circuit.cphaseshift(0,3,np.pi/4)
circuit.cphaseshift(1,3,np.pi/4)
circuit.cphaseshift(1,3,np.pi/4)
circuit.cphaseshift(2,3,np.pi/4)
circuit.cphaseshift(2,3,np.pi/4)
circuit.cphaseshift(2,3,np.pi/4)
circuit.cphaseshift(2,3,np.pi/4)
circuit.swap(0, 2)
circuit.h(0)
circuit.cphaseshift(0,1,-np.pi/2)
circuit.h(1)
circuit.cphaseshift(0,2,-np.pi/4)
circuit.cphaseshift(1,2,-np.pi/2)
circuit.h(2)
