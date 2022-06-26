import random
def path_finding():
    target=(9,9)
    steps=0
    path=[]
    
    #create 2D matrix with weights
    obstacles=[(9,7),(8,7),(6,8),(6,7)]
    matrix=[]
    for x in range(10):
        matrix.append([])
        for y in range(10):
            dist=abs((x-target[0]))+abs((y-target[1])) #calculate manhattan distnce
            matrix[x].append(dist)
    #mark obstacles with -1
    for x in obstacles:
        a=x[0]
        b=x[1]
        matrix[a][b]=-1
        
    #A*
    opened=[]
    closed=[]
    steps=0
    opened.append((0,0,matrix[0][0]))
    while opened:
        
        steps+=1
        opened.sort(key=lambda a: a[2])
        parent=opened.pop(0)
        
        if parent==(9,9,0):
            path.append((9,9))
            return steps, path
        closed.append(parent)
        a=parent[0]
        b=parent[1]
        path.append((a,b))
        if a>0 and b>0:
            if matrix[a+1][b+1]!=-1:  #diagonal
                opened.append((a+1,b+1,matrix[a+1][b+1]))
            if matrix[a+1][b]!=-1:   #bottom
                opened.append((a+1,b,matrix[a+1][b]))
            if matrix[a][b+1]!=-1:   #right
                opened.append((a,b+1,matrix[a][b+1]))
            if matrix[a-1][b]!=-1:  #top
                opened.append((a-1,b,matrix[a-1][b]))
            if matrix[a][b-1]!=-1:  #left
                opened.append((a,b-1,matrix[a][b-1]))
        elif a>0 and b==0:
            if matrix[a+1][b+1]!=-1:  #diagonal
                opened.append((a+1,b+1,matrix[a+1][b+1]))
            if matrix[a+1][b]!=-1:   #bottom
                opened.append((a+1,b,matrix[a+1][b]))
            if matrix[a][b+1]!=-1:   #right
                opened.append((a,b+1,matrix[a][b+1]))
            if matrix[a-1][b]!=-1:  #top
                opened.append((a-1,b,matrix[a-1][b]))
        elif a==0 and b>0:
            if matrix[a+1][b+1]!=-1:  #diagonal
                opened.append((a+1,b+1,matrix[a+1][b+1]))
            if matrix[a+1][b]!=-1:   #bottom
                opened.append((a+1,b,matrix[a+1][b]))
            if matrix[a][b+1]!=-1:   #right
                opened.append((a,b+1,matrix[a][b+1]))
            if matrix[a][b-1]!=-1:  #left
                opened.append((a,b-1,matrix[a][b-1]))
        elif a==0 and b==0:
            if matrix[a+1][b+1]!=-1:  #diagonal
                opened.append((a+1,b+1,matrix[a+1][b+1]))
            if matrix[a+1][b]!=-1:   #bottom
                opened.append((a+1,b,matrix[a+1][b]))
            if matrix[a][b+1]!=-1:   #right
                opened.append((a,b+1,matrix[a][b+1]))
        elif a==0 and b==9:
            if matrix[a+1][b]!=-1:   #bottom
                opened.append((a+1,b,matrix[a+1][b]))
            if matrix[a][b-1]!=-1:  #left
                opened.append((a,b-1,matrix[a][b-1]))
            if matrix[a+1][b-1]!=-1:  #diagonal
                opened.append((a+1,b-1,matrix[a+1][b-1]))
        elif a>0 and b==9:
            if matrix[a+1][b-1]!=-1:  #diagonal
                opened.append((a+1,b-1,matrix[a+1][b-1]))
            if matrix[a+1][b]!=-1:   #bottom
                opened.append((a+1,b,matrix[a+1][b]))
            if matrix[a-1][b]!=-1:  #top
                opened.append((a-1,b,matrix[a-1][b]))
            if matrix[a][b-1]!=-1:  #left
                opened.append((a,b-1,matrix[a][b-1]))
        elif a==9 and b==9:
            if matrix[a-1][b-1]!=-1:  #diagonal
                opened.append((a-1,b-1,matrix[a-1][b-1]))
            if matrix[a-1][b]!=-1:  #top
                opened.append((a-1,b,matrix[a-1][b]))
            if matrix[a][b-1]!=-1:  #left
                opened.append((a,b-1,matrix[a][b-1]))
            


print(path_finding())







