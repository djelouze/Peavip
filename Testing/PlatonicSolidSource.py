try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()


src = PlatonicSolidSource()
rep = Show()
Render()

