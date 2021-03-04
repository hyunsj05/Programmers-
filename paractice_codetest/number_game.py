def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    answer=0
    for i in A:
        # flag=0
        # for po,j in enumerate(B):
        if B[0]>i:
            del B[0]
            answer+=1
            
            # if j<i and flag==0:
            #     del B[len(B)-1]
            #     break
            # elif j<i:
            #     del B[po-1]
            #     answer+=1
            #     break
            # elif len(B)-1==po:
            #     if j==i:
            #         del B[po]
            #     else:
            #         del B[po]
            #         answer+=1
            # flag=1
                
                
    return answer
