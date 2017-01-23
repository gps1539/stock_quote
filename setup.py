from distutils.core import setup
setup(
  name = 'stock_quote',
  packages = ['stock_quote'], # this must be the same as the name above
  version = '0.1',
  description = 'gets stock quotes, calculating gains and losses and optionally recording to a time series database (influxdb)',
  author = 'Graham Smith',
  author_email = 'gps1530@gmail.com',
  url = 'https://github.com/gps1539/stock_quote', # use the URL to the github repo
  download_url = 'https://github.com/gps1539/stock_quote/tarball/0.1', # I'll explain this in a second
  keywords = ['stocks'], # arbitrary keywords
  classifiers = [],
)
