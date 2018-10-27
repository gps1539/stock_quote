# stock_quote
python script for getting stock quotes, calculating gains and losses and optionally recording to a time series database (influxdb).

usage: stock_quote [-h] [-a ADD [ADD ...]] [-d DELETE [DELETE ...]] [-g] [-G]
                   [-i INFLUX [INFLUX ...]] [-o] [-p PORTFOLIO]
                   [-q QUOTE [QUOTE ...]] [-R READ [READ ...]]
                   [-r REPEAT [REPEAT ...]] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -a ADD [ADD ...], --add ADD [ADD ...]
                        add a symbol, the quantity held and the price paid
  -d DELETE [DELETE ...], --delete DELETE [DELETE ...]
                        delete a symbol
  -g, --dailygain       display stocks by today's gainers and losers
  -G, --totalgain       display stocks by total gainers and losers
  -i INFLUX [INFLUX ...], --influx INFLUX [INFLUX ...]
                        influx server, port, user and password
  -o, --offline         displays last downloaded data
  -H, --holdings        displays cost, quanity and price paid
  -p PORTFOLIO, --portfolio PORTFOLIO
                        choose a portfolio
  -q QUOTE [QUOTE ...], --quote QUOTE [QUOTE ...]
                        add a symbol, gets quote for single stock
  -R READ [READ ...], --read READ [READ ...]
                        read transactions from a csv file (google finance)
  -r REPEAT [REPEAT ...], --repeat REPEAT [REPEAT ...]
                        pull data every N minutes
  -v, --version         print the version and exit
  
When adding the stock symbol, quantity and price are required

Files are created in a .stocks directory in the users home directory

Allows multiple portfolios to be created and used. They are created as directories under .stocks in the user's home directory. Program will create 3 files in each portfolio directory to store portfolio info (cost.npy, last.npy and stocks.npy)

When using --influx, influxdb most be running on the target server and you must have a valid user and passwd. Graphs can be created using grafana (and other tools) by using influxdb as a datasource.

--read supports importing transactions from an exported google finance portfolio csv file.
