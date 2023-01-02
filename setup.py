import re
import setuptools

with open("__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

if __name__ == "__main__":
    setuptools.setup(
        name="autoindent",
        version=version,
        url="https://github.com/AvesterHupper/StringIndent",
        author="AvesterHupper",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11"
        ],
        python_requires="~=3.7",)
