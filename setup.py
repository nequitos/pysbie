from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='pysbie',
    version='1.0.0',
    author='Dzhigit',
    author_email='dzhigitabdualah@gmail.com',
    description='Interact with Sandboxie in Python',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/Dzhigit/pysbie',
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: GNU General Public License Version 3',
        'Operation System :: Windows 7 or higher, 32-bit or 64-bit'
    ],
    keywords='sandboxie python',
    python_requires='>=3.9'
)
