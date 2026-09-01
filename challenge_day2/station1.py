def solution_station_1(input_val):
    n = int(input_val)
    if n <= 0:
        return 0
    
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
        
    return int(b)  