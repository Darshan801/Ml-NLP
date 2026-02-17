from setuptools import find_packages , setup


setup(
    name="QAsystem with haystack",
    version="0.0.1",
    author="hello",
    author_email="hello@gmail.com",
    packages=find_packages(),
    install_requires=["pinecone-haystack","haystack-ai","fastapi","uvicorn","python-dotenv","pathlib"]
)