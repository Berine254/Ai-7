# Quantum Simulation using Qiskit (IBM Quantum)
from qiskit import QuantumCircuit, Aer, execute

# 4-Qubit Grover's Circuit to search for '1010'
qc = QuantumCircuit(4, 4)

# Step 1: Superposition
qc.h([0, 1, 2, 3])

# Step 2: Oracle for '1010' (example)
qc.x([0, 2])  # Flip bits that are 0 in target
qc.h(3)
qc.mct([0, 1, 2], 3)  # Multi-controlled Toffoli
qc.h(3)
qc.x([0, 2])  # Undo flips

# Step 3: Diffusion Operator
qc.h([0, 1, 2, 3])
qc.x([0, 1, 2, 3])
qc.h(3)
qc.mct([0, 1, 2], 3)
qc.h(3)
qc.x([0, 1, 2, 3])
qc.h([0, 1, 2, 3])

# Measurement
qc.measure([0, 1, 2, 3], [0, 1, 2, 3])

# Simulate
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, backend=simulator, shots=1024).result()
counts = result.get_counts()
print(counts)