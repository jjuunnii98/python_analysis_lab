# 03. Healthcare ML

헬스케어 데이터를 기반으로 환자 리스크 예측 및 임상 피처 분석을 수행합니다.

## Dataset

- 추천: [Heart Disease UCI](https://archive.ics.uci.edu/dataset/45/heart+disease), [Diabetes](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- `data/raw/` 에 원본 데이터 저장

## Analysis Flow

| Notebook | 내용 |
|---|---|
| `01_eda.ipynb` | 임상 변수 탐색, 결측치, 클래스 불균형 확인 |
| `02_feature_engineering.ipynb` | 피처 선택, 스케일링, 불균형 처리 (SMOTE 등) |
| `03_modeling.ipynb` | 분류 모델 (Logistic, XGBoost, RF), ROC/AUC 평가 |
| `04_insights.ipynb` | 피처 중요도, SHAP 해석, 임상적 시사점 |

## Key Questions

- 어떤 임상 변수가 질병 예측에 가장 중요한가?
- 클래스 불균형이 모델 성능에 미치는 영향은?
- 예측 결과를 어떻게 임상적으로 해석할 수 있는가?
