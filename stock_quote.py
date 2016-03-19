#!/usr/bin/env python3
import urllib.request
import sys
import os
import re
import getopt
import numpy as np
import argparse
from colorama import init, Fore, Back, Style
init()

# command line options and help
parser = argparse.ArgumentParser()
parser.add_argument("--add", nargs='+', help="add a symbol, the quantity held and the price paid")
parser.add_argument("--delete", help="delete a symbol")
parser.add_argument("--portfolio", help="choose a portfolio")
args = parser.parse_args()

if args.add:
     if len(args.add)!=3:
          print('symbol, quantity and price are required with --add')
          sys.exit(1)

# set directory to user's home (should work for Linux, Mac and Windows)
os.chdir(os.path.expanduser("~"))

if args.portfolio:
     portfolio=str("." + (args.portfolio))
     if os.path.exists(portfolio)==False:
          os.mkdir(portfolio) 
     os.chdir(os.path.expanduser(portfolio))

# check if files exist for stocks and cost info
if os.path.exists('stocks.npy')==False:
     stocks={}
else:
     stocks = np.load('stocks.npy').item()
if os.path.exists('cost.npy')==False:
     cost={}
else:
     cost = np.load('cost.npy').item()
value = cost.copy()
day = cost.copy()

# function to add stock, quanity and price. checks if stock is valid on Yahoo
def inputtostocks(sym, qtn, price):
     url = "http://download.finance.yahoo.com/d/quotes.csv?s="+sym+"&f=ac"
     f = urllib.request.urlopen(url)
     r = f.read()
     if len(r)<10:
          print(sym + ' is not a valid stock symbol')
          return
     if (str(r)[2])=='N':
          print(sym + ' is not a valid stock symbol')
          return
     paid=int(qtn*price)
     stocks.update({sym:qtn})
     np.save('stocks.npy', stocks) 
     cost.update({sym:paid})
     np.save('cost.npy', cost)

# function to remove a stock      
def removestocks(sym):
     if sym in stocks:
          del stocks[sym]
          np.save('stocks.npy', stocks) 
     if sym in cost:
          del cost[sym]
          np.save('cost.npy', cost)
     return

# function to get current price for a stock and print results
def getcurrentprice(symbol):
     url = "http://download.finance.yahoo.com/d/quotes.csv?s="+symbol+"&f=ac"
     f = urllib.request.urlopen(url)
     r = f.read()
     r = (r.decode("utf-8").strip())
     data=re.sub(r'\s', '',r).split(',')
     if (data[0])=='N/A':
          print ('Could not get price for ' +(symbol))
          return
     s=float(data[0])
     test=(data[0])
     change=((data[1][2:7]).strip('-'))
     if (data[1][1])=='-':
          change=float('-'+change)
          col=(Fore.RED)
     else:
          col=(Fore.GREEN)
     if (((stocks[symbol])*(s)) -(cost[symbol])) <0:
          tcol=(Fore.RED)
     else:
          tcol=(Fore.GREEN)
     day[symbol]=(float(change)*(stocks[symbol]))
     value[symbol] =((stocks[symbol])*(s))
     print('{:<4} {:<8} {:<26} {:<16} {:<16}'.format
           (symbol,
            ' $'+str(s),
            col + str((data[1]).strip('"')) + Style.RESET_ALL,
            'value $'+ str(round((stocks[symbol])*(s),2)),
            'gain $'+ tcol + str(round(((stocks[symbol])*(s)) -(cost[symbol]),2))),
            '%'+ str(round(100*((((stocks[symbol])*(s)) - (cost[symbol]))/(cost[symbol])),2)) + Style.RESET_ALL)

# get latest change in Dow Jones Index
def getdow():
     url = "http://download.finance.yahoo.com/d/quotes.csv?s=DIA&f=ac"
     f = urllib.request.urlopen(url)
     r = f.read()
     r = (r.decode("utf-8").strip())
     data=re.sub(r'\s', '',r).split(',')
#     s=(float(data[0])*100)
     change=((data[1][2:7]).strip('-'))
     if (data[1][1])=='-':
          change=float('-'+change)
          col=(Fore.RED)
     else:
          col=(Fore.GREEN)
     print('DOW   ', col + str((data[1]).strip('"'))+ Style.RESET_ALL)

# get latest change in Nasdaq Index
def getnasdaq():
     url = "http://download.finance.yahoo.com/d/quotes.csv?s=^IXIC&f=ac"
     f = urllib.request.urlopen(url)
     r = f.read()
     r = (r.decode("utf-8").strip())
     data=re.sub(r'\s', '',r).split(',')
#     s=float(data[0])
     change=((data[1][2:7]).strip('-'))
     if (data[1][1])=='-':
          change=float('-'+change)
          col=(Fore.RED)
     else:
          col=(Fore.GREEN)
     print('Nasdaq',col + str((data[1]).strip('"'))+ Style.RESET_ALL)

# call inputtostocks if --added option on command line
if args.add:
     sym=str(args.add[0])
     qtn=int(args.add[1])
     price=float(args.add[2])
     inputtostocks(sym,qtn,price)

# call removestocks if --delete option on command line      
if args.delete:
     sym=str(args.delete)
     removestocks(sym)

# polite exit if no stocks in directory and --added not used
if len(stocks)==0:
     print('Please input stocks with --add')
     sys.exit(1)

# call getcurrentprice for each stock in stocks dictory
for key in sorted(stocks.keys()):
	getcurrentprice(key)

# formatting and printing summary
gain=sum(day.values())

if (gain)<0:
     pgain=(Fore.RED + str(round(gain,2)))
else:
     pgain=(Fore.GREEN + str(round(gain,2)))

mkt=sum(value.values())
cst=sum(cost.values())
tgain=(round((mkt-cst),2))
print()
getdow()
getnasdaq()

if (tgain)<0:
     ptgain=(Fore.RED + str(tgain))
else:
     ptgain=(Fore.GREEN + str(tgain))
     
print()
print('Day Gain =   $'+pgain +
     ',  %' + str(round((100*(gain/mkt)),4))+ Style.RESET_ALL)
print('Total Gain = $'+ptgain +
       ', %' + str(round((100*(mkt-cst)/cst),2))+ Style.RESET_ALL)
print('Cost $' + str(cst) +
       ' Current Value $' + str(round(mkt,2)))
