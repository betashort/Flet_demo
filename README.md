# Flet_demo

## Python環境

### uvのインストール

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```sh
uv --version
```

### pythonのインストール

```sh
uv python list
```

```sh
uv py install 3.xx
```

### デフォルトのPythonの設定

```sh
uv py global 3.xx
```

### 仮想環境の作成

```sh
uv venv .venv
```

### パッケージのインストール・アンインストール

```sh
uv pip install xxxx

uv pip uninstall xxx
```

## Pythonライブラリ

```sh
uv pip install jupyter ipykernel
```

```sh
uv pip isntall flet flet-desktop
```