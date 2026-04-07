# Python Analysis Lab

데이터 분석 & 머신러닝 포트폴리오 프로젝트. 각 폴더는 독립된 도메인 데이터를 바탕으로 EDA부터 모델링, 인사이트 도출까지 다룹니다.

## Structure

| Folder | Domain | Focus |
|---|---|---|
| `01_retail_analytics/` | 리테일/이커머스 | 고객 세그멘테이션, 이탈 예측, 매출 분석 |
| `02_financial_analysis/` | 금융/시장 | 수익률, 변동성, 포트폴리오 최적화 |
| `03_healthcare_ml/` | 헬스케어 | 환자 리스크 예측, 임상 피처 분석 |
| `shared/` | 공통 | 재사용 유틸리티, 시각화 설정 |

## Analysis Flow (per project)

```
01_eda → 02_feature_engineering → 03_modeling → 04_insights
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
