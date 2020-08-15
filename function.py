from .functions import *

x = "x"

### 언어 변경 ###
language = ["English"]


def Korean():
    del language[:]
    language.append("Korean")
    print("언어선택 : 한국어")


def korean():
    Korean()


def 한국어():
    Korean()


def English():
    del language[:]
    language.append("English")
    print("language selection : English")


def english():
    English()


### start messege ###
def messege():
    print("-" * 60)
    if language == ["English"]:
        print("1. Defining f(x):")
        print(
            "Type 'fx()', and then Type coefficients for each terms (descending order)"
        )
        print("(Separate by spacing, Scope: rational-number)\n")

        print("2. Getting a value of function")
        print(
            "Type f(x), df(x), F(x) or dF(x) with a substitute of some rational-num in x, a, b"
        )
        print(
            "if you wanna type infinitely decimal, attach ' to both sides of the each of x, a, b value."
        )
    elif language == ["Korean"]:
        print("1. f(x) 정의하기")
        print("'f(x)'를 입력한 다음, 각 항의 계수들을 입력해라 (내림차순)")
        print("띄어쓰기로 항 구분, 범위: 유리수\n")

        print("2. 함수값 구하기")
        print("x, a, b 에 유리수를 대입하여 f(x) 또는 df(x), F(x), dF(a, b)를 입력해라")
        print("만약 무한소수를 입력하고 싶다면, x, a, b 각각 양옆에 '를 붙여라")
    print("ex) f('1/3'), df(2), F(x), dF(1.5, 2.5)\n")
    print("'help()' helps you, language : English(), Korean()")
    print("-" * 60)


messege()
# coefficients: 계수, term: 항, descending order 내림차순, fraction: 분수


### help ###
def help():
    print("language selection : korean(), english()")
    if language == ["English"]:
        print("starting messege: messege()\n")
        print("defining function f : fx()\n")
        print("f('x' or rational-number), df('x' or r-n), 'F(x)', dF(r-n, r-n) :")
        print("f(x), differential, integral-indef and integral-def\n")
        print("Can define g(x) also (put g in place of f)")
    elif language == ["Korean"]:
        print("시작 메세지: messege()\n")
        print("fraction(a, b) 뜻 : a/b\n")
        print("함수 f 정의 : fx()\n")
        print("f('x' or 유리수), df('x' or 유리수), 'F(x)', dF(유리수, 유리수)) :")
        print("f(x), 미분, 부정적분, 정벅분\n")
        print("함수 g도 정의 가능 (f 자리에 g를 넣어서)")


## 함숫값 구하기 ##
def value_of_function(x, coefs):
    for n in range(len(coefs)):  # n : n차항의 계수
        if n == 0:
            y = coefs[0]
        else:
            y += coefs[n] * x ** n
    return y


### 유리 함수 f 추가 ###

f_coefs = []
df_coefs = []
F_coefs = []
f_function = []

## 함수 f(x) 정의 ## (각 항의 계수를 입력받아 위에 list 형태로 저장)
def fx():
    try:
        if language == ["English"]:
            list = input("coefficients: ").split()
        elif language == ["Korean"]:
            list = input("계수들: ").split()

        del f_coefs[:]
        f_coefs.extend(Change_strs_fractions(list))
        f_coefs.reverse()  # 오름차순 (계산, 출력에 용이)

        del f_function[:]
        f_function.append(Change_human_tailored_expression(f_coefs))
        print("f(x) =", f_function[0])  # 함수식 출력

    except:
        if list == []:
            if language == ["English"]:
                print("'Error: nothing inputed'")
            elif language == ["Korean"]:
                print("'오류: 입력 없음'")
        else:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님'")


## f(x) 함숫값 ##
def f(x):
    try:
        x = Change_str_fraction(str(x))
        return value_of_function(x, f_coefs)  # 함숫값 계산, 출력

    except:
        if f_coefs == []:
            if language == ["English"]:
                print("'Error: f(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: f(x)가 정의되지 않음'")
        elif x == "x":
            print("f(x) =", f_function[0])
        else:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님'")


## f(x) 미분, 값 ##
def df(x):
    try:
        if len(f_coefs) == 1:
            return 0

        del df_coefs[:]
        for n in range(len(f_coefs)):  # 각 항에서
            df_coefs.append(n * f_coefs[n])  # 새 계수 = 차수 x 계수
        del df_coefs[0]  # 상수항 사라짐

        x = Change_str_fraction(str(x))
        return value_of_function(x, df_coefs)

    except:
        if f_coefs == []:
            if language == ["English"]:
                print("'Error: f(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: f(x)가 정의되지 않음'")
        elif x == "x":
            print("df(x)/dx =", Change_human_tailored_expression(df_coefs))
        else:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님'")


## f(x) 부정적분 ##
def F(x):
    try:
        if f_coefs == []:
            raise
        if x != "x" and isTrue_rational_num(str(x)) == False:
            raise

        if f_coefs[0] == 0 and len(f_coefs) == 1:  # 항이 0 하나면 0 출력
            return 0

        del F_coefs[:]
        for n in range(len(f_coefs)):  # 각 항에서
            F_coefs.append(f_coefs[n] / (n + 1))  # 새 계수 = 계수 / (차수+1)

        F_coefs.reverse()
        F_coefs.append("C")  # 적분상수 C 추가
        F_coefs.reverse()
        print("F(x) = " + Change_human_tailored_expression(F_coefs))

    except:
        if f_coefs == []:
            if language == ["English"]:
                print("'Error: f(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: f(x)가 정의되지 않음'")
        elif x != "x" and isTrue_rational_num(x) == False:
            if language == ["English"]:
                print("'Error: not 'x' or rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 'x' 또는 유리수가 아님'")


