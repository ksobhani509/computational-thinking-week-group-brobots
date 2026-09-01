def solution_station_7(expression):
    values = {
        "a": 3,
        "b": 4,
        "c": -1,
        "d": 7,
        "e": 0.5,
    }
    
    return eval(expression, {"__builtins__": None}, values)

#example   
print(solution_station_7("b + d")) 
print(solution_station_7("a * e + c"))  


