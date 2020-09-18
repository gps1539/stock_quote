## stock_quote

## Overview
stock quote is a python script for getting stock quotes, news, calculating gains and losses and optionally recording to a time series database (influxdb). Usage now requires an account (free) from https://iexcloud.io

## Usage
```
usage: stock_quote [-h] [-a ADD [ADD ...]] [-c]
                   [-com COMPANY [COMPANY ...]]
                   [-cd CHART_DAY [CHART_DAY ...]] [-ch]
                   [-cy CHART_YEAR [CHART_YEAR ...]]
                   [-d DELETE [DELETE ...]]
                   [-div DIVIDENDS [DIVIDENDS ...]]
                   [-e EARNINGS [EARNINGS ...]] [-g] [-G]
                   [-i INFLUX [INFLUX ...]] [-k KEY [KEY ...]]
                   [-n NEWS [NEWS ...]] [-o] [-p PORTFOLIO]
                   [-q QUOTE [QUOTE ...]] [-R READ [READ ...]]
                   [-r REPEAT [REPEAT ...]] [-s STATS [STATS ...]]
                   [-v]

optional arguments:
  -h, --help            show this help message and exit
  -a ADD [ADD ...], --add ADD [ADD ...]
                        add a symbol, the quantity held and the price
                        paid
  -c, --costs           displays cost, quantity and price paid
  -com COMPANY [COMPANY ...], --company COMPANY [COMPANY ...]
                        get the company details for stock
  -cd CHART_DAY [CHART_DAY ...], --chart_day CHART_DAY [CHART_DAY ...]
                        display a intra day chart for symbol(s)
  -ch, --chart_holdings
                        display a pie chart of current holdings
  -cy CHART_YEAR [CHART_YEAR ...], --chart_year CHART_YEAR [CHART_YEAR ...]
                        display a 12m chart for a symbol(s)
  -d DELETE [DELETE ...], --delete DELETE [DELETE ...]
                        delete a symbol
  -div DIVIDENDS [DIVIDENDS ...], --dividends DIVIDENDS [DIVIDENDS ...]
                        get the next dividend data for a stock
  -e EARNINGS [EARNINGS ...], --earnings EARNINGS [EARNINGS ...]
                        get earnings actual v estimate for a stock
  -g, --dailygain       display stocks by today's gainers and losers
  -G, --totalgain       display stocks by total gainers and losers
  -i INFLUX [INFLUX ...], --influx INFLUX [INFLUX ...]
                        influx server, port, user and password
  -k KEY [KEY ...], --key KEY [KEY ...]
                        add an api key, see https://iexcloud.io
  -n NEWS [NEWS ...], --news NEWS [NEWS ...]
                        opens news page(s) for symbols in your
                        browser
  -o, --offline         displays last downloaded data
  -p PORTFOLIO, --portfolio PORTFOLIO
                        choose a portfolio
  -q QUOTE [QUOTE ...], --quote QUOTE [QUOTE ...]
                        gets quote for single stock
  -R READ [READ ...], --read READ [READ ...]
                        inport from a csv file
                        (symbol,quantity,price)
  -r REPEAT [REPEAT ...], --repeat REPEAT [REPEAT ...]
                        pull data every N minutes
  -s STATS [STATS ...], --stats STATS [STATS ...]
                        gets stats for single stock
  -v, --version         print the version and exit

```
  
## How to use
A key is now required. Create an account at iexcloud.io, find your API tokens and enter the "Publishable" token using --key 
 
When adding the stock symbol, quantity and price are required

Allows multiple portfolios to be created and used. They are created as directories under user's home directory. Program will create 3 files in each portfolio directory to store portfolio info (cost.npy, last.npy and stocks.npy)

When using --influx, influxdb should be running on the target server and you must have a valid user and passwd. Graphs can be created using grafana (and other tools) by using influxdb as a datasource.

To import transactions with --read ensure the csv file has the following fields: symbol,quantity,price
