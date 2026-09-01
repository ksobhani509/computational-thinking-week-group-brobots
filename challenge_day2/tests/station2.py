from datetime import datetime

def solution_station_2(input_val):
    date_str = str(input_val).strip()
    date_obj = datetime.strptime(date_str, "%Y/%m/%d")
    day_oftw = date_obj.strftime("%A")

    if day_oftw == "Monday":
        return "星期一"
    elif day_oftw == "Tuesday":
        return "星期二"
    elif day_oftw == "Wednesday":
        return "星期三"
    elif day_oftw == "Thursday":
        return "星期四"
    elif day_oftw == "Friday":
        return "星期五"
    elif day_oftw == "Saturday":
        return "星期六"
    elif day_oftw == "Sunday":
        return "星期日"