from __future__ import annotations

from typing import List, Any, Callable

ATTRIBUTE = "values"


class ReservedAttributeError(ValueError):
    """Reserved attribute used in `Enum`-definition."""

    attribute = ATTRIBUTE

    def __init__(self, class_name: str, metaclass_name: str) -> None:
        message = (
            f"Class {class_name!r} implements `{ReservedAttributeError.attribute}` "
            f"which is a reserved attribute in {metaclass_name!r}. "
            f"Use any other attribute name instead."
        )
        super().__init__(message)


class EnumMeta(type):
    """Metaclass to ensure `.values` functionality in `Enum`."""

    def __new__(mcs, name: str, bases: tuple, dct: dict) -> EnumMeta:
        """Check if the reserved attribute has been used."""

        if ReservedAttributeError.attribute in dct:
            raise ReservedAttributeError(class_name=name, metaclass_name=mcs.__name__)

        return super().__new__(mcs, name, bases, dct)

    @property
    def values(self) -> Callable[[], List[str]]:
        """All public values from `self` (ignores private or protected values)."""
        return lambda: list(v for k, v in self.__dict__.items() if not k.startswith("_"))

    @values.setter
    def values(self, value: Any) -> None:
        """Raise `ReservedAttributeError` for `self` regardless of `value`."""
        raise_reserved_attribute_error(self)

    @values.deleter
    def values(self) -> None:
        """Raise `ReservedAttributeError` for `self`."""
        raise_reserved_attribute_error(self)


class Enum(metaclass=EnumMeta):
    """Base Enum class hiding the EnumMeta class.

    Usage:

    .. code-block:: python

        from eofw_utilities.enum import Enum

        class ExampleEnum(Enum)
            KEY_ONE = "value_1"
            KEY_TWO = "value_2"

        print(Example.KEY_ONE)
        print(Example.values())

    """
    pass


def raise_reserved_attribute_error(instance) -> None:
    """Raise `ReservedAttributeError` for `instance`."""
    class_name = type(instance).__name__
    metaclass_name = EnumMeta.__name__
    raise ReservedAttributeError(class_name=class_name, metaclass_name=metaclass_name)
