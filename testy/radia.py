def radiationExposure(start, stop, step):
    if stop - start <= 0:
        return 0
    else:
        return step*f(start)+ radiationExposure(start+step,stop,step)
