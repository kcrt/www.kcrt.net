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
    # skip urllib.request.urlretrieve(url, f"../images/{datestr}_{filename}")
    return f"/images/{datestr}_{filename}"


def main():

    blogimg_re = r'(https://blog.kcrt.net/files/.*\.(jpg|png|jpeg|JPG|PNG))'

    for file in pathlib.Path(".").glob("*"):
        if file.stem == "process":
            continue
        print(file)
        lines = file.read_text()
        post = frontmatter.loads(lines)
        del post["author"]
        del post["meta"]
        del post["parent_id"]
        del post["password"]
        del post["permalink"]
        del post["published"]
        del post["status"]
        post["tags"].append("旧日記")
        for cat in post["categories"]:
            post["tags"].append(cat)
        del post["categories"]
        # post["layout"] = "olddiary"
        del post["layout"]
        urls = [m[0] for m in re.findall(blogimg_re, post.content)]
        datestr = post["date"].strftime("%Y-%m-%d")
        for url in urls:
            filename = download_file(url, datestr)
            post.content = post.content.replace(
                url, filename)
        filename = "../_posts/" + \
            post["date"].strftime("%Y-%m-%d-%H%M%S") + ".html"
        frontmatter.dump(post, filename)
        # print(frontmatter.dumps(post))


if __name__ == "__main__":
    main()
