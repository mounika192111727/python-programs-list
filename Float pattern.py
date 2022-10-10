floats = []  
start = 0  
end = 1  
stepsize = 0.1  
while start < end:
    print("start append stepsize 0.1:")
    floats.append(start)
    start = correct(start + stepsize)
