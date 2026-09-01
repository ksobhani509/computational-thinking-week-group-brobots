def solution_station_5(input_val):
    name = str(input_val).strip()
    
    team_1 = ["Ainas", "Tobit", "Yasmin", "Zoë", "Iuliia", "Klementyna", "Markus", "Mufang", "Oumaima", "Ebony", "Nandini", "Nathan", "Tiara", "Yurui", "Ben", "Christopher", "Lula", "Muni", "Yuvraj"]
    team_2 = ["Huy", "Iris", "Katharina", "Minseo", "Sade", "Alex", "Arwen", "Rajko", "Sylwia", "Zeno", "Christina", "Helen", "Mark", "Mats", "Vadim", "David", "Lora", "Quinn", "Tarling"]
    team_3 = ["Elizabeth", "Gabriel", "Jakub", "Luc", "Soelie", "Aleksandra", "Arnav", "Donna", "Milan", "Rongze", "Cris", "Jingqi", "Oliver", "Vaayu", "Yusef", "Afua", "Anna", "Daniel", "Nataly", "Rafael"]
    team_4 = ["Jeremy", "Krishiv", "Neel", "Yujie", "yutong", "An", "Heer", "Paige", "Samir", "Amalia", "Douwe", "Illya", "Maria", "Rakin", "Lara", "Lucas", "Michelle", "Oliwia", "Tom"]
    
    if name in team_1:
        return 1
    elif name in team_2:
        return 2
    elif name in team_3:
        return 3
    elif name in team_4:
        return 4
    else:
        return 0
