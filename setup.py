from setuptools import setup
setup(name='packaging_test',
      version='0.1',
      description='The funniest joke in the world',
      author='F2L',
      license='Zalo',
      packages=['lppackage', 'package_2'],
      dependency_links=['https://github.com/LocLePhuoc/packaging_test.git'],
      zip_safe=False)