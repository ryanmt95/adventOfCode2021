def sonar_sweep(depth_measurements):

    count = 0
    for i, depth in enumerate(depth_measurements[1:], start=1):
        if depth > depth_measurements[i-1]:
            count += 1
    return count

def sonar_sweep2(depth_measurements):
    
    result = [0] * (len(depth_measurements) - 2)
    for i in range(0, len(depth_measurements) - 2):
        result[i] += depth_measurements[i]
        result[i] += depth_measurements[i+1]
        result[i] += depth_measurements[i+2]

    return sonar_sweep(result)

if __name__ == "__main__":
    print("Let's start day one!")

    input_file = "day_1.txt"

    f = open(input_file,'r',encoding = 'utf-8')

    depth_measurements = []
    for row in f:
        depth_measurements.append(int(row))
    
    result = sonar_sweep(depth_measurements)

    print(result)

    result = sonar_sweep2(depth_measurements)

    print(result)
