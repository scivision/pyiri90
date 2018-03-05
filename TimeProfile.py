#!/usr/bin/env python
from dateutil.parser import parse
from datetime import timedelta
import numpy as np
from matplotlib.pyplot import show

#
import pyiri90, pyiri90.plots

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='IRI90 time profile plot')
    p.add_argument('-t','--trange',help='START STOP STEP (hours) time [UTC]',nargs=3,
                   default=('2012-08-21','2012-08-22',0.25))
    p.add_argument('--alt',help='START STOP STEP altitude [km]',type=float, nargs=3,default=(120,180,20))
    p.add_argument('-c','--latlon',help='geodetic coordinates of simulation',
                   type=float,default=(65,-147.5))
    p.add_argument('--f107',type=float,default=200.)
    p.add_argument('--f107a', type=float,default=200.)
    p.add_argument('--ap', type=int, default=4)
    p.add_argument('--species',help='species to plot',nargs='+',default=('ne'))
    p = p.parse_args()
# %% user parameters
    tlim = (parse(p.trange[0]), parse(p.trange[1]))
    dt = timedelta(hours=p.trange[2]) # timedelta reduces to seconds, etc for sub-hour step size

    altkm = np.arange(*p.alt)
# %% run IRI90 across time
    iono =  pyiri90.timeprofile(tlim, dt, altkm, p.latlon, p.f107, p.f107a, ap=p.ap)
# %% plots
    pyiri90.plots.plottime(iono, p.species)
    show()
