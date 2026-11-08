from __future__ import annotations

__all__: list[str] = ["SizedAndSupportsAdd"]

from typing import Protocol, Self, TypeVar

Other = TypeVar("Other", contravariant=True)


class SizedAndSupportsAdd(Protocol[Other]):
    def __add__(self: Self, other: Other, /) -> Self: ...
    def __len__(self: Self, /) -> int: ...
