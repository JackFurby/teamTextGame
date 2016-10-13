room_Office1={
	"name":"Office 1",
	"description":
    """Your office is small with a chair by your desk and a bench against the wall. There is a door to the east leading to Therapy""",
	"items":[],
	"exits":{"East":"Therapy room"},
	"map": ["------------", "|          |", "| OFFICE 1 |", "|          |", "|          |", "---- \------"]
}
room_Office2={
	"name":"Office 2",
	"description":
    """add me""",
	"items":[],
	"exits":{"north":"Canteen","south":"Room 666"}	
}
room_Reception={
	"name":"Reception",
	"description":
    """add me""",
	"items":[],
	"exits":{"east":"The yard","west":"Emergency room"}	
}
room_Therapy={
	"name":"Therapy room",
	"description":
    """add me""",
	"items":[],
	"exits":{"west":"Office 1","east":"Canteen"}	
}
room_Canteen={
	"name":"Canteen",
	"description":
    """add me""",
	"items":[],
	"exits":{"west":"Therapy room","south":"Office 2","east":"Emergency room"}	
}
room_666={
	"name":"Room 666",
	"description":
    """add me""",
	"items":[],
	"exits":{"north":"Office 2"}	
}
room_ER={
	"name":"Emergency room",
	"description":
    """add me""",
	"items":[],
	"exits":{"west":"Canteen","east":"Reception"}
}
room_Yard={
	"name":"The yard",
	"description":
    """add me""",
	"items":[],
	"exits":{"north":"Reception"}
}
rooms={
	"Office 1":room_Office1,
	"Office 2":room_Office2,
	"Reception":room_Reception,
	"Therapy room":room_Therapy,
	"Canteen":room_Canteen,
	"Room 666":room_666,
	"Emergency room":room_ER,
	"The yard":room_Yard
}
