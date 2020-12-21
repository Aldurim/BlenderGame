import bge
path = bge.logic.expandPath("//")
path = path + "saves/"
#Identify the object running this script
control = bge.logic.getCurrentController()
ray  = control.owner.sensors[0]     #RaySensor
curScene = bge.logic.getCurrentScene()  #speichert die momentane Scene in curScene
scenes = bge.logic.getSceneList()
for i in scenes:
    if i.name == "overlay":
        overlay = i
        
if ray.hitObject:
    overlay.objects['DisplayText']['Text'] = ray.hitObject["NAME"]#.name.replace("ITEM_","") #zeigt den Namen des Items an worauf der Spierler schaut
    for key,status in control.owner.sensors[1].events:  #Keybiardsensor
        # key[0] == bge.events.keycode, key[1] = status
        if status == bge.logic.KX_INPUT_JUST_ACTIVATED:
            if key == bge.events.EKEY:
                #Eventhandler für Items:
                #Updatet das tempfile für Items. D.h das Item wird als gelöscht für die Szene
                #gespeichert, da es von dem spieler entwendet wurde
                #später soll dann das item im inventar file gespeichert werden
                if "ITEM" in ray.hitObject.name:
                    tempfile = open(path + curScene.name + "/temp_items", "r")
                    tempItems = tempfile.readlines()
                    tempfile.close()
                    tempfile = open(path + curScene.name + "/temp_items", "w")
                    for i in tempItems:
                        if ray.hitObject.name in i:
                            tempfile.write(ray.hitObject.name + ",0\n")
                        else:
                            tempfile.write(i)
                    tempfile.close()
                    ray.hitObject.endObject()
                    
                if "DOOR" in ray.hitObject.name:
                    tempfile = open(path + curScene.name + "/temp_doors", "r")
                    tempItems = tempfile.readlines()
                    tempfile.close()
                    tempfile = open(path + curScene.name + "/temp_doors", "w")
                    for i in tempItems:
                        if ray.hitObject.name in i:
                            ray.hitObject["OPEN"] = (ray.hitObject["OPEN"] + 1) % 2
                            tempfile.write(ray.hitObject.name + "," + str(ray.hitObject["OPEN"])+ "," +str(ray.hitObject["LOCKED"])+"\n")
                        else:
                            tempfile.write(i)
                    tempfile.close()
                    
else:
    overlay.objects['DisplayText']['Text'] = ""
