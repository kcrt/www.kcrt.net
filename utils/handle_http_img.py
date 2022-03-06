#!/usr/bin/env python3
import pathlib
from typing import Set
import frontmatter
import datetime
import re
import urllib.request
import os


def download_file(url, datestr):
    print(f"Downloading {url}...")
    filename = os.path.basename(url)
    urllib.request.urlretrieve(url, f"../images/{datestr}_{filename}")
    return f"/images/{datestr}_{filename}"


def main():

    blogimg_re = r'((http://blog.kcrt.net/files/.*?\.(jpg|png|jpeg|JPG|PNG))|(http://d.hatena.ne.jp/images/diary/kcrt/.*?\.(jpg|png|jpeg|JPG|PNG)))'
    blogimg_re = r'((http://blog.kcrt.net/wp-content/uploads/.*?\.(png|jpg|jpeg|JPG|PNG))|(http://hp.vector.co.jp/authors/VA020032/images/.*?\.(png|jpg|jpeg|JPG|PNG)))'

    for file in pathlib.Path("../_posts").glob("*"):
        print(file)
        lines = file.read_text()
        post = frontmatter.loads(lines)
        urls = [m[0] for m in re.findall(blogimg_re, post.content)]
        datestr = post["date"][0:10]
        for url in urls:
            filename = download_file(url, datestr)
            post.content = post.content.replace(
                url, filename)
        lines = frontmatter.dumps(post)
        file.write_text(lines)
        # print(frontmatter.dumps(post))


if __name__ == "__main__":
    main()
