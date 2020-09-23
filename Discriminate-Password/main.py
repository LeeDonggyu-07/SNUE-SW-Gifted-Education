import re
pw = input("판별할 비밀번호를 입력해주세요")
x = True

while x:
  if 8<=len(pw)<=15:
    print("invalid")
    break
  elif not re.search("[a-z].pw"):
    print("invalid")
    break
  elif not re.search("[0-9].pw"):
    print("invalid")
    break
  else:
    print("valid")
