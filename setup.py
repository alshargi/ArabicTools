import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ArabicTools',
    version='0.0.5',
    author='Dr. Faisal Alshargi',
    author_email='alshargi@hotmail.de',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/alshargi/ArabicTools',
    project_urls = {
        "Bug Tracker": "https://github.com/alshargi/ArabicTools/issues"
    },
    license='MIT',
    packages=['ArabicTools'],
    install_requires=['requests'],
)
