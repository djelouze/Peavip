try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

import os,sys
sys.path.append(os.getcwd())

import ImageGaussianSource
import ImageEllipsoidSource
import PlatonicSolidSource
