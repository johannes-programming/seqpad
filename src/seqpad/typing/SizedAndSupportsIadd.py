from __future__ import annotations

__all__: list[str] = ["SizedAndSupportsIadd"]

from typing import Protocol, Self, TypeVar

Other = TypeVar("Other", contravariant=True)


class SizedAndSupportsIadd(Protocol[Other]):
    def __iadd__(self: Self, other: Other, /) -> Self: ...
    def __len__(self: Self, /) -> int: ...
