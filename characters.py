from items import *
from location import rooms
#We have to put an actual name for each patient, cant leave it as patient and a number

Player={
  "name":"Doc",
  "current_room":rooms["Office 1"],
  "inventory":[],
  "alive": True,
  "escape": False,
  "invent_weight":0
}
Cannibal={
  "name":"Hannibal the cannibal",
  "current_room":rooms["Room 666"],
  "inventory":[],
  "file":"",
  "alive":True
}
Leeroy_Jenkins={
  "name":"Leerooooooooy Jenkiiiiiiins",
  "patient_no": "420",
  "current_room":rooms["Office 1"],
  "inventory":[],
  "history":"The one and only. The mighty. No need to say more.",
  "reason_for_imprisonment": "Failed to obey the guild master's orders. Got the whole group killed",
  "file":"",
  "alive": True
}
Patient_483={
  "name":"Patient 483",
  "current_room":rooms["Office 1"],
  "inventory":[],
  "file":"",
  "alive": True
  }
Patient_645={
  "name":"Patient 645",
  "current_room":rooms["Office 1"],
  "inventory":[],
  "file":"",
  "alive": True
  }
Patient_234={
  "name":"Patient 234",
  "current_room":rooms["Office 1"],
  "inventory":[],
  "file":"",
  "alive": True
}
Patient_251={
  "name":"Sarah Connor",
  "current_room":rooms["Office 1"],
  "inventory":[],
  "file":"Crazy woman that thinks robots are going to take over the world.",
  "alive": True
}
Patient_347={
  "name":"Patient 347",
  "current_room":rooms["Office 1"],
  "inventory":[],
  "file":"",
  "alive": True
}
Players={
  "Doc":Player,
  "Hannibal the cannibal":Cannibal,
  "Patient 483":Patient_483,
  "Patient 645":Patient_645,
  "Patient 234":Patient_234,
  "Patient 251":Patient_251,
  "Patient 347":Patient_347
}
