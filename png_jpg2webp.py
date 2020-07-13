'''
    breif   :   将png jpg格式转为webp格式
    history :   renbin.guo created 20200713
    note    :   ref:https://developers.google.com/speed/webp/docs/using
                使用时按先修改imgPath  toolPath outputPath 三个路径自己的
'''

import os
imgPath = r'F:\git_code\modelUploaderFrontend\src\assets\images\imgOrigan\\'
toolPath = r"F:\git_code\task_record\png2webp\libwebp-1.1.0-windows-x64\bin\\"
outputPath = r"F:\git_code\modelUploaderFrontend\src\assets\images\imgWebp\\"
filenames = os.listdir( imgPath )
print(filenames)
print("\n\n转换开始....")
for filename in filenames:
    cmdStr = toolPath+'cwebp.exe'+'  '+imgPath+filename+'  -o  '+  outputPath+filename[0:-4]+'.webp'
    print(cmdStr)
    print("\n")
    os.system(cmdStr)
print("\n\n转换结束....")
