import functools

def main():
    file = open("input/1.data", "r")

    # Part 1
    print("Part1: "+str(functools.reduce(lambda a,b: (a[0]+1,int(b)) if int(b)>int(a[1]) else (a[0],int(b)), file.readlines(), (-1,0))[0]))
    # Part 2
    file.seek(0)
    start = *file.readlines()[0:3],
    file.seek(2)
    print("Part2: "+str(functools.reduce(lambda a,b: (a[0]+1,a[1][1:]+(int(b),)) if sum(map(int,a[1][1:]+(int(b),)))>sum(map(int,a[1])) else (a[0],a[1][1:]+(int(b),)), file.readlines(), (-1,start))[0]))

if __name__ == "__main__":
    main()
