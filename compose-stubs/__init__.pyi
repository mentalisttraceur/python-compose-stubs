from typing import Callable, TypeVar, ParamSpec, overload

P = ParamSpec('P')
R1 = TypeVar('R1')
R2 = TypeVar('R2')
@overload
def compose(f2: Callable[[R1], R2], f1: Callable[P, R1]) -> Callable[P, R2]:
    ...
R3 = TypeVar('R3')
@overload
def compose(f3: Callable[[R2], R3], f2: Callable[[R1], R2], f1: Callable[P, R1]) -> Callable[P, R3]:
    ...
R4 = TypeVar('R4')
@overload
def compose(f4: Callable[[R3], R4], f3: Callable[[R2], R3], f2: Callable[[R1], R2], f1: Callable[P, R1]) -> Callable[P, R4]:
    ...
