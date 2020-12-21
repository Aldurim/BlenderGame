import bge
import os
path = bge.logic.expandPath("//")
path = path + "saves/"

scenes = bge.logic.getSceneList()
curScene = bge.logic.getCurrentScene()
control = bge.logic.getCurrentController()
scene  = control.actuators['set']
mouse = control.actuators['Mouse']

#für sauberkeit, entferne alle scenes bis auf das menu
scenes = bge.logic.getSceneList()
for i in scenes:
    if i.name != curScene.name:
        i.end()
        
#für sauberkeit entferne alle tempfiles
dirList = os.listdir(path)
for i in dirList:
    if os.path.isdir(path + i + "/"):
        fileList = os.listdir(path + i+"/")
        for j in fileList:
            if "temp_" in j:
                os.system("rm " + path + i + "/" + j)

if os.path.isfile(path + "player"):
    file = open(path + "player")
    data = file.readline()
    file.close()
    
    data = data.replace("\n","")
    scene.scene = data
    mouse.visible = False
    control.activate(mouse)
    control.activate(scene)
    file = open(path+"LOAD","w+")
    file.write("True")
    file.close() 
    #alle anderen Daten werden in dem initSzene geladen
         
