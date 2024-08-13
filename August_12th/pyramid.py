# 2. 피라미드
# 맨위부터 1,3,5,7,9개 순서로
# *이 보이는 그림을 출력하는 프로그램을 작성해봅시다

# 이게 내가 짠 코드다.

def pyramid(a):
    for i in range(1, a+1):
        print(" "*(a-i)+"*"*(i*2-1))

pyramid(5)

# 이게 윤희님이 짠 코드다. 본래 코드는 왼쪽으로 붙어서 짜졌는데, print(' ' * (H - i), end='') 파트에서 ' '가 아니라 ''으로 써져서 그런 것 같다.

H = int(input("피라미드의 높이는:"))

for i in range(1, H+1):
    print(' ' * (H - i), end='')
    print('*'*(2*i-1))

# 다음은 출제자 희선님이 짠 코드다. 일단 아무튼 그 결과만 출력할 지, 아니면 경우 및 변형가능성을 많이 열어둘지를 살펴볼 수 있다.

# 우선 아무튼 결과를 만들어내는 코드를 봐보자.

print(" "*4+"*")
print(" "*3+"***")
print(" "*2+"*****")
print(" "*1+"*******")
print("*"*9)

# 그리고 고급 코드를 봐보자.

def print_pyramid(height):
    """
    Prints a pyramid with the given height.
    """
    for i in range(height):
        num_stars = 2 * i + 1
        num_spaces = height - i - 1
        
        line = ' ' * num_spaces + '*' * num_stars
        print(line)

def get_valid_height():
    """
    Prompts the user for a valid pyramid height and returns it.
    """
    while True:
        try:
            # 사용자 입력 받기
            user_input = input("피라미드의 높이를 입력하세요 (양의 정수): ")
            height = int(user_input)
            
            # 입력값 유효성 검사
            if height <= 0:
                print("높이는 1 이상의 양의 정수여야 합니다. 다시 입력해 주세요.")
            else:
                return height
        except ValueError:
            print("유효하지 않은 입력입니다. 정수를 입력해 주세요.")

# 유효한 높이를 입력받고 피라미드 출력
pyramid_height = get_valid_height()
print_pyramid(pyramid_height)

# 나와 윤희님의 코드를 비교하면 차이점은 구구단에서와 비슷하다. 나는 input을 안 썼다.
# 그리고 회선님의 고급 코드와 저급 코드를 비교해보면 그 둘의 차이가 명확하다.
# 저급 코드는 우선 결과를 출력하는 것에 완벽히 치중해있다.
# 고급 코드는 발생가능한 많은 문제들에 대해 대처를 해두고 있고, 응용성도 높다.
# 예를 들자면 오류 가능성에 대해서는 받은 데이터가 1. 자료형의 종류가 맞는지, 2. 자료형이 일치한다면 원하는 값(양의 정수)인지를 확인하고 있다.
# 또한 입력받은 값을 확인하는 함수(get_valid_height())와 받은 값으로 피라미드를 출력하는 함수(print_pyramid())를 구분하고 있다.
# 따라서 응용이 편하다. 예를 들어, 코드의 다른 곳에서 내가 입력 값을 확인하고 싶을 때에는 get_valid_height() 함수를 그대로 가져다 쓸 수 있을 것이다.
# 마지막으로, 코드에 대해 주석이 충실하게 달려있다. 주석 없는 코드는 나중에 재앙으로 돌아올 수 있다. 이게 왜 있는지를 다 새로 해석해야 하니까.

# 구구단과 피라미드 과제에 대한 코드를 살펴보면 알 수 있듯이, 코드를 짤 때 고려해야 하는 사항이 생각보다 많다.이런 것을 잘 익혀두도록 하자.
# 그리고, 짧아도 항상 주석을 다는 습관을 익혀두도록 해보자. 배우는 내용이 어려워질수록 더 시간절약에 도움이 될 것이므로, 꼭 필요하다.