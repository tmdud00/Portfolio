import random
하루식단아침=[]
하루식단점심=[]
하루식단저녁=[]
하루식단간식=[]
print("="*50)
print("환영합니다. 삼식이 메인화면입니다!")
print("="*50)
print("오늘의 메뉴는?:1 / 식단표짜러가기:2")
while True:
    메인메뉴=int(input("원하시는 메뉴를 선택해주세요:"))
    if 메인메뉴 in [1,2]:
        if 메인메뉴==1:
            print("식단표를 먼저 구성해주세요!")
        else:
            print("="*50)
            print("식단표 페이지입니다. 최대 한 달간의 식단을 구성할 수 있습니다.")
            print("회원님의 권장 칼로리에 맞게 메뉴를 입력해주세요!")
            print("="*50)
            break
    else:
        print("오류입니다. 다시입력해주세요!")
           
for i in range(30):
    연속여부=int(input("식단표 짜기를 원하시면 [1] / 오늘의 메뉴는? 페이지를 원하시면 [2]:"))
    if 연속여부 in [1,2]:
        if 연속여부==1:
            print("최대 30일차까지 저장이 가능합니다")
            print("아침>점심>저녁>간식 순서로 입력해주세요!")  
            하루식단아침.append(input("아침:"))
            하루식단점심.append(input("점심:"))
            하루식단저녁.append(input("저녁:"))
            하루식단간식.append(input("간식:"))
            print("="*50)
            print("하루식단이 모두 구성되었습니다")
            
        elif 연속여부==2:
            break
    else:
         print("오류입니다. 다시입력해주세요!")
        
print("="*50)    
print("오늘의 메뉴는?페이지입니다.")
print("아침:1 / 점심:2 / 저녁:3 / 간식:4")
print("="*50)
for i in range(30):
    시간선택=int(input("원하시는 항목을 선택해주세요:"))
    if 시간선택 in [1,2,3,4]:
        if 시간선택==1:
            아침메뉴=random.choice(하루식단아침)
            print("오늘의 아침메뉴는:{}".format(아침메뉴))
        elif 시간선택==2:
            점심메뉴=random.choice(하루식단점심)
            print("오늘의 점심메뉴는:{}".format(점심메뉴))
        elif 시간선택==3:
            저녁메뉴=random.choice(하루식단저녁)
            print("오늘의 저녁메뉴는:{}".format(저녁메뉴))
        else:
            간식메뉴=random.choice(하루식단간식)
            print("오늘의 간식메뉴는:{}".format(간식메뉴))
    else:
         print("오류입니다. 다시입력해주세요!")
                
            

         
