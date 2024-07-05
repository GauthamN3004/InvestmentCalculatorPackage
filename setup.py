from setuptools import setup, find_packages

setup(
    name='investment_calculator',
    author='Gautham',
    description='This package is used to calculate your investment returns.',
    version = "1.1.0", 
    url='https://github.com/GauthamN3004/InvestmentCalculatorPackage',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=['pandas'],
    # extras_require={
    #     'dev': ['check-manifest'],
    #     # 'test': ['coverage'],
    # },
)
