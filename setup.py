from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='scanf',
    version='0.2.0',
    author='Dawnfz-Lenfeng',
    author_email='lingfengbut@qq.com',
    description='A scanf for python based on RE',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    license="MIT",
    install_requires=[],
    url='https://github.com/Dawnfz-Lenfeng/scanf'
)
