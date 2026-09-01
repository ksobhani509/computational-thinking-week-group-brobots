from datetime import datetime

def solution_station_2(input_val):
    date_str = str(input_val).strip()
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    day_oftw = date_obj.strftime("%A")

    if day_oftw == "Monday":
        return "月曜日"
    elif day_oftw == "Tuesday":
        return "火曜日"
    elif day_oftw == "Wednesday":
        return "水曜日"
    elif day_oftw == "Thursday":
        return "木曜日"
    elif day_oftw == "Friday":
        return "金曜日"
    elif day_oftw == "Saturday":
        return "土曜日"
    elif day_oftw == "Sunday":
        return "日曜日"