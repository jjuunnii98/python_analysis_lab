# Day 03 — Analysis Track (Files & Operating System)

## 🎯 목표
Day 03의 analysis 트랙에서는 **파일과 운영체제(OS)** 개념을
직접 실행해 보며 관찰하는 것을 목표로 한다.

- 파일이 OS에 의해 어떻게 관리되는지
- 경로(Path)가 왜 중요한지
- 파일 객체가 왜 이터레이터인지  
를 **실험 중심 코드**로 확인한다.

---

## 📌 다루는 핵심 개념
- 현재 작업 디렉터리(Current Working Directory)
- 절대경로 / 상대경로
- 파일 생성, 읽기, 쓰기
- 디렉터리 탐색
- 파일 객체와 이터레이터
- `os` vs `pathlib` 모듈

---

## 📂 주요 파일
- `03_files_and_os_walkthrough.py`
  - 파일 시스템과 OS 동작을 단계적으로 실험
  - 출력(`print`)과 임시 파일 생성을 허용
  - 개념 확인을 위한 관찰용 코드 중심

---

## 🔍 분석 관점 포인트
- 파일 접근은 항상 **운영체제를 통해 이루어진다**
- 파일 객체는 **한 줄씩 읽을 수 있는 이터레이터**
- 문자열 기반 경로 처리보다 **`pathlib.Path`가 안전**
- analysis 코드에서는
  - 가독성
  - 관찰 가능성
  - 개념 명확성  
  을 우선한다

---

## ▶️ 실행 방법
macOS 기준:

```bash
python3 03_days/analysis/03_files_and_os_walkthrough.py