from items import *
from location import rooms

Player={
  "name":"Doc",
  "current_room":rooms["Office 1"],
  "inventory":[item_knife],
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

Players={
  "Doc":Player,
  "Hannibal the cannibal":Cannibal
}
