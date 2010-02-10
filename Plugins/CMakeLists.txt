
# List xml description of filters
SET( FILTERS_XML 
./Filters/ImageCast.xml
./Filters/ImageDivergence.xml
./Filters/ImageExtractComponents.xml
./Filters/ImageFFT.xml
./Filters/ImageRFFT.xml
./Filters/ImageFlip.xml
./Filters/ImageGaussianSmooth.xml
./Filters/ImageMagnitude.xml
./Filters/ImageMathematics.xml
./Filters/ImageResample.xml
./Filters/ImageReslice.xml
./Filters/ImageShiftScale.xml
./Filters/ImageSobel3D.xml
./Filters/ImageStencil.xml
./Filters/ImageThreshold.xml
./Filters/ProbeFilter.xml
./Filters/SplineFilter.xml
./Filters/TensorGlyph.xml
)

# Create target that will contain all the listed VTK filter
ADD_PARAVIEW_PLUGIN(PeavipFilters "1.0"
  SERVER_MANAGER_XML ${FILTERS_XML}  )

# List xml descriptions of VTK sources
SET( SOURCES_XML 
./Sources/ImageGaussianSource.xml
./Sources/PlatonicSolidSource.xml
)


# Create target that will contain all the listed VTK sources
ADD_PARAVIEW_PLUGIN(PeavipSources "1.0"
  SERVER_MANAGER_XML ${SOURCES_XML}  )

