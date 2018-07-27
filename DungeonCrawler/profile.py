# use this as a decorator to profile a function
# @profileMe

# use to grab stats...
# import pstats
# p = pstats.Stats('filename here')
# p.sort_stats('time') --- sort by what you want to look at
# p.print_Stats(3) --- 3 for top 3 or however many we need

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
