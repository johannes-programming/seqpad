from __future__ import annotations

__all__: list[str] = ["AddSeq"]

from typing import TYPE_CHECKING, Protocol, Self, TypeVar

if TYPE_CHECKING:
    from seqpad.typing.IaddSeq import IaddSeq

Other = TypeVar("Other", contravariant=True)


class AddSeq(Protocol[Other]):
    def __add__(
        self: Self,
        other: Other,
        /,
    ) -> AddSeq[Other] | IaddSeq[Other]: ...
    def __hash__(self:Self, /) -> int: ...
    def __len__(self: Self, /) -> int: ...
