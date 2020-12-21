import bge
import os
path = bge.logic.expandPath("//")
path = path + "saves/"
curScene = bge.logic.getCurrentScene()
scenes = bge.logic.getSceneList()   #listet alle aktiven Szenen
dirList = os.listdir(path)

# Speichert Spielervariablen: Position, letzte Szene in der er sich aufgehalten hat, Level, Lebel, etc
for i in scenes:
    if i.name != 'menu' and i.name != 'overlay':
        playerScene = i
        player = playerScene.objects["Spieler"]
        playerPos = player.position
        playerRot = player.worldOrientation.to_euler()
        file = open(path + "player", "w+")
        file.write(playerScene.name + "\n")
        file.write(str(playerPos[0])+","+str(playerPos[1])+","+str(playerPos[2])+"\n")
        file.write(str(playerRot.x)+","+str(playerRot.y)+","+str(playerRot.z)+"\n")
        file.close()
        break

# Speichert Objekte, NPCs, Türen, etc. aus der Welt
# i ist die Szene bzw die Directory
# j ist das tempFile
for i in dirList:
    if os.path.isdir(path + i+"/"):
        fileList = os.listdir(path + i+"/")
        for j in fileList:
            if "temp_" in j:
                file = open(path + i+"/"+j, "r")
                data = file.readlines()
                file.close()
                filename = "/" + j.replace("temp_","")
                file = open(path + i + filename, "w+")
                for k in data:
                    file.write(k)
                file.close()


 
