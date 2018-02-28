#!/usr/bin/env python
from dateutil.parser import parse
import numpy as np
from matplotlib.pyplot import show
#
import pyiri90, pyiri90.plots

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('--alt',help='START STOP STEP altitude [km]',type=float, nargs=3, default=(85,500,1.))
    p.add_argument('-t','--time',help='date and time of simulation',default='2012-07-21T12:35')
    p.add_argument('-c','--latlon',help='geodetic coordinates of simulation',default=(65,-147.5),type=float)
    p.add_argument('--f107',type=float,default=200.)
    p.add_argument('--f107a',type=float,default=200.)
    p.add_argument('--ap',type=int,default=4)
    p = p.parse_args()
# %% user parameters
    altkm = np.arange(p.alt[0], p.alt[1], p.alt[2])
    dtime = parse(p.time)
# %% run IRI90 across altitude
    iono =  pyiri90.runiri(dtime,altkm,p.latlon,p.f107, p.f107a, ap=p.ap)
# %% plots
    pyiri90.plots.plotiono(iono,dtime,p.latlon,p.f107,p.f107a,p.ap)
    show()
