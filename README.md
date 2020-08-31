# SFSymbolsTo3DObj
Convert Apple's SF Symbol SVG Icons to 3D obj files using Blender

## Motivation
Rendering 3D cascading effects with SF Symbols in SceneKit

Input Apple's SF Symbol SVG file:

![](/misc/gyroscopesvg.png)

Output 3D Obj model file:

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

On Mac, from inside the repository directory:

`/Applications/Blender.app/Contents/MacOS/Blender -b --python /blender.py -- /svg/ /models/`

Output of one transformation call:

```
Info: Deleted 1 object(s)
/Users/jefhai/Documents/git/SFSymbolsTo3D/svg/smallcircle.circle.fill.svg
Info: Deleted 47 object(s)
    (  0.0001 sec |   0.0000 sec) OBJ Export path: '/Users/jefhai/Documents/git/SFSymbolsTo3D/models/smallcircle.circle.fill.obj'
    (  0.0125 sec |   0.0119 sec) Finished writing geometry of 'Curve.039'.
    (  0.0141 sec |   0.0137 sec) Finished exporting geometry, now exporting materials
NO NODES! 100.00%
    (  0.0151 sec |   0.0147 sec) OBJ Export Finished
Progress: 100.00%
```

## Licensing & Legal
Disclaimer: I am not the owner nor copyright holder of these files. Apple provides a licensing mechanism to App Store developers to modify and use advance rendering techiniques for their SF Symbol fonts and icons.

Follow Apple's human interface guidelines, terms and licensing!
* https://developer.apple.com/design/human-interface-guidelines/sf-symbols/overview/
* https://developer.apple.com/terms/
