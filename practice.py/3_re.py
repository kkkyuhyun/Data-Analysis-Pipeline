import re
#abcd, book, desk
#ca?e
#care, cafe, case, cave 

p = re.compile("ca.e") #pattern . 은 하나의 문자 ^은 문자열의 시작


def print_match(m):

    if m:
        print("m.group():",m.group())
        print("m.string:",m.string)
        print("m.start():",m.start())
        print("m.end():",m.end())
        print("m.span():",m.span())
    else:
        print("not match")
        
m= p.match("cafe")
print_match(m)


m=p.search("careless") # 주어진 문자열 중에 일치하는게 있는지 확인 
print_match(m)

m=p.findall("careless") #findall : 일치하는 모든 것을 리스트 형태로 반환 

lst=p.findall("good care")
print(lst)
#1. p = re.compile("원하는 형태로 반환")
#2. m = p.match("비교할 문자열")
#3. m = p.search("비교할 문자열")
#4. lst=p.findall("비교할 문자열") 일치하는 모든 것을 리스트 형태로 반환

#원하는 형태 정규식 .일때는 하나의 문자열 ^de 문자의 시작 달러를 쓰면 문자의 끝을 사용하는 것이다.