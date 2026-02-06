from pathlib import Path
from typing import Iterable


def write_text(path: Path, text: str) -> None:
    """텍스트 파일 쓰기"""
    path.write_text(text)


def read_text(path: Path) -> str:
    """텍스트 파일 읽기"""
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text()


def read_lines(path: Path) -> Iterable[str]:
    """파일을 한 줄씩 반환 (iterator)"""
    if not path.exists():
        raise FileNotFoundError(path)

    with path.open() as f:
        for line in f:
            yield line.rstrip("\n")