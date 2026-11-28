print("♠ 컴퓨터 용어사전 ♠")

dic = {
    "CPU": "중앙처리장치",
    "RAM": "주기억장치",
    "변수": "데이터를 저장하는 메모리 공간",
    "함수": "특정 작업을 수행하는 코드의 집합"
}

while True:
    word = input("검색할 단어를 입력하세요: ")
    key = word.upper()  # 입력 단어를 대문자로 변환하여 검색
    if key in dic:
        print(f"{word} : {dic[key]}")
    else:
        print(f"{word} : 사전에 없는 단어입니다.")
        
    cont = input("계속 검색하시겠습니까? (y/n): ")
    if cont.lower() != 'y':
        break 