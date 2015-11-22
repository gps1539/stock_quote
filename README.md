# stock_quote
python script for getting stock quotes from yahoo and calculating gains and losses.

I wrote this to learn python, so expect issues and bugs. Feedback and suggestions welcome.

usage: stock_quote.py [-h] [--add ADD [ADD ...]] [--delete DELETE]

optional arguments:
  -h, --help           show this help message and exit
  --add ADD [ADD ...]  add a symbol, the quantity held and the price paid
  --delete DELETE      delete a symbol
  
  
when adding the stock symbol, quantity and price are required

Program will create 2 files in the installed directory to store your portfolio info (cost.npy and stocks.npy)
