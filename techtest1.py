def minimum_cost(stones_path):

    if stones_path[0] != 0:
        print(f"stones_path[0] first element should be zero in {stones_path}")
        return

    if len(stones_path) < 2 or len(stones_path) > 100:
        print(f"stones_path length should be between 2 and 100 stones")
        return
    
    for i in range(len(stones_path)-1):
        if stones_path[i] >= stones_path[i+1]:
            print(f"stones_path should be sorted in a strictly increasing order")
            return
    
    def cost_function(path):
        return max(abs (path[i] - path[i+1]) for i in range(len(path)-1) )

    #Path1: from left to right picking every second stone, then the rest in reverse (backward)
    forward1 = stones_path[::2]         #even indexed stones forward
    backward1 = stones_path[1::2][::-1] #odd indexed stones backward
    path1 = forward1 + backward1
    cost1 = cost_function(path1)
    print(f"Cost1: {cost1}, Path: {path1}")

    #Path2: from left to right picking every first stone, then the rest in reverse (backward)
    forward2 = stones_path[1::2]            #odd indexed stones forward
    backward2 = stones_path[::2][::-1]     #even indexed stones backward
    path2 = forward2 + backward2
    cost2 = cost_function(path2)
    print(f"Cost2: {cost2}, Path: {path2}")

    min_cost = min(cost1, cost2)
    return min_cost


# Test Cases:
stones_path = [0,3,9]
print(minimum_cost(stones_path))

stones_path = [0,2,5,6,7]
print(minimum_cost(stones_path))

stones_path = [0,3,8,15,20,22,31,44,52]
print(minimum_cost(stones_path))
