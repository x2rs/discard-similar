# discard_similar.py

## How to use

1. 将 `filled_dataset.json` 放入根目录。
2. 修改 `discard_similar.py` 的 `SIMILARITY_THRESHOLD` 的值，默认为 `0.9`，表示相似度超过90%就丢弃。
3. 运行 `discard_similar.py`，进度条结束后会生成 `filtered_dataset.json`。
4. 运行 `dataset_reader.py`，输出两个数据集的元素个数。

## Details

用 [`ChatGLM`](https://chatglm.cn/) 生成了 `discard_similar_demo.py`，改进为 `discard_similar.py`，该算法的基本思路如下：

1. 使用 `difflib` 判断两个数据的`output`字段的相似度（区间为0.0-1.0）。
2. 若相似度超过 `similarity_threshold`（取值区间为0.0-1.0，默认为0.9）则丢弃，否则存入新数组。
3. 使用 `tqdm` 进度条显示进度。

