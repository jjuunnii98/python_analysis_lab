# 03_days/analysis/03_files_and_os_walkthrough.py
"""
Day 03 — Analysis Track
주제: 파일과 운영체제(File & OS)

목표:
- 파일 경로, 읽기/쓰기, 디렉터리 탐색을 직접 실행하며 확인
- OS가 파일을 어떻게 관리하는지 관찰
"""

from pathlib import Path
import os


def section(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def demo_paths() -> None:
    section("1) 현재 작업 디렉터리와 경로")

    cwd = Path.cwd()
    print("Current working directory:", cwd)

    example = cwd / "example.txt"
    print("Example path:", example)
    print("Exists?:", example.exists())


def demo_file_write_read() -> None:
    section("2) 파일 쓰기 / 읽기")

    path = Path("sample.txt")

    # write
    path.write_text("Hello File System!\nThis is Day03.")
    print("File written:", path.resolve())

    # read
    content = path.read_text()
    print("File content:")
    print(content)


def demo_directory_listing() -> None:
    section("3) 디렉터리 탐색")

    here = Path(".")
    for p in here.iterdir():
        print("DIR ENTRY:", p.name)


def demo_file_iterator() -> None:
    section("4) 파일은 이터레이터다")

    path = Path("sample.txt")

    with path.open() as f:
        for line in f:
            print("LINE:", line.strip())


def demo_os_module() -> None:
    section("5) os 모듈")

    print("OS name:", os.name)
    print("Environment variables (sample):")
    for k in list(os.environ.keys())[:5]:
        print(k, "=", os.environ[k])


def main() -> None:
    demo_paths()
    demo_file_write_read()
    demo_directory_listing()
    demo_file_iterator()
    demo_os_module()


if __name__ == "__main__":
    main()