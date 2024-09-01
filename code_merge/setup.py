from setuptools import setup, find_packages

setup(
    name='code_merge',
    version='0.1',
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'code_merge=code_merge.main:main',
        ],
    },
    author='Ankhly Chamstin',
    author_email='chamstin@gmail.com',
    description='A tool to consolidate code files from a directory',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/code_merge',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
