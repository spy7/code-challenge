from setuptools import find_packages, setup

setup(
    name="code_challenge",
    version="0.1.0",
    description="A stock recommendation package",
    author="Carlos",
    author_email="carlosspy@gmail.com",
    packages=find_packages(exclude=("tests",)),
    entry_points={
        "console_scripts": ["cc_config=code_challenge.api.config:config"],
    },
    install_requires=["requests>=2.28.1"],
)
