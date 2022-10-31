from setuptools import setup

setup(
    name='kavalkade',
    install_requires=[
        'horseman',
        'knappe',
        'knappe_deform'
    ],
    extras_require={
        'test': [
            'WebTest',
            'pytest',
            'pyhamcrest'
        ]
    }
)