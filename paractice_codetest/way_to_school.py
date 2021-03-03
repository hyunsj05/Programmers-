# import numpy as np
def solution(m, n, puddles):
    # answer = m*n/2;
    # for i in puddles:
    #     answer-=i[0]*i[1]*(m-i[0])*(n-i[1])/4
    a=[[1]*n for i in range(m)]
    # a[0][0]=1
    # print(a)
    for i in puddles:
        a[i[0]-1][i[1]-1]=0
    for i in range(m):
        for j in range(n):
            if (a[i][j]==1):
                if i==0:
                    a[i][j]=a[i][j-1]
                elif j==0:
                    a[i][j]=a[i-1][j]
                else:
                    a[i][j]=a[i-1][j]+a[i][j-1]
    answer=a[m-1][n-1]%1000000007
    # answer=1
    return answer
