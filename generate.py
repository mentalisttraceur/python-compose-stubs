#!/usr/bin/env python3

arguments = 'f1: Callable[P, R1], /'
overloads = [f'def compose({arguments}) -> Callable[P, R1]']

for number in range(2, 256):
    arguments = f'f{number}: Callable[[R{number-1}], R{number}], {arguments}'
    overloads.append(f'def compose({arguments}) -> Callable[P, R{number}]')

print('from typing import Callable, ParamSpec, TypeVar, overload')
print("P = ParamSpec('P')")

for number in range(1, 256):
    print(f"R{number} = TypeVar('R{number}')")

for signature in overloads:
    print('@overload')
    print(f'{signature}:')
    print('    ...')
