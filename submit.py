path='0'+input()
used =[[False]*9 for i in range(9)]

cnt = 0

def only(i,j):
    
    k = 0

    if (i == 7 and j == 1):
        return 0;
    if not(used[i - 1][j]):
        k+=1;
    if not(used[i + 1][j]):
        k+=1;
    if not(used[i][j - 1]):
        k+=1;
    if not(used[i][j + 1]):
        k+=1;
    return k == 1;


def solve(i,j,h) :
    
    u=0
    d=0 
    l=0
    r=0
    global path
    
    if (h == 48 or (i == 7 and j == 1)) :
        if (h == 48):
            global cnt
            cnt+=1
        return

    u = not(used[i - 1][j])
    d = not(used[i + 1][j])
    l = not(used[i][j - 1])
    r = not(used[i][j + 1])
    
    if ((u and d and not(l) and not(r)) or (not(u) and not(d) and l and r)):
        return
    used[i][j] = 1
    h+=1
    p = path[h]
    
    if (u and only(i - 1, j)):
        if (p == 'U' or p == '?'):
            solve(i - 1, j, h)
        used[i][j] = 0
        h-=1
        return

    if (d and only(i + 1, j)) :
        if (p == 'D' or p == '?'):
            solve(i + 1, j, h)
        used[i][j] = 0
        h-=1
        return

    if (l and only(i, j - 1)):
        if (p == 'L' or p == '?'):
            solve(i, j - 1, h);
        used[i][j] = 0
        h-=1
        return;

    if (r and only(i, j + 1)):
        if (p == 'R' or p == '?'):
            solve(i, j + 1, h)
        used[i][j] = 0
        h-=1
        return;

    if (u and (p == 'U' or p == '?')):
        solve(i - 1, j, h)
    if (d and (p == 'D' or p == '?')):
        solve(i + 1, j, h);
    if (l and (p == 'L' or p == '?')):
        solve(i, j - 1, h)
    if (r and (p == 'R' or p == '?')):
        solve(i, j + 1, h)
    
    used[i][j] = 0
    h-=1


for i  in range(9):
    for j in range(9):
        used[i][j] = i == 0 or i == 8 or j == 0 or j == 8


solve(1, 1, 0)
print(cnt)
