room_Office1={
	"name":"Office 1",
	"description":
    """Your office is small with a chair by your desk and a bench against the wall.
There is a door to the east leading to Therapy.""",
	"items":[],
	"exits":{"east":"Room 483"},
	"map":["------------", "|          |", "| OFFICE 1 |", "|          |", "|          |", "---- \------"]
}
room_Office2={
	"name":"Office 2",
	"description":
    """add me""",
	"items":[],
	"exits":{"north":"Emergency room","south":"Canteen","east":"The yard","west":"Therapy room"}	
}
room_Reception={
	"name":"Reception",
	"description":
    """add me""",
	"items":[],
	"exits":{"south":"Room 123","west":"Emergency room"}	
}
room_Therapy={
	"name":"Therapy room",
	"description":
    """add me""",
	"items":[],
	"exits":{"east":"Office 2","south":"Room 483"}	
}
room_Canteen={
	"name":"Canteen",
	"description":
    """add me""",
	"items":[],
	"exits":{"west":"Room 483","south":"Room 234","east":"Room 251","north":"Office 2"}	
}
room_666={
	"name":"Room 666",
	"description":
    """add me""",
	"items":[],
	"exits":{"north":"Room 234","east":"Room 696"}	
}
room_ER={
	"name":"Emergency room",
	"description":
    """add me""",
	"items":[],
	"exits":{"south":"Office 2"}
}
room_Yard={
	"name":"The yard",
	"description":
    """add me""",
	"items":[],
	"exits":{"west":"Office 2","south":"Room 251"}
}
room_483={
	"name":"Room 483",
	"description":
    """add me""",
	"items":[],
	"exits":{"north":"Therapy room","west":"Office 1","south":"Room 645","east":"Canteen"}	
}
room_645={
	"name":"Room 645",
	"description":
    """add me""",
	"items":[],
	"exits":{"north":"Room 483","east":"Room 234"}	
}
room_234={
	"name":"Room 234",
	"description":
    """add me""",
	"items":[],
	"exits":{"north":"Canteen","south":"Room 666","east":"Room 347","west":"Room 645"}	
}
room_123={
	"name":"Room 123",
	"description":
    """add me""",
	"items":[],
	"exits":{"north":"Reception"}	
}
room_251={
	"name":"Room 251",
	"description":
    """add me""",
	"items":[],
	"exits":{"north":"The yard","south":"Room 347","east":"Reception","west":"Canteen"}	
}
room_347={
	"name":"Room 347",
	"description":
    """add me""",
	"items":[],
	"exits":{"north":"Room 251","east":"Room 123","west":"Room 234","south":"Room 696"}	
}
room_696={
	"name":"Room 696",
	"description":
    """add me""",
	"items":[],
	"exits":{"north":"Room 347","west":"666"}	
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
