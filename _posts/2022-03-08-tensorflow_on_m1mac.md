---
date: 2022-03-08 09:16:32 +0900
tags:
    - プログラミング
    - mac
title: TensorFlow を M1 Macで動かす
type: post
---

以前よりは大分簡単にはなりましたが、それでもまだ一癖あるようです……

## 公式の方法

- [Getting Started with tensorflow-metal PluggableDevice](https://developer.apple.com/metal/tensorflow-plugin/)
- Miniforgeを使います

## conda使いたくないときの方法

```bash
$ uname -a
Darwin aluminum 21.3.0 Darwin Kernel Version 21.3.0: Wed Jan  5 21:37:58 PST 2022; root:xnu-8019.80.24~20/RELEASE_ARM64_T6000 arm64

$ brew install hdf5 openssl@3 zlib
# LDFLAGSなどを適切に設定 kcrt/dotfiles/.zshrc https://github.com/kcrt/dotfiles/blob/main/.zshrc 参照

$ asdf install python 3.9.9 # 3.10だと動かないかも

# ARMバイナリであることを確認
$ lipo -archs `which python3`
arm64

# venv
$ mkdir mac-tf; cd mac-tf
$ asdf local python 3.9.9
$ python3 -m venv .
$ source bin/activate

$ brew install tensorflow
$ SYSTEM_VERSION_COMPAT=1 GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1 GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1 pip3 install grpcio
$ HDF5_DIR=`brew --prefix hdf5` pip3 install tensorflow-macos tensorflow-metal
```

- Xcode入れて…とかその辺の前準備の説明は省略
- これで無理になってたら教えてください or Pull requestお願いします
