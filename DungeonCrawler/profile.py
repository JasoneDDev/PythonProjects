# use this as a decorator to profile a function
# @profileMe

import cProfile

def profileMe(fn):
    def profiled_fn(*args, **kwargs):
        # name for profile dump
        fpath = fn.__name__ + '.profile'
        prof = cProfile.Profile()
        ret = prof.runcall(fn, *args, **kwargs)
        prof.dump_stats(fpath)
        return ret
    return profiled_fn    