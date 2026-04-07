# 01. Retail Analytics

리테일/이커머스 데이터를 기반으로 고객 행동 및 매출 패턴을 분석합니다.

## Dataset

- 추천: [Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii) / Kaggle E-commerce datasets
- `data/raw/` 에 원본 데이터 저장

## Analysis Flow

| Notebook | 내용 |
|---|---|
| `01_eda.ipynb` | 데이터 탐색, 분포, 결측치, 이상치 |
| `02_feature_engineering.ipynb` | RFM 피처, 날짜 파생변수, 인코딩 |
| `03_modeling.ipynb` | 고객 이탈 예측, 세그멘테이션 (클러스터링) |
| `04_insights.ipynb` | 결과 해석, 비즈니스 인사이트 도출 |

## Key Questions

- 어떤 고객이 이탈 위험이 높은가?
- 구매 패턴으로 고객 세그먼트를 어떻게 나눌 수 있는가?
- 매출에 기여도가 높은 상품/카테고리는 무엇인가?
