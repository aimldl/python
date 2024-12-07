* Rev.1: 2021-08-06 (Fri)
* Draft: 2020-11-09 (Mon)

# Installation
## Summary
* 설치 스크립트 [install_konlpy](bash_scripts/install_konlpy)를 실행합니다.

```bash
# 로컬에 내용을 복사해서 설치 스크립트를 만든 후 실행합니다.
$ chmod +x install_konlpy
$ ./install_konlpy
```

## Ubuntu
아래의 명령어를 실행하면 설치가 진행됩니다. 아나콘다 가상환경에서 실행할 경우 목적으로 하는 가상환경 안에서 실행해야 합니다. 예를 들어, `korean_news_extraction`가 원하는 가상환경의 이름일 경우, 이 환경 안에서 실행해야 합니다.


아래 명령어는 설치 스크립트 [install_konlpy](bash_scripts/install_konlpy)와 동일합니다.

```bash
# 로컬에 내용을 복사해서 설치 스크립트를 만든 후 실행합니다.
$ chmod +x install_konlpy
$ ./install_konlpy
```

```bash
#!/bin/bash
# install_konlpy

sudo apt install -y g++ openjdk-8-jdk python3-dev python3-pip curl
python3 -m pip install --upgrade pip
python3 -m pip install konlpy

# Optionally install mecab
sudo apt-get install curl git
bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
```

mecab까지 설치가 마무리 되면 다음과 같은 메세지가 생성됩니다.

```bash
  ...
Successfully built mecab-python
Installing collected packages: mecab-python
Successfully installed mecab-python-0.996-ko-0.9.2
Done.
(korean_news_extraction) $
```

아래는 KoNLPy 공식 페이지의 설치 관련 내용입니다.

> Supported: Xenial(16.04.3 LTS), Bionic(18.04.3 LTS), Disco(19.04), Eoan(19.10)
>
> 1. Install dependencies
>
>    > ```bash
>    > # Install Java 1.8 or up
>    > $ sudo apt install -y g++ openjdk-8-jdk python3-dev python3-pip curl
>    > ```
>
> 2. Install KoNLPy
>
>    > ```bash
>    > $ python3 -m pip install --upgrade pip
>    > $ python3 -m pip install konlpy       # Python 3.x
>    > ```
>
> 3. Install MeCab (*optional*)
>
>    > ```bash
>    > $ sudo apt-get install curl git
>    > $ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
>    > ```
>
> Source: https://konlpy.org/en/latest/install/#ubuntu

