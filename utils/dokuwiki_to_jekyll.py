#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess
import frontmatter  # python-frontmatter
import datetime
import re
import urllib.request
import os
import argparse
from urllib.parse import unquote


def parse_args():
    arg_parser = argparse.ArgumentParser(
        description="Convert Dokuwiki to Jekyll")
    arg_parser.add_argument(
        "-i", "--input", help="dokuwiki's data folder", type=str, required=True)
    arg_parser.add_argument(
        "-o", "--output", help="jekyll's posts, recommend empty dir", type=str, required=True)
    return arg_parser.parse_args()


def do_pandoc(dokuwiki):
    ret = subprocess.run("pandoc -f dokuwiki -t markdown", input=dokuwiki, capture_output=True,
                         text=True, shell=True)
    if ret.returncode != 0:
        print(ret.stderr)
        raise Exception(ret.stderr)
    else:
        return ret.stdout


def main():
    args = parse_args()
    inputpath = Path(args.input)
    for file in (inputpath / "pages").glob("**/*.txt"):
        print(file)
        relpath = file.relative_to(inputpath / "pages")
        parts = list(relpath.parts)  # from tuple
        parts[-1] = parts[-1].replace(".txt", "")
        parts = [unquote(part) for part in parts]
        parts.insert(0, "medicine")

        markdown = do_pandoc(file.read_text())

        post = frontmatter.Post(markdown)
        post["date"] = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S +0900")
        post["tags"] = parts[:-1]
        post["categories"] = post["tags"][:]
        post["tags"].append("scope:kcrt")
        post["tags"].append("AYOR")
        post["title"] = parts[-1]
        post["type"] = "page"

        parts[-1] = parts[-1] + ".md"
        savepath = Path(args.output).joinpath(*parts)
        savepath.parent.mkdir(parents=True, exist_ok=True)
        savepath.write_text(frontmatter.dumps(post))
        print(savepath)

    for file in (inputpath / "media").glob("**/*.*"):
        print(file)
        relpath = file.relative_to(inputpath / "media")
        parts = list(relpath.parts)
        parts = [unquote(part) for part in parts]
        parts[0] = "medicine"
        savepath = Path(args.output).joinpath(*parts)
        savepath.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(file, savepath)


if __name__ == "__main__":
    main()
