# stock_quote
python script for getting stock quotes, calculating gains and losses and optionally recording to a time series database (influxdb).

usage: stock_quote [-h] [--add ADD [ADD ...]] [--delete DELETE [DELETE ...]]
                   [--gain] [--influx INFLUX [INFLUX ...]] [--offline]
                   [--portfolio PORTFOLIO] [--read READ [READ ...]]
                   [--repeat REPEAT [REPEAT ...]] [--version]

optional arguments:
  -h, --help            show this help message and exit
  --add ADD [ADD ...]   add a symbol, the quantity held and the price paid
  --delete DELETE [DELETE ...]
                        delete a symbol
  --gain                display stocks by gainers and losers
  --influx INFLUX [INFLUX ...]
                        influx server, port, user and password
  --offline             displays last downloaded data
  --portfolio PORTFOLIO
                        choose a portfolio
  --read READ [READ ...]
                        read transactions from a csv file (google finance)
  --repeat REPEAT [REPEAT ...]
                        pull data every N minutes
  --version             print the version and exit

  
When adding the stock symbol, quantity and price are required

Files are created in a .stocks directory in the users home directory

Allows multiple portfolios to be created and used. They are created as directories under .stocks in the user's home directory. Program will create 3 files in each portfolio directory to store portfolio info (cost.npy, last.npy and stocks.npy)

When using --influx, influxdb most be running on the target server and you must have a valid user and passwd. Graphs can be created using grafana (and other tools) by using influxdb as a datasource.

--read supports importing transactions from an exported google finance portfolio csv file.
