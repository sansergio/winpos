from setuptools import setup, find_packages
setup(
    name="winpos",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pywin32>=227",
        "psutil>=5.6.7"
        ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'winpos=winpos:main',
        ],
    },
)