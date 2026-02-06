from pathlib import Path


def get_cwd() -> Path:
    """현재 작업 디렉터리 반환"""
    return Path.cwd()


def list_files(path: Path) -> list[Path]:
    """주어진 디렉터리의 파일/폴더 목록 반환"""
    if not path.exists():
        raise FileNotFoundError(path)
    return list(path.iterdir())