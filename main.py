# 양자 컴퓨터를 이용한 수소 분자의 결합 길이 변화에 따른 에너지 상태 분석 및 전위 에너지 곡선 도출
from qiskit.circuit.library import TwoLocal
from qiskit.primitives import Estimator
from qiskit_algorithms import VQE
from qiskit_algorithms.optimizers import COBYLA
from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mappers import ParityMapper
from qiskit_nature.second_q.problems import ElectronicStructureProblem
from qiskit_nature.second_q.transformers import ActiveSpaceTransformer
import numpy as np
import matplotlib.pyplot as plt
import config

if config.EXE_BACKEND == "IBM": # IBM: IBM Quantum 하드웨어
    '''
    from qiskit_ibm_provider import IBMProvider

    IBMProvider.save_account(token='IBM_QUANTUM_API_TOKEN', overwrite=True)
    provider = IBMProvider()
    backend = provider.get_backend('ibmq_qasm')
    estimator = Estimator(backend=backend)
    '''
elif config.EXE_BACKEND == "Google":
    '''
    '''
elif config.EXE_BACKEND == "IonQ":
    '''
    '''
elif config.EXE_BACKEND == "Rigetti":
    '''
    '''
elif config.EXE_BACKEND == "Azure":
    '''
    '''
else: # statevector_simulator
    # Estimator는 양자 회로의 기대값을 계산하는 데 사용됩니다.
    estimator = Estimator()

# 결합 길이(bond length)를 minÅ에서 maxÅ까지 count개의 값으로 설정
# 이 범위는 분자의 원자핵 사이 거리가 어떻게 에너지에 영향을 미치는지 보여줍니다.
bond_lengths = np.linspace(config.BOND_MIN, config.BOND_MAX, config.BOND_COUNT)
energies = []

# 활성 공간 변환기는 계산 효율성을 높이기 위해 필요한 전자와 궤도만 선택합니다.
# 여기서는 수소 분자의 전자 수와 궤도 수를 설정합니다.
num_electrons = config.NUM_ELECTRONS # 수소 분자에는 전자 2개가 존재합니다.
num_spatial_orbitals = config.NUM_SPATIAL_ORBITALS # 공간적 궤도 수를 설정합니다.
transformer = ActiveSpaceTransformer(num_electrons=num_electrons, num_spatial_orbitals=num_spatial_orbitals)

# VQE 알고리즘에서 사용하는 변분 회로(Ansatz)를 생성합니다.
# TwoLocal 회로는 양자 게이트와 얽힘을 정의하는 데 사용됩니다.
ansatz = TwoLocal(rotation_blocks="ry", entanglement_blocks="cz", reps=2)

# VQE에서 사용하는 고전적 최적화 알고리즘을 설정합니다.
# 여기서는 COBYLA를 사용하며 최대 200번의 반복을 허용합니다.
optimizer = COBYLA(maxiter=200)

# VQE 알고리즘을 설정합니다.
# VQE는 변분 양자 알고리즘으로, 바닥 상태 에너지를 계산하는 데 사용됩니다.
vqe = VQE(ansatz=ansatz, optimizer=optimizer, estimator=estimator)

for bond_length in bond_lengths:
    # 현재 결합 길이에 따라 수소 분자의 원자 좌표를 정의합니다.
    atom = f"H 0 0 0; H 0 0 {bond_length}"

    # PySCFDriver를 사용해 분자의 전자 구조 데이터를 생성합니다.
    driver = PySCFDriver(atom=atom, basis="sto3g")
    driver_result = driver.run()

    # PySCFDriver의 결과에서 해밀토니안(Hamiltonian)을 추출합니다.
    hamiltonian = driver_result.hamiltonian

    # 활성 공간 변환기를 적용하여 필요한 전자와 궤도만 변환합니다.
    transformed_driver_result = transformer.transform(driver_result)

    # 해밀토니안을 기반으로 전자 구조 문제를 생성합니다.
    problem = ElectronicStructureProblem(hamiltonian)

    # 전자 구조 문제를 큐비트 연산자로 변환합니다.
    # ParityMapper를 사용해 전자 구조 문제를 양자 회로에서 처리할 수 있는 형태로 매핑합니다.
    second_q_op = problem.hamiltonian.second_q_op()

    # VQE 알고리즘을 실행하여 바닥 상태 에너지를 계산합니다.
    mapper = ParityMapper() # ParityMapper는 분자를 큐비트 상태로 매핑.
    qubit_op = mapper.map(second_q_op)

    # VQE 알고리즘을 실행하여 바닥 상태 에너지를 계산합니다.
    result = vqe.compute_minimum_eigenvalue(qubit_op)
    energies.append(result.eigenvalue.real)

    print("Calculated ground state energy (Hartree):", result.eigenvalue.real)

# 계산된 결합 길이와 에너지 데이터를 사용하여 그래프 생성
plt.figure(figsize=(10, 6)) # 그래프 크기 설정
plt.plot(bond_lengths, energies, marker='o', linestyle='-', label="Potential Energy Curve") # 에너지 곡선
plt.title("Potential Energy Curve for H2 Molecule", fontsize=14) # 그래프 제목
plt.xlabel("Bond Length (Å)", fontsize=12) # X축: 결합 길이
plt.ylabel("Energy (Hartree)", fontsize=12) # Y축: 에너지
# 평형 결합 거리 equilibrium bond length: 분자가 가장 안정한 상태(에너지가 최소화되는 상태)
plt.axvline(x=config.H2_ANGSTROM, color='r', linestyle='--', label=f"Equilibrium Bond Length (~{config.H2_ANGSTROM} Å)")
plt.legend() # 범례 추가
plt.grid(alpha=0.5) # 그래프 그리드 추가 (가시성 개선)
plt.show() # 전위 에너지 곡선 그래프 표시
