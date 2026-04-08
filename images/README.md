# Images

当前仓库快照不包含原始图片文件。

如果你拥有经授权的图片数据，请按照以下结构放置：

```text
images/<category>/<subcategory>/positive/<filename>
```

说明：

- 为兼容当前标注文件，路径中仍保留 `positive/` 这一历史目录名。
- 这里的 `positive/` 是发布结构的一部分，并非要求额外提供其他对照目录。
- `annotations/*.jsonl` 中的 `image_path` 默认采用这一相对路径格式。
