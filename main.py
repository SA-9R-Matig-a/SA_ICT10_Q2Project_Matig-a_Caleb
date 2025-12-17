from pyscript import display, document # type: ignore

# Define club information using dictionaries
club_info = {
            "singing": {
                "name": "Singing Club",
                "description": "A club for vocalists and utaites of all skill levels.",
                "meeting_time": "Every Wednesday 3:30-5:00 PM",
                "location": "Room 23",
                "admin": "Naima",
                "members": 7,
                "category": "Arts"
            },
            "dance": {
                "name": "Dance Club",
                "description": "Let your body be free and flow to the music",
                "meeting_time": "Every Monday and Thursday 4:00-6:00 PM",
                "location": "Yodaka Dome",
                "admin": "Gira",
                "members": 67,
                "category": "Arts"
            },
            "japan": {
                "name": "Japanese Club",
                "description": "Learn, memorize, and speak Japanese with other like-minded people",
                "meeting_time": "Every Tuesday 3:45-5:30 PM",
                "location": "Room 10",
                "admin": "Merry",
                "members": 12,
                "category": "Academic"
            },
            "film": {
                "name": "Film Club",
                "description": "Produce, develop, and present amazing films and videos",
                "meeting_time": "Every Friday 3:30-5:00 PM",
                "location": "Room 25",
                "admin": "Odori",
                "members": 9,
                "category": "Arts"
            },
            "art": {
                "name": "Stylized Art Club",
                "description": "For those who love anime and other stylized art styles.",
                "meeting_time": "Every Wednesday 3:45-5:15 PM",
                "location": "Art Room",
                "admin": "Keiko",
                "members": 20,
                "category": "Arts"
            },
            "": {
                "name": "NA",
                "description": "NA",
                "meeting_time": "NA",
                "location": "NA",
                "admin": "NA",
                "members": "NA",
                "category": "NA"
            }
        }

# Recommends additional clubs based on chosen club.
related_clubs = {
    "singing": ["dance"],
    "dance": ["singing"],
    "film": ["art"],
    "art": ["film"],
    "japan": ["film"]
}

        
def show_club_info(e):
    document.getElementById('club-info').innerHTML = " "
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info[""])
            
    output = f"""
                {info['name']}
                Description:{info['description']}
                Meeting Time: {info['meeting_time']}
                Location: {info['location']}
                Administrator: {info['admin']}
                Number of Members: {info['members']}
                Category: {info['category']}
            """
    
    suggestions = related_clubs.get(selected_club, [])

    if suggestions:
                output += "If you're interested in this club, consider joining "
    for club_key in suggestions:
                output += f"{club_info[club_key]['name']} as well!"

    display(output, target="club-info")