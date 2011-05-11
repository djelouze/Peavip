try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()


src = ImageGaussianSource()
rep = Show()
Render()

