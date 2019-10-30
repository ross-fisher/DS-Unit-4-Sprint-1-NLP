import functools

def comp(*funcs):
    def comp2(f, g):
        return lambda x: f(g(x))
    return functools.reduce(comp2, funcs, lambda x: x)
