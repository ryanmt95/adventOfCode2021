from collections import defaultdict

def hydrothermal_venture(vent_lines):
    
    vent_map = defaultdict(int)
    for start, end in vent_lines:
        if (start[0] != end[0]) and (start[1] != end[1]):
            continue

        if start[0] != end[0]:
            for i in range(start[0], end[0]+1):
                vent_map[(i, start[1])] += 1
        else:
            for i in range(start[1], end[1]+1):
                vent_map[(start[0], i)] += 1
    
    count = 0
    for _, val in vent_map.items():
        if val >= 2:
            count += 1
    
    return count

def hydrothermal_venture2(vent_lines):
    vent_map = defaultdict(int)
    for start, end in vent_lines:
        if (start[0] != end[0]) and (start[1] != end[1]):
            increment = 1 if start[1] < end[1] else -1
            for dx, dy in zip(range(start[0], end[0]+1), range(start[1], end[1]+increment, increment)):
                vent_map[(dx, dy)] += 1
        elif start[0] != end[0]:
            for i in range(start[0], end[0]+1):
                vent_map[(i, start[1])] += 1
        else:
            for i in range(start[1], end[1]+1):
                vent_map[(start[0], i)] += 1
    
    count = 0
    for _, val in vent_map.items():
        if val >= 2:
            count += 1
    
    return count

if __name__ == "__main__":
    print("Day 5: Knees Weak, Arms Spaghetti")

    f = open("day_5.txt",'r',encoding = 'utf-8')

    vent_lines = []
    for row in f:
        vent_line = sorted(list(map(lambda x: list(map(int, x.strip().split(","))), row.replace("\n", "").split("->"))), key = lambda x: (x[0], x[1]))
        vent_lines.append(vent_line)

    result = hydrothermal_venture(vent_lines)
    print(result)

    result = hydrothermal_venture2(vent_lines)
    print(result)