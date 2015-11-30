# stock_quote
python script for getting stock quotes from yahoo and calculating gains and losses.

I wrote this to learn python, so expect bugs. Feedback and suggestions welcome.

usage: stock_quote.py [-h] [--add ADD [ADD ...]] [--delete DELETE]

optional arguments:
  -h, --help           show this help message and exit
  --add ADD [ADD ...]  add a symbol, the quantity held and the price paid
  --delete DELETE      delete a symbol
  
  
when adding the stock symbol, quantity and price are required

Program will create 2 files in the users home directory to store portfolio info (cost.npy and stocks.npy)

For continuous updates watch (bash) is useful:
watch -n 5 --color stock_quote.py
