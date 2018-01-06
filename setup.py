from setuptools import setup
setup(
  name = 'stock_quote',
  packages = ['stock_quote'], # this must be the same as the name above
  install_requires=[
	'numpy',
	'colorama',
	'influxdb',
	'argparse',
  ],
  version = '0.9.6.2',
  description = 'python script to get stock quotes and calculate gains and losses', 
  author = 'Graham Smith',
  author_email = 'gps1539@gmail.com',
  python_requires='>=3.4',
  scripts = ['stock_quote/stock_quote'],
  license='GPL3',
  url = 'https://github.com/gps1539/stock_quote', # use the URL to the github repo
  download_url = 'https://github.com/gps1539/stock_quote/archive/0.2.tar.gz',
  keywords = ['testing', 'example'], # arbitrary keywords
  classifiers = [],
)
