from setuptools import setup, find_packages
import os

version = '1.1dev'

setup(name='silva.pageactions.base',
      version=version,
      description="Action on public pages in Silva.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='silva actions pages',
      author='Infrae',
      author_email='info@infrae.com',
      url='',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['silva', 'silva.pageactions'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'five.grok',
        'grokcore.chameleon',
        'silva.core.interfaces',
        'silva.core.views',
        ],
      )
