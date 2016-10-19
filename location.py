from maps import *
from items import *
from file import *

room_Office1={
	"name":"Office 1",
	"description":
    """Your office is small with a chair by your desk and a bench against the wall.
There is a door to the east leading to Room 483.""",
	"items":[],
	"items_hidden":[],
	"searched":False,
	"exits":{"east":"Room 483"},
	"map":[maps["Office 1 map"],mapsON["Office 1 map"]]
}
room_Office2={
	"name":"Office 2",
	"description":
    """This office is big and has a number of portraits hanging on the walls.
A desk sits in the middle. There is a phone hanging on the wall and under closer
inspection it still works. Other than that the room is bare.""",
	"items":[],
	"items_hidden":[],
	"searched":False,
	"exits":{"north":"Emergency room","south":"Canteen","east":"The yard","west":"Therapy room"},
	"map":[maps["Office 2 map"],mapsON["Office 2 map"]]	
}
room_Reception={
	"name":"Reception",
	"description":
    """The reception is more like an extension of the hall. There are two
chairs behind the desk and files litter both the floor and workspace.
You would offer to help clean but there is no one around.""",
	"items":[],
	"items_hidden":[],
	"searched":False,
	"exits":{"south":"Room 123","west":"Emergency room"},
	"map":[maps["Reception map"],mapsON["Reception map"]]
}
room_Therapy={
	"name":"Therapy room",
	"description":
    """You force open the door which smashes against the wall, you are blinded by a beaming light shining directly in your face. 
You see a large settee and an old oak desk in the centre of the room.
The window flies open blowing paper from the desk all over the room.
""",
	"items":[],
	"items_hidden":[],
	"searched":False,
	"exits":{"east":"Office 2","south":"Room 483"},
	"map":[maps["Therapy room map"],mapsON["Therapy room map"]]
}
room_Canteen={
	"name":"Canteen",
	"description":
    """You open up two large doors to a massive room with a cluster of long tables,
    after walking further into the pasty white room you realise this is the canteen.
    Apart from a few crooked pictures on the walls the room is esentially bare,
    you can see utensils on the surface of the table and a dinner tray covered in what looks like some sort of flesh""",
	"items":[],
	"items_hidden":[item_knife],
	"searched":False,
	"exits":{"west":"Room 483","south":"Room 234","east":"Room 251","north":"Office 2"},
	"map":[maps["Canteen map"],mapsON["Canteen map"]]
}
room_666={
	"name":"Room 666",
	"description":
    """You open the cell door to a fairly small bare cell,
as you start to walk in you realise the walls are covered in blood, spelling out ‘I’m
coming for you’, you see a body like shape in the bed.""",
	"items":[],
	"items_hidden":[],
	"searched":False,
	"exits":{"north":"Room 234","east":"Room 696"},
	"map":[maps["Room 666 map"],mapsON["Room 666 map"]],
	"file":file_list["room 666"]
}
room_ER={
	"name":"Emergency room",
	"description":
    """The emergency room is pretty empty, as it had been sacked. You can see on a table some cameras
and a tablet. There's a switch on the wall with an unclear label, it seems like it will have some 
effect on the locked doors.""",
	"items":[],
	"items_hidden":[],
	"searched":False,
	"exits":{"south":"Office 2"},
	"map":[maps["Emergency room map"],mapsON["Emergency room map"]],
	"switch":False
}
room_Yard={
	"name":"The yard",
	"description":
    """You charge through the doors and stumble into a large stone courtyard with a vine covered
fountain in the middle, you look around and see nothing but a small gate blown open, 
you hear the faint sounds of sirens in the distance.""",
	"items":[],
	"items_hidden":[],
	"searched":False,
	"exits":{"west":"Office 2","south":"Room 251"},
	"map":[maps["The yard map"],mapsON["The yard map"]]
}
room_483={
	"name":"Room 483",
	"description":
    """You open the door, you are greeted by a foul smell,
as you inspect the room you see a large bed in the middle of the room and a small bag in the corner covered with flies.
""",
	"items":[],
	"items_hidden":[],
	"searched":False,
	"exits":{"north":"Therapy room","west":"Office 1","south":"Room 645","east":"Canteen"},
	"map":[maps["Room 483 map"],mapsON["Room 483 map"]],
	"file":file_list["room 483"]
}
room_645={
	"name":"Room 645",
	"description":
    """You enter cell 645 and you see a small note hanging on the wall, apart from that the room is entirely bare.""",
	"items":[],
	"items_hidden":[],
	"searched":False,
	"exits":{"north":"Room 483","east":"Room 234"},
	"map":[maps["Room 645 map"],mapsON["Room 645 map"]],
	"file":file_list["room 645"]
}
room_234={
	"name":"Room 234",
	"description":
    """You see an open door after walking into the room it resembles cell 666, you see a double
bed pushed tightly against the corner. There appears to be some kind of liquid on the floor.""",
	"items":[],
	"items_hidden":[],
	"searched":False,
	"exits":{"north":"Canteen","south":"Room 666","east":"Room 347","west":"Room 645"},
	"map":[maps["Room 234 map"],mapsON["Room 234 map"]],
	"file":file_list["room 234"]
}
room_123={
	"name":"Room 123",
	"description":
    """The door is clean off its hinges, you slowly start to creep into the room and see a pile
of doctors notes spread across the bed, your file is on top and opened.""",
	"items":[],
	"items_hidden":[],
	"searched":False,
	"exits":{"north":"Reception"},
	"map":[maps["Room 123 map"],mapsON["Room 123 map"]],
	"file":file_list["room 123"]
}
room_251={
	"name":"Room 251",
	"description":
    """The door is open but the lock appears to be intact.
As you walk in you see a small bed that has been pushed into the centre of the room and a small silver toilet is in the corner.""",
	"items":[],
	"items_hidden":[],
	"searched":False,
	"exits":{"north":"The yard","south":"Room 347","east":"Reception","west":"Canteen"},
	"map":[maps["Room 251 map"],mapsON["Room 251 map"]],
	"file":file_list["room 251"]
}
room_347={
	"name":"Room 347",
	"description":
    """You enter cell 347 and see an inmate’s gown hung up on the wall covered in blood.
There is a large bed in the centre of the room. """,
	"items":[],
	"items_hidden":[],
	"searched":False,
	"exits":{"north":"Room 251","east":"Room 123","west":"Room 234","south":"Room 696"},
	"map":[maps["Room 347 map"],mapsON["Room 347 map"]],
	"file":file_list["room 347"]
}
room_696={
	"name":"Room 696",
	"description":
    """You try to open the door but it appears to be stuck you smash into it and it falls onto the floor giving out a huge bang. 
You get up and see a large metal sink in the corner of the room with a glowing red liquid flowing down onto the floor.
""",
	"items":[],
	"items_hidden":[],
	"searched":False,
	"exits":{"north":"Room 347","west":"Room 666"},
	"map":[maps["Room 696 map"],mapsON["Room 696 map"]],
	"file":file_list["room 696"]
}
rooms={
	"Office 1":room_Office1,
	"Office 2":room_Office2,
	"Reception":room_Reception,
	"Therapy room":room_Therapy,
	"Canteen":room_Canteen,
	"Room 666":room_666,
	"Emergency room":room_ER,
	"The yard":room_Yard,
	"Room 483":room_483,
	"Room 645":room_645,
	"Room 234":room_234,
	"Room 123":room_123,
	"Room 347":room_347,
	"Room 251":room_251,
	"Room 696":room_696
}
lockedRooms={
	"Canteeneast":"Room 483west",
	"Canteensouth":"Room 234north",
	"Canteenwest":"Room 251east",
}
