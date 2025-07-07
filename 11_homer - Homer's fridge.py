"""
Homer's fridge
Course: B0B36ZAL
"""
 
#nasledujici kod nijak nemodifikujte!
class Food:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration
#predesly kod nijak nemodifikujte!
 
def openFridge(fridge):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(
            str(food.name), str(food.expiration))
        )
    print("")
 
# test vypisu - pri odevzdani smazte, nebo zakomentujte
 
 
"""
Task #1
"""
def maxExpirationDay(fridge):
    if not fridge:
        return -1
    max_expiration = max(food.expiration for food in fridge)
    return max_expiration
    pass
 
# test vypisu - pri odevzdani smazte, nebo zakomentujte
# The command should print 4
 
 
"""
Task #2
"""
def histogramOfExpirations(fridge):
    histogram = [0] * (maxExpirationDay(fridge) + 1)
    for food in fridge:
        histogram[food.expiration] += 1
    return histogram
 
# test vypisu - pri odevzdani smazte, nebo zakomentujte
# The command should print [0, 2, 0, 1, 1]
 
 
"""
Task #3
"""
def cumulativeSum(histogram):
    sum = [0] * len(histogram)
    for i in range(0, len(histogram)):
        sum[i] = sum[i-1] + histogram[i]
    return sum
 
# test vypisu - pri odevzdani smazte, nebo zakomentujte
 
# The command should print [0, 2, 2, 3, 4]
 
 
"""
Task #4
"""
def sortFoodInFridge(fridge):
    sorted_food = [None] * len(fridge)
    histogram = histogramOfExpirations(fridge)
    sum = cumulativeSum(histogram)
    for food in fridge:
        pos_ind = sum[food.expiration] - 1
        sorted_food[pos_ind] = food
        sum[food.expiration] -= 1
    for food in sorted_food:
        print(food.name, "(expires in: ", food.expiration, " days)")
    return sorted_food
 
# test vypisu - pri odevzdani smazte, nebo zakomentujte
# The command should print
# Following items are in Homer's fridge:
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)
 
 
"""
Task #5
"""
def reverseFridge(fridge):
    return fridge[::-1]
 
# test vypisu - pri odevzdani smazte, nebo zakomentujte
# The command should print
# Following items are in Homer's fridge:
# donut (expires in: 3 days)
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# beer (expires in: 4 days)
 
# test vypisu - pri odevzdani smazte, nebo zakomentujte
# The command should print
# Following items are in Homer's fridge:
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)
 
 
"""
Task #6
"""
def eatFood(name, fridge):
   # filtered_fridge = [food_item for food_item in fridge if food_item.name != name and food_item.expiration]
    filtered_fridge = fridge.copy()
    minExp = float('inf')
    potentialDelete = None
 
    for i in range(len(filtered_fridge)):
        food = filtered_fridge[i]
        if food.name == name:
            if food.expiration <= minExp:
                minExp = food.expiration
                potentialDelete = i
    if potentialDelete is None:
        return filtered_fridge
     
    else:
        filtered_fridge.pop(potentialDelete)
 
        return filtered_fridge
 
            
            
 
 
 
 
# test vypisu - pri odevzdani smazte, nebo zakomentujte
 
# The command should print
# Following items are in Homer's fridge:
# beer (expires in: 4 days)
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# donut (expires in: 6 days)
 
if __name__ == '__main__':
    openFridge(
    eatFood("donut",
        [Food("beer", 4), Food("steak", 1), Food("hamburger", 1),
        Food("donut", 3), Food("donut", 1), Food("donut", 6)]
    ))