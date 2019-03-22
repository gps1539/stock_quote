## stock_quote

## Overview
stock quote is a python script for getting stock quotes, news, calculating gains and losses and optionally recording to a time series database (influxdb).

## Usage
```
usage: stock_quote [-h] [-a ADD [ADD ...]] [-d DELETE [DELETE ...]] [-g] [-G]
                   [-H] [-i INFLUX [INFLUX ...]] [-n NEWS [NEWS ...]] [-o]
                   [-p PORTFOLIO] [-q QUOTE [QUOTE ...]] [-R READ [READ ...]]
                   [-r REPEAT [REPEAT ...]] [-v]
```
```
optional arguments:
  -h, --help            show this help message and exit
  -a ADD [ADD ...], --add ADD [ADD ...]
                        add a symbol, the quantity held and the price paid
  -d DELETE [DELETE ...], --delete DELETE [DELETE ...]
                        delete a symbol
  -g, --dailygain       display stocks by today's gainers and losers
  -G, --totalgain       display stocks by total gainers and losers
  -H, --holdings        displays cost, quantity and price paid
  -i INFLUX [INFLUX ...], --influx INFLUX [INFLUX ...]
                        influx server, port, user and password
  -n NEWS [NEWS ...], --news NEWS [NEWS ...]
                        opens news page(s) for symbols in your browser
  -o, --offline         displays last downloaded data
  -p PORTFOLIO, --portfolio PORTFOLIO
                        choose a portfolio
  -q QUOTE [QUOTE ...], --quote QUOTE [QUOTE ...]
                        add a symbol, gets quote for single stock
  -R READ [READ ...], --read READ [READ ...]
                        inport from a csv file (symbol,quantity,price)
  -r REPEAT [REPEAT ...], --repeat REPEAT [REPEAT ...]
                        pull data every N minutes
  -v, --version         print the version and exit
```
  
## How to use
When adding the stock symbol, quantity and price are required

Allows multiple portfolios to be created and used. They are created as directories under user's home directory. Program will create 3 files in each portfolio directory to store portfolio info (cost.npy, last.npy and stocks.npy)

When using --influx, influxdb should be running on the target server and you must have a valid user and passwd. Graphs can be created using grafana (and other tools) by using influxdb as a datasource.

To import transactions with --read ensure the csv file has the following fields: symbol,quantity,price
