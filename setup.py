from setuptools import setup

setup(
    name='kavalkade',
    install_requires=[
        'horseman',
        'knappe',
        'knappe_deform',
        'tinydb',
        'minicli'
    ],
    extras_require={
        'test': [
            'WebTest',
            'pytest',
            'pyhamcrest'
        ]
    }
)