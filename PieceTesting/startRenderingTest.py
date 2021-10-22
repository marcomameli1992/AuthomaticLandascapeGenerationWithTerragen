import os
import glob

files = glob.glob('../generatedFile/*.tgd')

for index, path in enumerate(files):
    os.system('start cmd /c ""%TERRAGEN_PATH%/tgdcli" -p ' + path +' -hide -exit -r -o C:/Users/mamel/Downloads/Render.%04d.tiff -ox C:/Users/mamel/Downloads/IMAGETYPE.%04d.exr "')
    if index == 0:
        break