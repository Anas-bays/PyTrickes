if __name__ == '__main__':
    x = int(input()) # 1
    y = int(input()) # 1
    z = int(input()) # 1
    n = int(input()) # 2
    l=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if ((i+j+k) != n):
                    l.append([i,j,k])
    print(l)
    
    # Output:
    # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    
