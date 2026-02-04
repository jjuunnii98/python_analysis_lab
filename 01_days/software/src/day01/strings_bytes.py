from __future__ import annotations


def safe_replace(text: str, old: str, new: str) -> str:
    """문자열은 불변이므로 replace는 '새 문자열'을 반환한다."""
    return text.replace(old, new)


def is_string_immutable() -> bool:
    """문자열 인덱스 재할당이 실패(TypeError)함을 확인."""
    s = "this is a string"
    try:
        s[10] = "f"  # type: ignore[misc]
        return False
    except TypeError:
        return True


def to_utf8_bytes(text: str) -> bytes:
    """유니코드 문자열을 UTF-8 바이트로 인코딩."""
    return text.encode("utf-8")