## f(x) 정적분 ##
def dF(range_a, range_b):
    try:
        if f_coefs == []:
            raise
        if isTrue_rational_nums([str(range_a), str(range_b)]) == False:
            raise  # 유리수가 아니면 예외

        a = Change_str_fraction(str(range_a))  # a, b를 분수꼴로 바꾸기
        b = Change_str_fraction(str(range_b))

        value = 0
        del F_coefs[:]
        for n in range(len(f_coefs)):
            F_coefs.append(f_coefs[n] / (n + 1))
            F_coefs[n] = F_coefs[n] * (b ** (n + 1) - a ** (n + 1))
            value += F_coefs[n]  # value = 각 항을 정적분하여 모두 더한 값
        return value

    except:
        if f_coefs == []:
            if language == ["English"]:
                print("'Error: f(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: f(x)가 정의되지 않음'")
        elif isTrue_rational_nums([str(range_a), str(range_a)]) == False:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님'")


### 유리 함수 g 추가 ### (똑같은 코드)

g_coefs = []
dg_coefs = []
G_coefs = []
g_function = []

## 함수 g(x) 정의 ##
def gx():
    try:
        if language == ["English"]:
            list = input("coefficients: ").split()
        elif language == ["Korean"]:
            list = input("계수들: ").split()

        del g_coefs[:]
        g_coefs.extend(Change_strs_fractions(list))
        g_coefs.reverse()

        del g_function[:]
        g_function.append(Change_human_tailored_expression(g_coefs))

        print("g(x) =", g_function[0])
        return True

    except:
        if list == []:
            if language == ["English"]:
                print("'Error: nothing inputed'")
            elif language == ["Korean"]:
                print("'오류: 입력 없음'")
        else:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님'")


## g(x) 함숫값 ##
def g(x):
    try:
        x = Change_str_fraction(str(x))
        return value_of_function(x, g_coefs)

    except:
        if g_coefs == []:
            if language == ["English"]:
                print("'Error: g(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: g(x)가 정의되지 않음'")
        elif x == "x":
            print("g(x) =", g_function[0])
        else:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("오류: 유리수가 아님")


## g(x) 미분, 값 ##
def dg(x):
    try:
        if len(g_coefs) == 1:
            return 0

        del dg_coefs[:]
        for n in range(len(g_coefs)):  # 각 항에서
            dg_coefs.append(n * g_coefs[n])  # 새 계수 = 차수 x 계수
        del dg_coefs[0]  # 상수항 사라짐

        x = Change_str_fraction(str(x))
        return value_of_function(x, dg_coefs)

    except:
        if g_coefs == []:
            if language == ["English"]:
                print("'Error: g(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: g(x)가 정의되지 않음'")
        elif x == "x":
            print("dg(x)/dx =", Change_human_tailored_expression(dg_coefs))
        else:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님'")


## g(x) 부정적분 ##
def G(x):
    try:
        if g_coefs == []:
            raise
        if x != "x" and isTrue_rational_num(str(x)) == False:
            raise

        if g_coefs[0] == 0 and len(g_coefs) == 1:
            return 0

        del G_coefs[:]
        for n in range(len(g_coefs)):
            G_coefs.append(g_coefs[n] / (n + 1))

        G_coefs.reverse()
        G_coefs.append("C")
        G_coefs.reverse()
        print("G(x) = " + Change_human_tailored_expression(G_coefs))

    except:
        if g_coefs == []:
            if language == ["English"]:
                print("'Error: g(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: g(x)가 정의되지 않음'")
        elif x != "x" and isTrue_rational_num(x) == False:
            if language == ["English"]:
                print("'Error: not 'x' or rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 'x' 또는 유리수가 아님'")


## g(x) 정적분 ##
def dG(range_a, range_b):
    try:
        if g_coefs == []:
            raise
        if isTrue_rational_nums([str(range_a), str(range_b)]) == False:
            raise  # 유리수가 아니면 예외

        a = Change_str_fraction(str(range_a))  # a, b를 분수꼴로 바꾸기
        b = Change_str_fraction(str(range_b))

        value = 0
        del G_coefs[:]
        for n in range(len(g_coefs)):
            G_coefs.append(g_coefs[n] / (n + 1))
            G_coefs[n] = G_coefs[n] * (b ** (n + 1) - a ** (n + 1))
            value += G_coefs[n]  # value = 각 항을 정적분하여 모두 더한 값
        return value

    except:
        if g_coefs == []:
            if language == ["English"]:
                print("'Error: g(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: g(x)가 정의되지 않음'")
        elif isTrue_rational_nums([str(range_a), str(range_a)]) == False:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님'")


## Tutorial ##

# while True:
#     print('-' * 60)
#     a = input()
#     if a == 'break':
#         break

#     ## 함수 정의 명령어 'fx()'를 입력 ##
#     elif a == 'fx()':

#         # fx() 실행
#         fx()

#     ## 함수 정의를 먼저 했는지 검사 ##
#     elif f_coefficients == []:
#         print(f_function[0])
#         print("Type 'fx()' first!")

#     ## x값 대입 명령어 f(x)를 쳤을 때 ##
#     elif 'f(' in a and ')' in a and a.index('f(') == 0 and a.index(')') == len(a)-1:

#         # x값만 추출 #
#         x = a.replace('f(', '').replace(')', '')

#         # "f(x)"라고 쳤을 때:
#         if x == 'x':
#             print('f(x) =', f_function[0])

#         else: # f(x) 값 출력 #
#             print(f(x))

#     ## 이상한 걸 입력 ##
#     else:
#         print("Type fx(), f(rational-number), or 'f(x)'!")