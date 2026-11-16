"""把 index-source.html 里的相对图片路径内嵌成 base64，生成可直接双击打开的 index.html。
改完 index-source.html 后重新运行本脚本即可。"""
import base64
from pathlib import Path

BASE = Path(__file__).resolve().parent

IMAGES = {
    "assets/portrait.jpg": "image/jpeg",
    "assets/works/fenchui-01.png": "image/png",
    "assets/works/fenchui-02.png": "image/png",
    "assets/works/fenchui-03.png": "image/png",
}

html = (BASE / "index-source.html").read_text(encoding="utf-8")
for rel, mime in IMAGES.items():
    raw = (BASE / rel).read_bytes()
    uri = "data:%s;base64,%s" % (mime, base64.b64encode(raw).decode("ascii"))
    token = 'src="%s"' % rel
    if token not in html:
        raise SystemExit("找不到图片引用：" + token)
    html = html.replace(token, 'src="%s"' % uri)

out = BASE / "index.html"
out.write_text(html, encoding="utf-8")
print("生成 %s（%s 字节）" % (out.name, out.stat().st_size))
