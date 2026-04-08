# Images

当前仓库快照不包含原始图片文件。

如果你拥有经授权的图片数据，请按照以下结构放置：

```text
images/<category>/<subcategory>/positive/<filename>
```

说明：

- 公开版 SmuggleBench 只包含违规样本。
- 为兼容已有标注文件，路径中仍保留 `positive/` 这一历史目录名。
- `annotations/*.jsonl` 中的 `image_path` 默认采用这一相对路径格式。
