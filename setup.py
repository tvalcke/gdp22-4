from setuptools import setup, find_packages

setup(
    name='super_outil_python',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.28.0',
        'numpy>=1.24.0',
    ],
    extras_require={
        'dev': [
            'flake8>=6.1.0',
            'pydocstyle>=6.2.0',
        ],
        'test': [
            'pytest>=7.1.0',
        ],
    },
    python_requires='>=3.9',
    author='Léo Dupont',
    author_email='leo.dupont@example.com',
    description='Un super outil Python pour des tâches incroyables.',
)
