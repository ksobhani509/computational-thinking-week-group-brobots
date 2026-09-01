def solution_station_7(expression):
    values = {
        "a": 3,
        "b": -1,
        "c": 4,
        "d": 7,
        "e": 0.5,
    }
    
    result = (eval(expression, {"__builtins__": None}, values))

    return float(result)

#example   
print(solution_station_7("b + d")) 
print(solution_station_7("a * e + c"))  


