#산술/기하/조화평균, 분산 : 4, 10, 20, 15를 기준으로

#산술평균
arith_mean=(4+10+20+15)/4 
print(arith_mean)

#기하평균
geometric_mean=(4*10*20*15)**(1/4)
print(geometric_mean)

#조화평균
harmonic_mean=4/(1/4+1/10+1/20+1/15)
print(harmonic_mean)

#분산
V=((arith_mean-4)**2+(arith_mean-10)**2+(arith_mean-20)**2+(arith_mean-15)**2)/4
print(V)

#최빈값과 반복 횟수, 중앙값 : 10, 8, 5, 4, 3, 6, 8, 7, 8, 6, 7, 9, 6, 8을 기준으로

#최빈값과 반복 횟수
num_list=[10, 8, 5, 4, 3, 6, 8, 7, 8, 6, 7, 9, 6, 8]
mode=-"none"
max=0
for x in list(set(num_list)):
  if num_list.count(x) > max:
    mode=x
    max=num_list.count(x)
print("최빈값 : ", mode, "반복 횟수 : "max)

#중앙값
num_list=num_list.sort()
n=len(numlist)
if n%2==1:
  median=numlist[int((n-1)/2)]
else:
  median=(numlist[int(n/2)-1]*numlist[int(n/2)])/2

print(median)
