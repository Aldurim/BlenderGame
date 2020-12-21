import bge
import os
path = bge.logic.expandPath("//")
path = path + "saves/"
scenes = bge.logic.getSceneList()
dirList = os.listdir(path)
curScene = bge.logic.getCurrentScene()
for i in dirList:
    if os.path.isdir(path + i + "/"):
        fileList = os.listdir(path + i+"/")
        for j in fileList:
            if "temp_" in j:
                os.system("rm " + path + i + "/" + j)

#für sauberkeit, entferne alle scenes bis auf das menu
scenes = bge.logic.getSceneList()
for i in scenes:
    if i.name != curScene.name:
        i.end() 
