## trace generated using paraview version 5.10.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
import os
root = os.getcwd()
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
casefoam = OpenFOAMReader(registrationName='case.foam', FileName=f"{root}/case.foam")
casefoam.MeshRegions = ['internalMesh']
casefoam.CellArrays = ['U', 'cellDist', 'k', 'p']
casefoam.Decomposepolyhedra = 0

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get the material library
materialLibrary1 = GetMaterialLibrary()

# get display properties
casefoamDisplay = GetDisplayProperties(casefoam, view=renderView1)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# set scalar coloring
ColorBy(casefoamDisplay, ('CELLS', 'cellDist'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
casefoamDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
casefoamDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'cellDist'
cellDistLUT = GetColorTransferFunction('cellDist')

# get opacity transfer function/opacity map for 'cellDist'
cellDistPWF = GetOpacityTransferFunction('cellDist')

# change representation type
casefoamDisplay.SetRepresentationType('Surface With Edges')

# Properties modified on casefoamDisplay
casefoamDisplay.EdgeColor = [1.0, 1.0, 1.0]

# create a new 'OpenFOAMReader'
casefoam_1 = OpenFOAMReader(registrationName='case.foam', FileName=f"{root}/case.foam")
casefoam_1.MeshRegions = ['internalMesh']
casefoam_1.CellArrays = ['U', 'cellDist', 'k', 'p']
casefoam_1.Decomposepolyhedra = 0

# show data in view
casefoam_1Display = Show(casefoam_1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
casefoam_1Display.Representation = 'Surface'
casefoam_1Display.ColorArrayName = ['POINTS', 'p']
casefoam_1Display.LookupTable = pLUT
casefoam_1Display.SelectTCoordArray = 'None'
casefoam_1Display.SelectNormalArray = 'None'
casefoam_1Display.SelectTangentArray = 'None'
casefoam_1Display.OSPRayScaleArray = 'p'
casefoam_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
casefoam_1Display.SelectOrientationVectors = 'U'
casefoam_1Display.ScaleFactor = 0.010000000149011612
casefoam_1Display.SelectScaleArray = 'p'
casefoam_1Display.GlyphType = 'Arrow'
casefoam_1Display.GlyphTableIndexArray = 'p'
casefoam_1Display.GaussianRadius = 0.0005000000074505806
casefoam_1Display.SetScaleArray = ['POINTS', 'p']
casefoam_1Display.ScaleTransferFunction = 'PiecewiseFunction'
casefoam_1Display.OpacityArray = ['POINTS', 'p']
casefoam_1Display.OpacityTransferFunction = 'PiecewiseFunction'
casefoam_1Display.DataAxesGrid = 'GridAxesRepresentation'
casefoam_1Display.PolarAxes = 'PolarAxesRepresentation'
casefoam_1Display.ScalarOpacityFunction = pPWF
casefoam_1Display.ScalarOpacityUnitDistance = 0.01924175606617764
casefoam_1Display.OpacityArrayName = ['POINTS', 'p']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
casefoam_1Display.ScaleTransferFunction.Points = [-71.01607513427734, 0.0, 0.5, 0.0, 21.268600463867188, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
casefoam_1Display.OpacityTransferFunction.Points = [-71.01607513427734, 0.0, 0.5, 0.0, 21.268600463867188, 1.0, 0.5, 0.0]

# show color bar/color legend
casefoam_1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Transform'
transform1 = Transform(registrationName='Transform1', Input=casefoam_1)
transform1.Transform = 'Transform'

# show data in view
transform1Display = Show(transform1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
transform1Display.Representation = 'Surface'
transform1Display.ColorArrayName = ['POINTS', 'p']
transform1Display.LookupTable = pLUT
transform1Display.SelectTCoordArray = 'None'
transform1Display.SelectNormalArray = 'None'
transform1Display.SelectTangentArray = 'None'
transform1Display.OSPRayScaleArray = 'p'
transform1Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform1Display.SelectOrientationVectors = 'U'
transform1Display.ScaleFactor = 0.010000000149011612
transform1Display.SelectScaleArray = 'p'
transform1Display.GlyphType = 'Arrow'
transform1Display.GlyphTableIndexArray = 'p'
transform1Display.GaussianRadius = 0.0005000000074505806
transform1Display.SetScaleArray = ['POINTS', 'p']
transform1Display.ScaleTransferFunction = 'PiecewiseFunction'
transform1Display.OpacityArray = ['POINTS', 'p']
transform1Display.OpacityTransferFunction = 'PiecewiseFunction'
transform1Display.DataAxesGrid = 'GridAxesRepresentation'
transform1Display.PolarAxes = 'PolarAxesRepresentation'
transform1Display.ScalarOpacityFunction = pPWF
transform1Display.ScalarOpacityUnitDistance = 0.01924175606617764
transform1Display.OpacityArrayName = ['POINTS', 'p']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform1Display.ScaleTransferFunction.Points = [-71.01607513427734, 0.0, 0.5, 0.0, 21.268600463867188, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform1Display.OpacityTransferFunction.Points = [-71.01607513427734, 0.0, 0.5, 0.0, 21.268600463867188, 1.0, 0.5, 0.0]

# hide data in view
Hide(casefoam_1, renderView1)

# show color bar/color legend
transform1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Translate = [0.105, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# set scalar coloring
ColorBy(transform1Display, ('CELLS', 'k'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
transform1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
transform1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'k'
kLUT = GetColorTransferFunction('k')

# get opacity transfer function/opacity map for 'k'
kPWF = GetOpacityTransferFunction('k')

# change representation type
transform1Display.SetRepresentationType('Surface With Edges')

# Properties modified on transform1Display
transform1Display.EdgeColor = [1.0, 1.0, 1.0]

# get color legend/bar for kLUT in view renderView1
kLUTColorBar = GetScalarBar(kLUT, renderView1)

# Properties modified on kLUTColorBar
kLUTColorBar.RangeLabelFormat = '%-#6.1f'

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
kLUT.ApplyPreset('Viridis (matplotlib)', True)


# get color legend/bar for cellDistLUT in view renderView1
cellDistLUTColorBar = GetScalarBar(cellDistLUT, renderView1)

# change scalar bar placement
cellDistLUTColorBar.WindowLocation = 'Any Location'
cellDistLUTColorBar.Position = [0.7515723270440252, 0.26607818411097095]
cellDistLUTColorBar.ScalarBarLength = 0.33000000000000007

# change scalar bar placement
kLUTColorBar.WindowLocation = 'Any Location'
kLUTColorBar.Position = [0.7578616352201258, 0.6406052963430012]
kLUTColorBar.ScalarBarLength = 0.33000000000000007

# set active source
SetActiveSource(casefoam)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
cellDistLUT.ApplyPreset('Cold and Hot', True)

# Properties modified on cellDistLUT
cellDistLUT.IndexedColors = [0.8941176470588236, 0.10196078431372549, 0.10980392156862745, 0.21568627450980393, 0.49411764705882355, 0.7215686274509804, 0.30196078431372547, 0.6862745098039216, 0.2901960784313726, 0.596078431372549, 0.3058823529411765, 0.6392156862745098]

# Properties modified on cellDistLUT
cellDistLUT.RescaleOnVisibilityChange = 1

# change scalar bar placement
cellDistLUTColorBar.Position = [0.7584905660377359, 0.27616645649432536]

# change scalar bar placement
kLUTColorBar.Position = [0.7515723270440252, 0.6406052963430012]

# change scalar bar placement
cellDistLUTColorBar.Position = [0.7522012578616353, 0.27616645649432536]

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# set active source
SetActiveSource(transform1)

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1590, 793)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.1379609587147451, 0.03230053969018198, 0.27888724573938806]
renderView1.CameraFocalPoint = [0.1379609587147451, 0.03230053969018198, 0.004999999888241291]
renderView1.CameraParallelScale = 0.07088723543695315

# save screenshot
SaveScreenshot(f"{root}/krandom.png", renderView1, ImageResolution=[1590, 793],
    TransparentBackground=1, 
    # PNG options
    CompressionLevel='3')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1590, 793)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.1379609587147451, 0.03230053969018198, 0.27888724573938806]
renderView1.CameraFocalPoint = [0.1379609587147451, 0.03230053969018198, 0.004999999888241291]
renderView1.CameraParallelScale = 0.07088723543695315

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...). alternatively, if you want to write images, you can use SaveScreenshot(...). alternatively, if you want to write images, you can use SaveScreenshot(...). alternatively, if you want to write images, you can use SaveScreenshot(...).
