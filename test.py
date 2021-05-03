dict_a = {
    "airplane" : "비행기",
    "total" : "총알",
    "enemy" : "적"
}

def warning():
    print("warning!")
    print("warning!")
    print("warning!")
warning()

for i in range(3):
    print("갤러그 게임 시작")
    print("적 비행기 발생")
    print("1. 발사 2. 오른쪽이동 3. 왼쪽이동 ")
    number = int(input("숫자를 입력하세요: "))
    list_a = ["쾅","!","슈슉-"]

    def choice():
        print(number,"선택")

    # 만약에 1번을 누르면 총알 발사
    if number == 1:
        choice()
        print(list_a[0])
        print("총알 발사")
        print(dict_a["airplane"], "에 총알이 맞았다.")
    # 만약에 2번을 누르면 오른쪽
    if number == 2:
        choice()
        print(list_a[1])
        print("오른쪽")
        print(dict_a["enemy"],"발견")
    # 만약에 3번을 누르면 왼쪽
    if number == 3:
        choice()
        print(list_a[2])
        print("왼쪽")
        print(dict_a["total"],"을 피했습니다.")