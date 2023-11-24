import random
import json

# 쉘에서 python -Xutf8 manage.py dumpdata compare_deposit --indent=2 > deposit.json 부터 하고 코드 실행

with open('./deposit.json', 'r', encoding="UTF-8") as f:
    json_data = json.load(f)


for data in json_data:
    if 'products' in data['model']:
        selected_numbers = random.sample(range(1, 10001), k=random.randint(50, 500))
        data['fields']['like_users'] = list(selected_numbers)


with open('./modified_deposit.json', 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=2)
