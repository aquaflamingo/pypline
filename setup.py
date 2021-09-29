from setuptools import find_packages, setup

setup(
    name='pypline',
    packages=find_packages('src'),
    packages_dir={'':'src'},
    version='0.1.0',
    description='Generic transformation pipelines.',
    author='@aquaflamingo',
    license'MIT',
)
