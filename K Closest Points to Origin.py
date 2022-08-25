import math
def kClosest(points,k):
    distance = []
    for v in range(len(points)):
        i = points[v]
        r = i[0] ** 2 + i[1] ** 2
        distance.append(math.sqrt(r))
        
    
    dictionary = [dictionary for distance, dictionary in sorted(zip(distance,points))]
    Final = []
    for index in range(k):
        Final.append(dictionary[index])
    return (Final)
    
  



