from __future__ import annotations

__all__: list[str] = ["IaddSeq"]

from typing import TYPE_CHECKING, Protocol, Self, TypeVar

if TYPE_CHECKING:
    from src.seqpad.typing.AddSeq import AddSeq

Other = TypeVar("Other", contravariant=True)


class IaddSeq(Protocol[Other]):
    def __iadd__(
        self: Self,
        other: Other,
        /,
    ) -> AddSeq[Other] | IaddSeq[Other]: ...
    def __len__(self: Self, /) -> int: ...
