import json
import random

with open('./modified_deposit.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)


for data in json_data:
    # if 'options' in data['model']:
    #     del data['fields']['like_users']
    #     del data['fields']['like_user']

    # if 'like_user' in data['fields']:
    #     del data['fields']['like_user']
    
    if 'products' in data['model']:
        selected_numbers = random.sample(range(1, 10001), k=random.randint(50, 500))
        data['fields']['like_users'] = list(selected_numbers)


with open('./modified_deposit.json', 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=2)
