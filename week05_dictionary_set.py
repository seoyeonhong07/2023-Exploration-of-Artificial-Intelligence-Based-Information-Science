subjects_list = [
    ['김영숙', '국어'],
    ['남동호', '수학'],
    ['김성훈', '수학'],
    ['양수진', '영어'],
    ['이지현', '정보'],
    ['김병수', '물리']
]

subjects_list = dict(subjects_list)
print(subjects_dict)
# print(subjects_dict['트럼프'])  # KeyError
print(subjects_dict.get('트럼프'))  # return None
print(subjects_dict.get('이지현'))
print(subjects_dict['트럼프'])
