def kidsWithCandies(candies: list[int], extraCandies: int):
    kids = len(candies)
    result = []
    for i in range(kids):
        temp = candies[i] + extraCandies
        temp_bool = True
        for x in candies:
            if x == candies[i]: continue
            if temp < x: temp_bool = False; break
        if temp_bool == False: result.append(False); continue
        result.append(True)
    return result