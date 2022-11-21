{
    "name": "Medical App",
    "summary": "medical module",
    "description": """patient management :
    -appointment .
    -medical history. 
    -doctors""",
    "sequence": -100,
    "website": "www.amar.sd",
    "author": "Amar Yasser Abdalsamad",
    "version": "1,0",
    "depends": ["base","hr","sale"],
    "data": ["security/ir.model.access.csv",
        "views/menu_action.xml",
        "views/views.xml",
        "data/sequence.xml",
        "views/website_menu.xml",
    ],
    "application": True,
}