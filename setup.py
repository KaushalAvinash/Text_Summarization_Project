from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPONAME = "Text_Summarization_Project"
AUTHOR_USER_NAME = "KaushalAvinash"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "avinashkaushal763@gmail.com"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarization Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}/issues"
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),    
)