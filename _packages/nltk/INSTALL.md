* Rev.1: 2020-05-25 (Mon)
* Draft: 2017-01-10 (Tue)
# Install NLTK and Necessary Datasets/Models

## Install NLTK
```bash
$ sudo pip install -U nltk
# pip install --user -U nltk # From the official website, but I'm iffy about it.
```
To verify the installation, run:
```bash
$ python -c "import nltk"
```
For details, refer to [Installing NLTK](https://www.nltk.org/install.html).

## If you need an up-to-the-minute version, run:
```bash
$ git clone https://github.com/nltk/nltk
```
## Download the datasets/models
After installing the NLTK package, do install the necessary datasets/models for specific functions to work.
```bash
$ python -c "import nltk; nltk.download(‘popular’)"
# or
$ python -m nltk.downloader popular
```
If you know a specific dataset/model, replace `popular` to your interested dataset/model.
