from setuptools import setup

setup(name='lppackage',
      version='0.1',
      description='The funniest joke in the world',
      author='F2L',
      license='Zalo',
      packages=['lppackage'],
      dependency_links=['https://github.com/LocLePhuoc/packaging_test.git'],
      zip_safe=False)