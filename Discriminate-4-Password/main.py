# 4 글자 비밀번호 판별
password=input("사용하고자 하는 암호를 입력하세요: ") # 비밀번호 입력

p1=int(password[0]) # 비밀번호의 숫자 하나하나를 변수로 지정
p2=int(password[1])
p3=int(password[2])
p4=int(password[3])

print(p1,p2,p3,p4) # 비밀번호 출력, 확인

# 1. 중복되는 숫자가 있는지를 검사
duplicate=p1==p2 or p1==p3 or p1 ==p4 or p2==p3 or p2==p4 or p3==p4
# 2. 4자리 수가 모두 1씩 증가하는지를 검사
increment=p1+1==p2 and p2+1 ==p3 and p3+1==p4
# 3. 4자리 수가 모두 1씩 감소하는지를 검사
decrement=p1-1==p2 and p2-1==p3 and p3-1==p4

if duplicate or increment or decrement:
 print("사용할 수 없는 암호입니다.")

else:
 print("사용할 수 있는 암호입니다.")
