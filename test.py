from compose import compose, acompose, sacompose


def f(i: int) -> float:
    return float(i)


def g(f: float) -> str:
    return str(f)


def h(s: str) -> int:
    return int(s)


def x(f: float, x: str | None = None) -> str:
    return str(f) + str(x)


v1: float = compose(f)(1)
v2: str = compose(g, f)(1)
v3: int = compose(h, g, f)(1)
v4: float = compose(f, h, g, f)(1)
v5: str = compose(g, f, h, g, f)(1)
v6: int = compose(h, g, f, h, g, f)(1)
v7: str = compose(x, f)(1)


async def af(i: int) -> float:
    return float(i)


async def ag(f: float) -> str:
    return str(f)


async def ah(s: str) -> int:
    return int(s)


async def ax(f: float, x: str | None = None) -> str:
    return str(f) + str(x)


async def a() -> None:
    v1: float = await acompose(f)(1)
    v2: str = await acompose(g, f)(1)
    v3: int = await acompose(h, g, f)(1)
    v4: float = await acompose(f, h, g, f)(1)
    v5: str = await acompose(g, f, h, g, f)(1)
    v6: int = await acompose(h, g, f, h, g, f)(1)
    v7: str = await acompose(x, f)(1)

    s1: float = await acompose(af)(1)
    s2: str = await acompose(g, af)(1)
    s3: int = await acompose(h, ag, af)(1)
    s4: float = await acompose(af, h, ag, f)(1)
    s5: str = await acompose(ag, f, ah, g, af)(1)
    s6: int = await acompose(ah, g, af, h, ag, f)(1)
    s7: str = await acompose(ax, f)(1)


async def sa() -> None:
    v1: float = sacompose(f)(1)
    v2: str = sacompose(g, f)(1)
    v3: int = sacompose(h, g, f)(1)
    v4: float = sacompose(f, h, g, f)(1)
    v5: str = sacompose(g, f, h, g, f)(1)
    v6: int = sacompose(h, g, f, h, g, f)(1)
    v7: str = sacompose(x, f)(1)

    s1: float = await sacompose(af)(1)
    s2: str = await sacompose(g, af)(1)
    s3: int = await sacompose(h, ag, af)(1)
    s4: float = await sacompose(af, h, ag, f)(1)
    s5: str = await sacompose(ag, f, ah, g, af)(1)
    s6: int = await sacompose(ah, g, af, h, ag, f)(1)
    s7: str = await sacompose(ax, f)(1)
