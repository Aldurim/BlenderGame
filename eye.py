import bge

#Identify the object running this script
control = bge.logic.getCurrentController()
ray  = control.owner.sensors[0]

scenes = bge.logic.getSceneList()
for i in scenes:
    if i.name == "Overlay":
        overlay = i
        
if ray.hitObject:
    overlay.objects['DisplayText']['Text'] = ray.hitObject.name.replace("ITEM_","")
    for key,status in control.owner.sensors[1].events:
        # key[0] == bge.events.keycode, key[1] = status
        if status == bge.logic.KX_INPUT_JUST_ACTIVATED:
            if key == bge.events.EKEY:
                ray.hitObject.endObject()
else:
    overlay.objects['DisplayText']['Text'] = ""
