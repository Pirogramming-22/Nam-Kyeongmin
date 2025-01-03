num = 0

class noneIntNum(Exception):
    def __init__(self):
        super().__init__('정수를 입력하세요')
        
class outOfRange(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')

### turn: playerA       
try:
    aNum = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
    if (aNum!=1 and aNum!=2 and aNum!=3):
        raise outOfRange
    elif (isinstance(aNum, int)):
        for i in range(1, aNum+1):
            print('playerA : {0}'.format(num+i))
        num = num+aNum
    else:
        # aNum이 정수가 아니라면
        raise noneIntNum    
except outOfRange as e1:
        print(e1)
except noneIntNum as e2:
        print(e2)

### turn: playerB    
try:
    bNum = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
    if (bNum!=1 and bNum!=2 and bNum!=3):
        raise outOfRange
    elif (isinstance(bNum, int)):
        for i in range(1, bNum+1):
            print('playerB : {0}'.format(num+i))
        num = num+bNum
    else:
        # bNum이 정수가 아니라면
        raise noneIntNum    
except outOfRange as e1:
        print(e1)
except noneIntNum as e2:
        print(e2)