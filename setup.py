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
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operation System :: Windows 10'
    ],
    keywords='sandboxie python',
    python_requires='>=3.9'
)
