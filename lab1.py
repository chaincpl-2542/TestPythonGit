pi = 3.14
allResults = []

print('Enter your radius:')
radius = input()

def circle_area_cal(radius):
    area = pow(radius,2) * pi
    allResults.append(area)
    return area
    
for i in range(1,6):
    #circle_area_cal(i)
    print(f"the area of {i} is {circle_area_cal(i)}")


allResults.append(10)
allResults.pop(0) 
print(sum(allResults))

grades = {'Chain' : 'A',
          'Jab' : 'B'}
        
print(grades['Chain'])
print("Chain")