#조건에 따른 실행문장 선택하기 : 조건문(if/else)
#미세먼지(dust) 농도의 값이 50 초과이면 '50초과' 50이하이면 '50이하'
dust = 50
#if 조건문 :    조건문안에는 참거짓을 따질 수 있는 표현식이 들어가야한다
  #실행할 문장
#else 조건문 :
    #실행할 문장
if dust > 50 :
    print('50초과')
else :
    print('50이하')