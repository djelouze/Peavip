
# List xml description of filters
SET( FILTERS_XML 
./Filters/GaussianSplatter.xml
./Filters/ImageCast.xml
./Filters/ImageChangeInformation.xml
./Filters/ImageConstantPad.xml
./Filters/ImageDivergence.xml
./Filters/ImageDotProduct.xml
./Filters/ImageExtractComponents.xml
./Filters/ImageFFT.xml
./Filters/ImageFourierCenter.xml
./Filters/ImageRFFT.xml
./Filters/ImageFlip.xml
./Filters/ImageGaussianSmooth.xml
./Filters/ImageMagnitude.xml
./Filters/ImageMathematics.xml
./Filters/ImageMirrorPad.xml
./Filters/ImageNormalize.xml
./Filters/ImagePermute.xml
./Filters/ImageResample.xml
./Filters/ImageReslice.xml
./Filters/ImageShiftScale.xml
./Filters/ImageSobel3D.xml
./Filters/ImageStencil.xml
./Filters/ImageThreshold.xml
./Filters/ImageWrapPad.xml
./Filters/InterpolateDataSetAttributes.xml
./Filters/ProbeFilter.xml
./Filters/RuledSurfaceFilter.xml
./Filters/SplineFilter.xml
./Filters/TensorGlyph.xml
./Filters/WindowedSincPolyDataFilter.xml
./Filters/BoostKruskalMinimumSpanningTree.xml
./Filters/BoostPrimMinimumSpanningTree.xml
./Filters/VertexDegree.xml
./Filters/PruneTreeFilter.xml
./Filters/TreeLevelsFilter.xml
./Filters/StrahlerMetric.xml
./Filters/GraphToPolyData.xml
)

# Create target that will contain all the listed VTK filter
ADD_PARAVIEW_PLUGIN(
  PeavipFilters "1.0"
  SERVER_MANAGER_XML ${FILTERS_XML}  
  GUI_RESOURCE_FILES PeavipFilterMenu.xml
)

# List xml descriptions of VTK sources
SET( SOURCES_XML 
./Sources/ImageGaussianSource.xml
./Sources/PlatonicSolidSource.xml
)


# Create target that will contain all the listed VTK sources
ADD_PARAVIEW_PLUGIN(PeavipSources "1.0"
  SERVER_MANAGER_XML ${SOURCES_XML}  )

