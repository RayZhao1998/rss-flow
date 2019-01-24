## 流程：

- 首先读取存储 RSS 的列表

- 添加所有 RSS 的内容（可能会影响性能）

- 存储所有博客文章名称和 Last update time，放在某个数据结构中。（字典？）

- 对所有文章按照 last update time 进行排序。

- 输出 title 和 date 。暂不考虑美化。

## 环境：

Python

## 模块：

- requests
- feedparser
- flask

## 安装运行

```
pip install -r requirements.txt
python generate_page.py
python get_first_10_blogs.py
```
访问 `127.0.0.1:5000` 即可获取最新10篇博客

## 参考内容：

[如何判断rss是否更新过](https://segmentfault.com/q/1010000002681837)

[Parsing different date formats from feedparser in python?](https://stackoverflow.com/questions/225274/parsing-different-date-formats-from-feedparser-in-python)

先运行 generate_rss.py，后运行 generate_page.py。以后再合并吧。。
