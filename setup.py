import setuptools

with open(README.md,'r',encoding = "utf-8") as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = "cnnClassifier"
AUTHOR_USER_NAME = "entbappy"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "oforibright4u14@gmail.com"

setuptools.setup(   
    name = SRC_REPO,
    version = __version__ ,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for CNN app"),
    long_description_content = "text/markdown",
    url = f"https://github.com{AUTHOR_USER_NAME}/{REPO_NAME}",
)