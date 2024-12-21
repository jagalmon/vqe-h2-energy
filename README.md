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

## 참고 자료

- Qiskit Documentation: https://qiskit.org/documentation/
- Qiskit Nature: https://qiskit.org/ecosystem/nature/
- IBM Quantum Experience: https://quantum-computing.ibm.com/

## AI로 양자 컴퓨터 프로그래밍이 불가능한 이유

- 양자 컴퓨터 분야에서 AI를 활용한 코딩은 현실적으로 불가능에 가깝습니다. Qiskit과 같은 양자 프로그래밍 라이브러리는 기술의 급속한 발전과 함께 API, 클래스, 사용법이 자주 변경됩니다. 새로운 알고리즘과 최적화가 추가되면서 기존 코드가 금세 호환되지 않는 경우가 빈번합니다.
- 특히 AI는 학습 시점의 데이터를 기반으로 작동하기 때문에, 지속적으로 변화하는 최신 정보를 정확히 반영하지 못합니다. 또한, 양자 컴퓨팅은 복잡한 수학적 배경과 물리적 이해가 필수적이므로, 단순히 AI가 코드를 생성한다고 해서 실질적인 문제 해결이 어렵습니다.
- 결과적으로, 빠르게 변화하는 양자 컴퓨터 생태계에서는 AI로 신뢰할 수 있는 코드를 작성하는 것이 거의 불가능합니다. 최신 정보를 숙지하고 직접 프로그래밍하는 접근이 여전히 필수적입니다.

## License

- This project is licensed under the MIT License. See the LICENSE file for details.
