from pathlib import Path
from day03.file_io import write_text, read_text, read_lines
from day03.paths import get_cwd, list_files


def test_cwd_exists():
    cwd = get_cwd()
    assert cwd.exists()


def test_write_and_read(tmp_path: Path):
    file_path = tmp_path / "test.txt"

    write_text(file_path, "hello")
    assert read_text(file_path) == "hello"


def test_read_lines(tmp_path: Path):
    file_path = tmp_path / "lines.txt"
    write_text(file_path, "a\nb\nc")

    lines = list(read_lines(file_path))
    assert lines == ["a", "b", "c"]


def test_list_files(tmp_path: Path):
    (tmp_path / "a.txt").write_text("a")
    (tmp_path / "b.txt").write_text("b")

    files = list_files(tmp_path)
    names = {p.name for p in files}
    assert names == {"a.txt", "b.txt"}