num = 0
class noneIntNum(Exception):
    def __init__(self):
        super().__init__('정수를 입력하세요')
        
class outOfRange(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')

gameTurn = True
# True = playerA, False = playerB

def brGame(num, gameTurn):
    try:
        answer = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')
        try:
            aNum = int(answer)
        except ValueError:
            raise noneIntNum
        
        if (aNum!=1 and aNum!=2 and aNum!=3):
            # aNum이 1,2,3의 숫자가 아니라면
            raise outOfRange
        elif (not isinstance(aNum, int)):
            # aNum이 정수가 아니라면
            raise noneIntNum
        else:
            for i in range(1, aNum+1):
                if(gameTurn):
                    print('playerA : {0}'.format(num+i))
                    if(num+i == 31):
                        return -1, gameTurn
                else:
                    print('playerB : {0}'.format(num+i))
                    if(num+i == 31):
                        return -1, gameTurn
            num = num+aNum
            gameTurn = not gameTurn # swith player turn
            return num, gameTurn
    except outOfRange as e1:
            print(e1)
    except noneIntNum as e2:
            print(e2)
    return num, gameTurn
                        
while(num < 31):
    num, gameTurn = brGame(num, gameTurn)
    if(num==-1):
        if(gameTurn):
            # 31을 외친 사람이 playerA인 경우
            print('playerB win!')
        else:
            # 31을 외친 사람이 playerB인 경우
            print('playerA win!')
        break