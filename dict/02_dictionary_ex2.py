#dictionnary_ex2.py



# 딕셔너리를 이용해 사용자로부터 영단어와 뜻을 입력받아 사전을 구성하고
# 사용자가 입력한 단어를 검색하여 뜻을 출력하는 프로그램


# 입력의 종류/ 단어 검색의 정료 모두 quit단어를 이용한다.
# 사전구성이 끝나면 바로 단어 검색을 진행한다.


# 빈 딕셔너리 생성
# ek_dic={}
ek_dic=dict()  #dict( )  함수 호출  . 윗줄 써도 되고 아래줄 써도 되고~!


# 사전 구성
# 종료 조건은 사용자가 quit 단어를 입력햇을떄



while True:
    # 단어 등록
    eng=input("/n 영어 단어 등록(종료시에는 quit를 입력하세요):")


    if eng=="quit":
        break  #단어 등록 종료


    elif eng not in ek_dic : # 단어를 등록시켜달라는 입력
                             # 사전에 단어가 있는 경우(등록하면 안됨:이미 등록된 단어입니다.)
                             # 사전에 단어가 없는 경우(뜻을 입력받아서 등록)                                                      
        kor=input("%s 의 뜻 입력: " % eng)
        ek_dic[eng]=kor

    else:
        print("%s는 이미 등록된 단어 입니다." % eng)

print()



print("사전에서 단어를 검색하세요.")

while True:
    eng=input("/n 영어 단어 등록(종료는 quit):")

    if eng=="quit":
        break

    elif eng in ek_dic:  # 입력된 단어가 사전에 있는 경우
        print("%s의 뜻은 %s 입니다." % (eng,ek_dic[eng]))

    else:
        print("%s는 사전에 없는 단어 입니다." % eng)


print("/n 종료 합니다." )









        
