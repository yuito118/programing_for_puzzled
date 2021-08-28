

def Good(Comb, candList, candTalents, AllTalents):
    for tal in AllTalents:
        cover = False
        for cand in Comb:
            candTal = candTalents[candList.index(cand)]
            if tal in candTal:
                cover = True
        if not cover:
            return False 
    return True         


#This procedure finds the combination with the minimum number of candidates
#that cover all the required talents by generating all the combinations
#one at a time.
def Hire4Show(candList, candTalents, talentList):

    n = len(candList)
    hire = candList[:]
    for i in range(2**n):
        Combination = []
        num = i
        for j in range(n): 
            if (num % 2 == 1):
                Combination = [candList[n-1-j]] + Combination
            num = num // 2

        if Good(Combination, candList, candTalents, talentList):
            if sum(x[1] for x in hire) > sum(x[1] for x in Combination):
                hire = Combination

    print ('Optimum Solution:', hire)


showTalentW = [1,2,3,4,5,6,7,8,9]
CandidateListW = [('A', 3), ('B',2), ('C',1), ('D',4), ('E',5), ('F',2), ('G',7)]
CandToTalentsW = [[1,5],[1,2,8],[2,3,6,9],[4,6,8],[2,3,9],[7,8,9],[1,3,5]]

Hire4Show(CandidateListW, CandToTalentsW, showTalentW)

