from setuptools import setup,find_packages

setup(
    author="Arief Akbar Hidayat",
    description="A NLP Package for Bahasa Indonesia",
    name="straycat",
    packages=find_packages(include=["straycat.*"]),
    version="0.1.0",
    # install_requires=['numpy', 'pandas','nltk','sastrawi'],
    python_requires=">=3.6.*"
)