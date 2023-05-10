total = 0
adult, teenager, kid = 0, 0, 0

try:
    raise Exception("인천과학고등학교")
    humans = int(input("몇 분 이세요? "))
    #ages = [None for _ in range(humans)]
    ages = []
    for i in range(humans):
        ages.append(int(input("나이는? ")))

    print(ages[2])

    for age in ages:
        # 어른 : 20000(>19), 청소년(19~8) 10000, 어린이(<8) 5000
        if age > 19:
            total = total + 20000
            adult += 1
        elif 19 >= age >= 8:
            total = total + 10000
            teenager += 1
        else:
            total = total + 5000
            kid += 1

except IndexError as err:
    print(f"인덱스의 범위를 체크하세요 (0에서 부터 전체 크기-1)\n{err}")
except ValueError as err:
    print(f"입력 값을 확인하세요!\n{err}")
except Exception as other:
    print("무언가 에러가 발생")
    print(other)
else:
    print(f'어른 {adult}명, 청소년 {teenager}명, 어린이 {kid}명의 총 요금은 {total}원 입니다')