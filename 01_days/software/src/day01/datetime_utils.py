from __future__ import annotations

from datetime import datetime


def format_dt(dt: datetime, fmt: str = "%Y-%m-%d %H:%M") -> str:
    return dt.strftime(fmt)


def parse_dt(text: str, fmt: str = "%Y%m%d %H:%M") -> datetime:
    return datetime.strptime(text, fmt)


def floor_to_hour(dt: datetime) -> datetime:
    """분/초를 0으로 만들어 시(hour) 단위로 내림."""
    return dt.replace(minute=0, second=0, microsecond=0)
