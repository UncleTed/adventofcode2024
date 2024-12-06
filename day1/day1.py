def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines


def day1():
    leftside = []
    rightside = []
    lines = get_input('long.txt')
    for l in lines:
        (left, right) = l.split()
        leftside.append(int(left))
        rightside.append(int(right))

    leftside.sort()
    rightside.sort()

    total_distance = 0
    for left, right in zip(leftside, rightside):
        total_distance = total_distance + abs(left - right)

    print('total distance is : ', total_distance)

    
def day2():
    leftside = []
    rightside = []
    lines = get_input('long.txt')
    for l in lines:
        (left, right) = l.split()
        leftside.append(int(left))
        rightside.append(int(right))

    similarity = 0
    for left in leftside:
        similarity = similarity + (left * rightside.count(left))

    print('similarity: ', similarity)

if __name__ == "__main__":
    day1()
    day2()