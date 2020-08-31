# SFSymbolsTo3DObj
Convert Apple's SF Symbol SVG Icons to 3D obj files using Blender

## Motivation
Rendering 3D cascading effects with SF Symbols in SceneKit

Input Apple's SF Symbol SVG file

![](/misc/gyroscopesvg.png)

Output 3D Obj model file

![](/misc/gyroscopeobj.png)

## Instructions
### Install Blender and locate your Blender exacutable
Download and install Blender https://www.blender.org/download/

On Mac, from the Applications folder, its `/Applications/Blender.app/Contents/MacOS/Blender`

### Run the following command
`/Path_TO/Blender -b --python /PATH/blender.py -- /PATH_TO/svg/ /PATH_TO/models/`

* `/Path_TO/Blender` is the Blender executable path
* `/PATH/blender.py` is the Blender python script
* `/PATH_TO/svg/` is the SF Symbol SVG input directory
* `/PATH_TO/models/` is the output Obj models directory

On Mac:

`/Applications/Blender.app/Contents/MacOS/Blender -b --python /blender.py -- /svg/ /models/`
