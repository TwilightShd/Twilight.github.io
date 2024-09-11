import markdown

# 读取Markdown文件
with open('readme.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 将Markdown转换为HTML
html = markdown.markdown(text)

# 保存HTML文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('read.html', 'w', encoding='utf-8') as f:
    f.write(html)