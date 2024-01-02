import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='FaisalARAtools',
    version='0.0.1',
    author='Dr. Faisal Alshargi',
    author_email='alshargi@hotmail.de',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/alshargi/FaisalARAtools',
    project_urls = {
        "Bug Tracker": "https://github.com/alshargi/FaisalARAtools/issues"
    },
    license='MIT',
    packages=['FaisalARAtools'],
    package_data={'FaisalARAtools': ['models/*.txt', 'models/*.sav']}, 
    install_requires=['requests'],
)
