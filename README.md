## stock_quote

## Overview
stock quote is a python script for getting stock quotes, news, calculating gains and losses and optionally recording to a time series database (influxdb). Usage requires an account (free) from www.alphavantage.co

## Usage
```
usage: stock_quote [-h] [-a ADD [ADD ...]] [-c] [-ca CASH [CASH ...]] [-ch] [-cv]
                   [-d DELETE [DELETE ...]] [-f] [-g] [-G] [-i INFLUX [INFLUX ...]]
                   [-k KEY [KEY ...]] [-n NEWS [NEWS ...]] [-o] [-p PORTFOLIO]
                   [-q QUOTE [QUOTE ...]] [-r REPEAT [REPEAT ...]] [-s STATS [STATS ...]]
                   [-t TARGET [TARGET ...]] [-v]

options:
  -h, --help            show this help message and exit
  -a ADD [ADD ...], --add ADD [ADD ...]
                        add a symbol, the quantity held and the price paid
  -c, --costs           displays cost, quantity, price paid and target prices
  -ca CASH [CASH ...], --cash CASH [CASH ...]
                        add an amount of cash held in the portfolio
  -ch, --chart_holdings
                        display a pie chart of current holdings
  -cv, --chart_value    display the value of the portfolio over time
  -d DELETE [DELETE ...], --delete DELETE [DELETE ...]
                        delete a symbol
  -f, --fundamentals    get target price, upside, P/E and 52 week Highs & Lows
  -g, --dailygain       display stocks by today's gainers and losers
  -G, --totalgain       display stocks by total gainers and losers
  -i INFLUX [INFLUX ...], --influx INFLUX [INFLUX ...]
                        influx server, port, user and password
  -k KEY [KEY ...], --key KEY [KEY ...]
                        add an api key, see https://www.alphavantage.co/
  -n NEWS [NEWS ...], --news NEWS [NEWS ...]
                        opens news page(s) for symbols in your browser
  -o, --offline         displays last downloaded data
  -p PORTFOLIO, --portfolio PORTFOLIO
                        choose a portfolio
  -q QUOTE [QUOTE ...], --quote QUOTE [QUOTE ...]
                        gets quote for single stock
  -r REPEAT [REPEAT ...], --repeat REPEAT [REPEAT ...]
                        pull data every N minutes
  -s STATS [STATS ...], --stats STATS [STATS ...]
                        gets stats for single stock
  -t TARGET [TARGET ...], --target TARGET [TARGET ...]
                        set a high and low target price for a symbol
  -v, --version         print the version and exit

```
  
## How to use
An API key is required, create an account at www.alphavantage.co, find your API tokens and enter the token using --key 
 
When adding the stock symbol, quantity and price are required

Allows multiple portfolios to be created and used. They are created as directories under user's home directory. Program will create 3 files in each portfolio directory to store portfolio info (cost.npy, last.npy and stocks.npy)

When using --influx, influxdb should be running on the target server and you must have a valid user and passwd. Graphs can be created using grafana (and other tools) by using influxdb as a datasource.
