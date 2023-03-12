from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='Sort files in your folder',
      author='Maksy',
      packages=find_namespace_packages(),
      include_package_data=True,
      entry_points={'console_scripts':['sort_folder = clean_folder.sort:main']})