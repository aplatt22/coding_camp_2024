import setuptools 

setuptools.setup(
  name = 'mylibrary',
  description = 'test library',
  packages = ['mylibrary'] #setuptools.find_packages(),
  python_requires='>=3.6',
  install_requires=['setuptools'],
  include_package_data=True,
)