num = 0

class noneIntNum(Exception):
    def __init__(self):
        super().__init__('정수를 입력하세요')
        
class outOfRange(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')
        
try:
    aNum = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
    if (aNum!=1 and aNum!=2 and aNum!=3):
        raise outOfRange
    else:
        # aNum이 정수가 아니라면
        raise noneIntNum    
except outOfRange as e1:
        print(e1)
except noneIntNum as e2:
        print(e2)

aNum = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))