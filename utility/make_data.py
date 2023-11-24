# make_data.py 파일은 랜덤한 더미 데이터를 만드는 예시 파일입니다.
# 반드시, 사용하는 필드를 확인한 후 본인의 프로젝트에 맞게 수정하여 진행해야 합니다.

import random

first_nickname_samples = "abcdefghijklmnop"
middle_nickname_samples = "abcdefghijklmnop"
last_nickname_samples = "0123456789"


# 닉네임 랜덤 생성
def random_nickname():
    result = ""
    result += random.choice(first_nickname_samples)
    result += random.choice(middle_nickname_samples)
    result += random.choice(last_nickname_samples)
    return result + str(random.randint(1, 1000))

year = list(map(str, (range(1970, 2005))))
month = [str(i).zfill(2) for i in range(1, 13)]
day = [str(i).zfill(2) for i in range(1, 30)]

def random_birthday():
    result = "" 
    result += random.choice(year)
    result += random.choice(month)
    result += random.choice(day)
    return result

address_list = ['서울특별시 강남구', '서울특별시 영등포구', '서울특별시 관악구', '부산광역시 금정구', '부산광역시 부산진구', '부산광역시 강서구', 
                '대구광역시 달서구', '대구광역시 중구', '인천광역시 동구', '세종특별자치시', '울산광역시 중구', '대전광역시 대덕구', '경기도 성남시 분당구', 
                '경기도 가평군', '경기도 고양시 일산서구', '경상북도 포항시', '경상남도 거제시', '경상남도 김해시', '전라남도 목포시', '전라북도 완주군',
                '강원특별자치도 강릉시', '강원특별자치도 속초시', '충청북도 단양군', '충청남도 당진시', '제주특별자치도 제주시']

bank_list = [
    '우리은행', '한국스탠다드차타드은행', '대구은행', '부산은행',
    '광주은행', '제주은행', '전북은행', '경남은행', '중소기업은행',
    '한국산업은행', '국민은행', '신한은행', '농협은행주식회사',
    '하나은행', '수협은행', '주식회사 케이뱅크',
    '주식회사 카카오뱅크', '토스뱅크 주식회사'
    ]

# json 파일 만들기
import json
from collections import OrderedDict

file1 = OrderedDict()
file2 = OrderedDict()

username_list = []
birthday_list = []

N = 10000
i = 0

while i < N:
    rn = random_nickname()
    if rn in username_list:
        continue
    
    bd = random_birthday()
    username_list.append(rn)
    birthday_list.append(bd)
    i += 1


# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = './accounts.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    
    for i in range(N):
        # 랜덤한 데이터를 삽입
        file1["model"] = "accounts.user"
        file1["pk"] = i+1
        file1["fields"] = {
            'username': username_list[i],  # 유저 이름 랜덤 생성
            'password': "1234",
            'last_login': "2023-11-20T03:15:18.727Z",
            'first_name': "",
            'last_name': "",
            'email': "asdf@asdf.com",
            'date_joined': "2023-11-20T00:12:01.568Z",
            'is_active': True,
            'is_staff': False,
            'is_superuser': False,
            'groups': [],
            'user_permissions': []
        }

        json.dump(file1, f, ensure_ascii=False, indent="\t")
        if i != N:
            f.write(',')

    for i in range(N):
        # 랜덤한 유저 상세 정보를 삽입
        file2["model"] = "accounts.detailuser"
        file2["pk"] = i+1
        file2["fields"] = {
            'user': i+1, 
            'nickname': "아무개",
            'birthday': birthday_list[i],
            'gender': random.choice(['남성','여성']),
            'address': random.choice(address_list),
            'main_bank': random.choice(bank_list),
            'salary': random.randrange(0, 150000000, 1000000), # 0 ~ 1억 5천, 백만 단위
            'asset': random.randrange(0, 1500000000, 10000000), # 0 ~ 15억, 천만 단위
            'goal': random.choice(['내 집 마련', '내 차 마련', '여행 경비', '목돈 마련']),
        }

        json.dump(file2, f, ensure_ascii=False, indent="\t")
        if i != N-1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')