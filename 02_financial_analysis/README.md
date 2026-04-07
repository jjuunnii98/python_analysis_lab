# 02. Financial Analysis

금융/시장 데이터를 기반으로 수익률, 변동성, 리스크 지표를 분석합니다.

## Dataset

- 추천: Yahoo Finance (`yfinance`), Kaggle Stock Market datasets
- `data/raw/` 에 원본 데이터 저장

## Analysis Flow

| Notebook | 내용 |
|---|---|
| `01_eda.ipynb` | 가격/거래량 탐색, 수익률 분포 |
| `02_feature_engineering.ipynb` | 기술적 지표 (MA, RSI, Bollinger), 변동성 계산 |
| `03_modeling.ipynb` | 가격 방향 예측, 포트폴리오 최적화 |
| `04_insights.ipynb` | 리스크/수익 분석, 전략 백테스트 결과 |

## Key Questions

- 자산 간 상관관계는 어떻게 되는가?
- 변동성 클러스터링이 존재하는가?
- 기술적 지표로 가격 방향 예측이 가능한가?
