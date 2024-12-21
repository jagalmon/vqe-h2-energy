# 양자 컴퓨터를 이용한 수소 분자(H₂)의 결합 길이 변화에 따른 에너지 상태 분석 및 전위 에너지 곡선 도출

- 작성자 : 김병민
- 이 코드는 수소 분자(H₂)의 전위 에너지 곡선을 시뮬레이션하는 Python 프로그램입니다. Qiskit Nature와 변분 양자 고유값 해법(VQE) 알고리즘을 활용하여 다양한 결합 길이에서 H₂ 분자의 바닥 상태 에너지를 계산합니다.

## 주요 기능

- 다양한 결합 길이에 따른 H₂ 분자의 전위 에너지 곡선 시뮬레이션
- Qiskit Nature를 활용한 양자 화학 시뮬레이션
- 활성 공간 변환기를 사용하여 문제 크기를 최적화
- VQE 알고리즘과 매개변수화된 양자 회로(TwoLocal), COBYLA 최적화 알고리즘 구현
- 다양한 실행 백엔드 지원(IBM Quantum, statevector simulator)
- Matplotlib을 이용한 에너지 곡선 시각화

## 필수 라이브러리

- Python 3.8 이상(현재 리파지토리는 3.11.9에서 빌드 및 실행)
- qiskit
- qiskit-algorithms
- qiskit-nature
- numpy
- pyscf
- matplotlib

## 설정

- 실행 전, config.py 파일을 수정하여 시뮬레이션 매개변수를 설정합니다. 결합 길이, 활성 공간 설정, 실행 백엔드 등의 매개변수를 포함하고 있습니다.

## 결과

- 프로그램은 결합 길이와 바닥 상태 에너지 간의 관계를 보여주는 H₂ 분자의 전위 에너지 곡선을 생성합니다. 또한 그래프에 평형 결합 거리(equilibrium bond length)를 강조 표시하여 분자가 가장 안정된 상태를 나타냅니다.

## 참고 사항

- 이 코드는 양자 화학 분야에서 교육 및 실험 목적으로 설계되었습니다.
- IBM Quantum 하드웨어에서 실행하려면 유효한 IBM Quantum 계정과 API 토큰이 필요합니다.
- 기본 기저 세트는 STO-3G이며, 활성 공간 변환기를 통해 필수 궤도와 전자에만 집중하여 계산 효율성을 높입니다.

### 참고 사항 - AI로 양자 컴퓨터 프로그래밍이 불가능한 이유

- 양자 컴퓨터 분야에서 AI를 활용한 코딩은 사실상 불가능에 가깝습니다. 이는 양자 컴퓨팅의 특수성과 생태계의 급격한 변화 때문입니다. 특히, 관련 패키지의 버전 차이와 환경 의존성이 크기 때문에 AI가 이를 정확히 처리하기 어렵습니다.

1. 빠르게 변화하는 생태계
Qiskit과 같은 양자 프로그래밍 라이브러리는 지속적으로 업데이트되며, 새로운 알고리즘과 최적화가 추가됩니다. 이 과정에서 기존 API와 함수가 자주 변경되거나 호환되지 않는 경우가 많습니다. Python, Qiskit, Qiskit Algorithms, Qiskit Nature, Numpy, Scipy, PySCF 등 관련 패키지의 각 버전이 달라질수록 동일한 코드조차 실행되지 않거나, 다른 결과를 낼 수 있습니다.

2. 환경 의존성
양자 컴퓨팅 종사자들조차도 자신의 설정된 환경 외에서는 코드를 실행하거나 개발하기가 어렵습니다. 이는 다양한 패키지의 버전 호환성과 실행 환경이 복잡하게 얽혀 있기 때문입니다. AI는 이러한 복잡성을 이해하고 각 환경에 맞는 코드를 작성하는 데 한계가 있습니다.

3. 양자 컴퓨팅의 복잡성
양자 프로그래밍은 단순한 코딩 이상의 복잡한 수학적, 물리적 이해를 요구합니다. 양자 상태, 게이트 연산, 회로 최적화 등은 AI가 단순히 학습된 데이터로 처리하기에는 너무 전문적이고 다면적입니다.

4. AI의 한계
AI는 과거의 데이터를 기반으로 작동하기 때문에, 최신 패키지 변경 사항이나 환경별 요구사항을 반영할 수 없습니다. 또한, AI가 생성한 코드가 양자 알고리즘의 복잡성을 충족시키지 못할 가능성이 큽니다.

5. 오류와 디버깅의 어려움
패키지 간 버전 불일치로 인한 오류는 AI가 스스로 해결하기 어렵습니다. 예를 들어, Qiskit의 특정 버전에서 작동하는 코드가 Qiskit Nature의 최신 버전에서는 호환되지 않을 수 있습니다. AI는 이러한 문제를 분석하고 해결하는 데 한계가 있습니다.

- 양자 컴퓨팅 프로그래밍은 급격히 변화하는 생태계, 복잡한 환경 의존성, 패키지 간의 호환성 문제로 인해 AI가 코드를 완벽히 작성하거나 실행 가능한 상태로 유지하는 것이 사실상 불가능합니다. AI는 간단한 보조 작업에서만 유용할 수 있지만, 양자 컴퓨팅의 실질적인 개발은 개발자의 역할이 필수적입니다.

## 참고 자료

- Qiskit Documentation: https://qiskit.org/documentation/
- Qiskit Nature: https://qiskit.org/ecosystem/nature/
- IBM Quantum Experience: https://quantum-computing.ibm.com/

## License

- This project is licensed under the MIT License. See the LICENSE file for details.
