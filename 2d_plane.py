def maxPoints(points) -> int:
    lenght = len(points)
    max_val = 0
    if lenght < 3: return lenght
    for i in points:
        d, dups, cur_max = {}, 0, 0
        for j in points:
            if i != j:
                if j[0] == i[0]:
                    slope = 'inf'
                else:
                    slope = float(j[1] - i[1])/float(j[0] - i[0])
                d[slope] = d.get(slope, 0) + 1
                cur_max = max(cur_max, d[slope])
            else:
                dups += 1
                
        max_val = max(max_val, cur_max + dups)
        
    return max_val  
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]] 
print(maxPoints(points)) 
