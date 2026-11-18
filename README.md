## stock_quote

## Overview
stock quote is a python script for getting stock quotes, news, calculating gains and losses. Usage requires an account (free) from www.alphavantage.co

## Usage
```
sage: stock_quote [-h] [-a ADD [ADD ...]] [-c] [-ca CASH [CASH ...]] [-ch] [-cv]
                   [-d DELETE [DELETE ...]] [-f] [-g] [-G] [-n NEWS [NEWS ...]] [-o] [-p PORTFOLIO]
                   [-q QUOTE [QUOTE ...]] [-r REPEAT [REPEAT ...]] [-s STATS [STATS ...]]
                   [-t TARGET [TARGET ...]] [-v]

options:
  -h, --help            show this help message and exit
  -a, --add ADD [ADD ...]
                        add a symbol, the quantity held and the price paid
  -c, --costs           displays cost, quantity, price paid and target prices
  -ca, --cash CASH [CASH ...]
                        add an amount of cash held in the portfolio
  -ch, --chart_holdings
                        display a pie chart of current holdings
  -cv, --chart_value    display the value of the portfolio over time
  -d, --delete DELETE [DELETE ...]
                        delete a symbol
  -f, --fundamentals    get target price, upside, P/E and 52 week Highs & Lows
  -g, --dailygain       display stocks by today's gainers and losers
  -G, --totalgain       display stocks by total gainers and losers
  -n, --news NEWS [NEWS ...]
                        opens news page(s) for symbols in your browser
  -o, --offline         displays last downloaded data
  -p, --portfolio PORTFOLIO
                        choose a portfolio
  -q, --quote QUOTE [QUOTE ...]
                        gets quote for single stock
  -r, --repeat REPEAT [REPEAT ...]
                        pull data every N minutes
  -s, --stats STATS [STATS ...]
                        gets stats for single stock
  -t, --target TARGET [TARGET ...]
                        set a high and low target price for a symbol
  -v, --version         print the version and exit
```
  
## How to use
When adding the stock symbol, quantity and price are required

Allows multiple portfolios to be created and used. They are created as directories under user's home directory. Program will create 6 files in each portfolio directory to store portfolio info (cost.npy  last.npy  stocks.npy  target.npy  value.npy)
