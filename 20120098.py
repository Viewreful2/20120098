
def rule1(B,size) :
    for i in range(size) :
        if (B[i][0]+B[i][1]+B[i][2]+B[i][3]+B[i][4]) == 0:
            return True;
    return False;

def rule2(B,size) :
    for i in range(size) :
        if (B[0][i]+B[1][i]+B[2][i]+B[3][i]+B[4][i]) == 0:
            return True;
    return False;

def rule3(B,size) :
        cnt = 0
        for i in range(size):
                if(B[i][i] == 0):
                        cnt += 1
        if(cnt == size):
                return True;
        cnt = 0
        for i in range(size):
                if(B[i][4-i] == 0):
                        cnt += 1
        if(cnt == size):
                return True;
        return False;

def rule4(B,size) :
        if (B[0][0]+B[0][4]+B[4][0]+B[4][4]) == 0:
                return True;
        return False;


size = 5

BingoCard= []
BingoCard_zero = []
T = int(input())

for i in range(T):
        
        BingoCard= []
        BingoCard_zero = [[1]*size for i in range(size)]
        if(BingoCard_zero[2][2] != 0):
                BingoCard_zero[2][2] = 0
        for i in range(0, size):
                rowInput = input().split()
                rowInput = [int(j) for j in rowInput]
                BingoCard.append(rowInput)
        if(BingoCard[2][2] != 0):
                BingoCard[2][2] = 0


        numInput = input().split()
        numInput = [int(j) for j in numInput]

        s = 0


        for num in numInput:
                s += 1

                for i in range(size):
                        for j in range(size):
                                if(BingoCard[i][j] == num):
                                        BingoCard_zero[i][j] = 0
                if rule1(BingoCard_zero,size) == True:
                        print(s)
                        break

                if rule2(BingoCard_zero,size) == True:
                        print(s)
                        break


                if rule3(BingoCard_zero,size) == True:
                        print(s)
                        break

                if rule4(BingoCard_zero,size) == True:
                        print(s)
                        break

                





