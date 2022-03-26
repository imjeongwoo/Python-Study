def 서브루틴(a, b):
    print('서브 루틴 시작')
    c = a + b
    print(f'c = {c}, 서브 루틴 종료')

def 메인루틴():
    print('메인 루틴 시작')
    서브루틴(1, 2)
    print('메인 루틴 다시 시작')

메인루틴()   