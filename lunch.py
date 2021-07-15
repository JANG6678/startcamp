import random
menu = ['한식','일식', '중식', '양식' ]
lunch = random.choice(menu)
print(lunch)

#랜덤으로 전화번호 가져오는 법
number = {'한식' : '123-456', '한식' : '123-456', '일식' : '123-456', '중식' : '123-456','양식' : '123-456'}
print(number[lunch])
print('오늘의 점심은',lunch,'입니다. 전화번호는 ', number[lunch], '입니다.')
print(f'오늘의 점심은{lunch}입니다. 전화번호는 {number[lunch]}입니다.')