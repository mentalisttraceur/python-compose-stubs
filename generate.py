#!/usr/bin/env python3


def _sync_callable(parameters, return_):
    return f'Callable[{parameters}, {return_}]'


def _async_callable(parameters, return_):
    return f'Callable[{parameters}, Awaitable[{return_}]]'


def _sync_or_async_callable(parameters, return_):
    return f'Callable[{parameters}, Union[{return_}, Awaitable[{return_}]]]'


def _overload(name, arguments, return_):
    return f'@overload\ndef {name}({arguments}) -> {return_}:\n    ...'


def _overloads(name, callable_, return_):
    argument = callable_('P', 'R1')
    arguments = f'f1: {argument}, /'
    yield _overload(name, arguments, return_('P', 'R1'))
    for number in range(2, 256):
        argument = callable_(f'[R{number-1}]', f'R{number}')
        arguments = f'f{number}: {argument}, {arguments}'
        yield _overload(name, arguments, return_('P', f'R{number}'))
        

print('from typing import'
      + ' Awaitable, Callable, ParamSpec, TypeVar, Union, overload')
print("P = ParamSpec('P')")

for number in range(1, 256):
    print(f"R{number} = TypeVar('R{number}')")

for x in _overloads('compose', _sync_callable, _sync_callable):
    print(x)
for x in _overloads('acompose', _sync_or_async_callable, _async_callable):
    print(x)
for x in _overloads('sacompose', _sync_callable, _sync_callable):
    print(x)
for x in _overloads('sacompose', _sync_or_async_callable, _async_callable):
    print(x)
