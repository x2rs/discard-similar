# discard_similar.py

用 [`ChatGLM`](https://chatglm.cn/) 生成了 `discard_similar_demo.py`，改进为 `discard_similar.py`，该算法的基本思路如下：

1. 使用 `difflib` 判断两个字符串的相似度（区间为0.0-1.0）
2. 若相似度超过 `similarity_threshold`（取值区间为0.0-1.0，默认为0.9）则丢弃，否则存入新数组
3. 使用 `tqdm` 进度条显示进度

