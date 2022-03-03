#!/usr/bin/env python3
import pathlib
from typing import Set
import frontmatter
import datetime
import re
import urllib.request
import os


def main():

    for file in pathlib.Path("../_oldposts").glob("*.html"):
        print(file)
        lines = file.read_text()
        post = frontmatter.loads(lines)
        post["data"] = post["date"].strftime("%Y-%m-%d %H:%M:%S +0900")
        filename = "../_posts/" + file.stem + ".html"
        frontmatter.dump(post, filename)
        # print(frontmatter.dumps(post))


if __name__ == "__main__":
    main()
