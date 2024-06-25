SIMILARITY_THRESHOLD = 0.9 # 相似度超过90%就丢弃

import json

import difflib
from tqdm import tqdm

def check_similarity(str1, str2):
    """检查两个字符串的相似度"""
    return difflib.SequenceMatcher(None, str1, str2).ratio()

def check_data_similarity(element1, element2):
    """检查两个数据的相似度，依据output字段"""
    return check_similarity(element1["output"], element2["output"])

def remove_similar_data(data, similarity_threshold):
    """去除相似度超过阈值的数据"""
    unique_data = []
    for datum in tqdm(data, desc="处理进度"):
        if all(check_data_similarity(datum, ud) < similarity_threshold for ud in unique_data):
            unique_data.append(datum)
    return unique_data

with open("filled_dataset.json", "r", encoding='utf-8') as f:
    raw_array = json.load(f)

filtered_array = remove_similar_data(raw_array, SIMILARITY_THRESHOLD)

with open("filtered_dataset.json", "w", encoding='utf-8') as f:
    json.dump(filtered_array, f, ensure_ascii=False, indent=4)