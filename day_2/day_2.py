def dive(directions):

    x, y = 0, 0

    for direction, magnitude in directions:
        if direction == 'forward':
            x += magnitude
        elif direction == 'down':
            y += magnitude
        elif direction == 'up':
            y -= magnitude
        else:
            continue
    
    return x * y

def dive2(directions):

    x, y, aim = 0, 0, 0

    for direction, magnitude in directions:
        if direction == 'forward':
            x += magnitude
            y += aim * magnitude
        elif direction == 'down':
            aim += magnitude
        elif direction == 'up':
            aim -= magnitude
        else:
            continue
    
    return x * y

if __name__ == "__main__":
    print("What is life? Just pain")

    input_file = "day_2.txt"

    f = open(input_file,'r',encoding = 'utf-8')

    directions = []
    for row in f:
        direction, magnitude = row.split(" ")
        directions.append((direction, int(magnitude)))
        
    result = dive(directions)
    print(result)

    result = dive2(directions)
    print(result)