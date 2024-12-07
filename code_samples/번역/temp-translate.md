Clipper is divided across two abstractions, aptly named model selection and model abstraction layers. The model selection layer is quite sophisticated in that it uses an adaptive online model selection policy and various ensemble techniques. 

클리퍼는 모델 선택과 모델 추상화 두 개의 추상화된 레이어로 나뉩니다. 모델 선택 계층은 적응형 온라인 모델 선택 정책과 다양한 앙상블 기술을 사용한다는 점에서 매우 정교합니다. 모델은 애플리케이션의 수명이 다할 때까지 피드백을 통해 지속적으로 학습하므로, 모델 선택 계층은 실패한 모델을 자체 교정합니다.

Since the model is continuously learning from feedback throughout the lifetime of the application, the model selection layer self-calibrates failed models without needing to interact directly with the policy layer.

