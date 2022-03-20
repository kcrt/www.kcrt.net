---
date: 2022-03-08 09:16:32 +0900
update: 2022-03-20 20:20:00 +0900
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
$ pip install -U pip

$ SYSTEM_VERSION_COMPAT=1 GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1 GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1 pip3 install grpcio
$ HDF5_DIR=`brew --prefix hdf5` pip3 install tensorflow-macos tensorflow-metal
$ echo "import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10)
model.evaluate(x_test,  y_test, verbose=2)
" > tf_test.py

$ python3 tf_test.py
```

- Xcode入れて…とかその辺の前準備の説明は省略
- これで無理になってたら教えてください or Pull requestお願いします

### 2021-03-20 追記
- サンプル実行コード追加
- h5pyとhomebrewのhdf5のバージョンが不一致だと動かないので、そのときは`--no-binary=h5py`で`h5py`をインストール
