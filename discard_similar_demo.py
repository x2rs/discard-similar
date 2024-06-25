import difflib

def check_similarity(str1, str2):
    """检查两个字符串的相似度"""
    return difflib.SequenceMatcher(None, str1, str2).ratio()

def remove_similar_strings(strings, similarity_threshold):
    """去除相似度超过阈值的字符串"""
    unique_strings = []
    for s in strings:
        if all(check_similarity(s, us) < similarity_threshold for us in unique_strings):
            unique_strings.append(s)
    return unique_strings

# 示例字符串数组
strings = ["你好世界", "你好世界！", "你好，世界", "你好，世界！"]

# 去除相似度超过90%的字符串
filtered_strings = remove_similar_strings(strings, 0.9)

print(filtered_strings)
