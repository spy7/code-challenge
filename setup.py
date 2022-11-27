from setuptools import find_packages, setup

setup(
    name="code_challenge",
    version="0.1.0",
    description="A stock recommendation package",
    author="Carlos",
    author_email="carlosspy@gmail.com",
    packages=find_packages(exclude=("tests",)),
    entry_points={
        "console_scripts": [
            "code_challenge=code_challenge.scripts.code_challenge:main"
        ],
    },
    install_requires=["requests>=2.28.1", "pandas>=1.5.2"],
)
