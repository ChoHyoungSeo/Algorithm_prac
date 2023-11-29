from collections import defaultdict

def solution(clothes):
    # id를 기준으로 물품 그룹화
    item_dict = defaultdict(list)
    for item, id_ in clothes:
        item_dict[id_].append(item)

    # 각 id 그룹별 선택지의 수 계산 (물품 수 + 1)
    num_choices = [len(items) + 1 for items in item_dict.values()]

    # 총 조합의 수 계산
    total_combinations = 1
    for choices in num_choices:
        total_combinations *= choices

    # 공집합 하나를 빼고 반환
    return total_combinations - 1