from collections import deque

def lantern_fish(fish, days):

    fishes = deque([0 for _ in range(9)])
    for f in fish:
        fishes[f] += 1

    for _ in range(days):
        num = fishes.popleft()
        fishes[6] += num
        fishes.append(num)
    
    return sum(fishes)
    

if __name__ == "__main__":
    print("Day 6: Monday Blues")

    f = open("day_6.txt",'r',encoding = 'utf-8')

    input = list(map(int, f.readline().split(",")))
    result = lantern_fish(input, 80)
    print(result)

    result = lantern_fish(input, 256)
    print(result)
        