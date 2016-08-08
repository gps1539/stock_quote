# stock_quote
python script for getting stock quotes and calculating gains and losses.

I wrote this to learn python, so expect bugs. Feedback and suggestions welcome.

usage: stock_quote.py [-h] [--add ADD [ADD ...]] [--delete DELETE]
                      [--portfolio PORTFOLIO]

optional arguments:
  -h, --help            show this help message and exit
  --add ADD [ADD ...]   add a symbol, the quantity held and the price paid
  --delete DELETE       delete a symbol
  --portfolio PORTFOLIO
                        choose a portfolio
  
When adding the stock symbol, quantity and price are required

Allows multiple portfolios to be created and used. They are created as hidden directories named after the portfolio in the user's home directory.

Program will create 2 files in the portfolio directory to store portfolio info (cost.npy and stocks.npy)

For continuous updates watch (bash) is useful:
watch -n 5 --color stock_quote.py
