# Day 02 — Analysis Track (Pages 83–107)

## 목표
Day 02에서는 파이썬 내장 자료구조(Sequence/Mapping/Set)와 반복 유틸리티(enumerate, sorted, zip)를
"실험 → 관찰 → 결론" 흐름으로 정리한다.

이 디렉터리는 **학습/탐색(analysis)** 용도로,
- 출력(print)과 예외 처리(try/except)를 포함할 수 있고
- 셀 단위(노트북) 느낌의 데모를 .py로 실행 가능하게 구성한다.

## 범위 (책 83–107p)
- Tuple: 생성, 인덱싱, 언패킹(unpacking), `*rest`
- List: 변경 가능성, 슬라이싱, `append` vs `extend`
- Dict: 생성/조회/삽입, `in`, `get`, `items()`, dict comprehension
- Set: 중복 제거, 합/교/차집합
- Built-ins: `enumerate`, `sorted`, `zip`

## 실행 파일
- `02_structures_walkthrough.py`
  - 튜플/리스트/딕트/셋의 핵심 동작을 한 번에 실험
  - 교재의 “설명용 placeholder 코드(바디 없는 for문 등)”를 제거하고 **실행 가능한 형태**로 정리

## 실행 방법
macOS에서는 보통 `python` 대신 `python3`를 사용한다.

```bash
python3 02_days/analysis/02_structures_walkthrough.py
