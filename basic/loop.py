

friends = ['p1', 'p2', 'p3'] 

for friend in friends:
    print(friend)

## finding the max number
def findMaxNum(numbers):
    max = None

    for number in numbers:
        if max is None:
            max = number
        elif number > max:
            max =  number
        else:
            continue

    return max    

print('Max num is: ', findMaxNum([ 10, 25, 3018, 1 , 5 , 955, 12, 17, 88, 500 ]) )           


##finding the average
def findingAvg(numbers):
    sum = 0
    count = 0

    for number in numbers:
        sum = sum + number
        count = count + 1

    avg = sum / count

    return avg


newNumbers = [ 9, 41, 12, 3, 74, 15 ]


print('Average: ', findingAvg(newNumbers) )        



