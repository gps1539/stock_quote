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
          del value[sym]
          del day[sym]
          np.save('cost.npy', cost)
     return

# function to get current price for a stock and print results
def getyahooprice(symbol):
     url = "http://download.finance.yahoo.com/d/quotes.csv?s="+symbol+"&f=ac"
     f = urllib.request.urlopen(url)
     r = f.read()
     r = (r.decode("utf-8").strip())
     data=re.sub(r'\s', '',r).split(',')
     if (data[0])=='N/A':
          print ('Could not get price for ' +(symbol))
          day[symbol]=0 
          value[symbol]=(cost[symbol])
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
     print('{:<10} {:<10} {:<27} {:<17} {:<20}'.format
           (symbol,
            ' $'+str(s),
            col + str((data[1]).strip('"')) + Style.RESET_ALL,
            'value $'+ str(round((stocks[symbol])*(s),2)),
            'gain $'+ tcol + str(round(((stocks[symbol])*(s)) -(cost[symbol]),2))),
            str(round(100*((((stocks[symbol])*(s)) - (cost[symbol]))/(cost[symbol])),2))+'%'+ Style.RESET_ALL)

def getgoogleprice(symbol):
     url = "http://finance.google.com/finance/info?client=ig&q="+symbol
     f = urllib.request.urlopen(url)
     r = f.read()
     r = (r.decode("utf-8").strip())
     r = re.sub(r'\s', '',r).split(',')
     s=float(re.sub(r'[a-z,:,",_]', "", r[5]))
     if (re.sub(r'[a-z,:,",_]', "", r[13])[0])=='-':
          col=(Fore.RED)
     else:
          col=(Fore.GREEN) 
     if (((stocks[symbol])*(s)) -(cost[symbol])) <0:
          tcol=(Fore.RED)
     else:
          tcol=(Fore.GREEN)    
     change=re.sub(r'[a-z,:,",_]', "", r[11])
     day[symbol]=(float(change)*(stocks[symbol]))
     value[symbol] =((stocks[symbol])*(s))
     ticker=re.sub(r'[a-z,:,",_]', "", r[1])
     price=re.sub(r'[a-z,:,",_]', "", r[5])
     percent=re.sub(r'[a-z,:,",_]', "", r[13])
     print('{:<11}'.format (ticker) + ' $' + '{:<6}'.format (price),
           col + ' ' + '{:<9}'.format (change)  + '{:<8}'.format (percent+'%') + Style.RESET_ALL, 
           'value $' + '{:<8}'.format (str(round((stocks[symbol])*(s)))), 
           'gain $' + tcol + '{:<8}'.format (str(round(((stocks[symbol])*(s)) -(cost[symbol]))))
	    + str(round(100*((((stocks[symbol])*(s)) - (cost[symbol]))/(cost[symbol])),2))+'%'+ Style.RESET_ALL)

# get latest change in Index (Nasdaq, DJI)
def getindex(symbol):
     url = "http://finance.google.com/finance/info?client=ig&q=."+symbol
     f1 = urllib.request.urlopen(url)
     r1 = f1.read()
     r1 = (r1.decode("utf-8").strip())
     r1 = re.sub(r'\s', '',r1).split(',')
     if (re.sub(r'[a-z,:,",_]', "", r1[13])[0])=='-':
          col=(Fore.RED)
     else:
          col=(Fore.GREEN)
     symbol=re.sub(r'[a-z,:,",_]', "", r1[2])
     price=re.sub(r'[a-z,:,",_]', "", r1[5])
     change=re.sub(r'[a-z,:,",_]', "", r1[13])
     percent=re.sub(r'[a-z,:,",_]', "", r1[15])
     print('{:<11}'.format (symbol) + ' ' + '{:<8}'.format  (price), col + '{:<8}'.format (change) + ' ' + (percent) + '% '+ Style.RESET_ALL)

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

# polite exit if no stocks in dictionary and --added not used
if len(stocks)==0:
     print('Please input stocks with --add')
     sys.exit(1)

# call yahoo getyahooprice for each stock in stocks dictionary
#for key in sorted(stocks.keys()):
#     getyahooprice(key)

# call google getgoogleprice for each stock in stocks dictionary
for key in sorted(stocks.keys()):
     getgoogleprice(key)

# formatting and printing summary
gain=sum(day.values())

if (gain)<0:
     pgain=(Fore.RED + str(round(gain)))
else:
     pgain=(Fore.GREEN + str(round(gain)))

mkt=sum(value.values())
cst=sum(cost.values())
tgain=(round((mkt-cst)))
print()
getindex("dji")
getindex("ixic")

if (tgain)<0:
     ptgain=(Fore.RED  + str(tgain))
else:
     ptgain=(Fore.GREEN + str(tgain))
     
print()
print('{:<12}'.format ('Daily Gain  $') + '{:<14}'.format (pgain) +
     '{:<27}'.format (str(round((100*(gain/mkt)),2))+'%') + Style.RESET_ALL
     + 'Total gain $'+ '{:<13}'.format (ptgain) + str(round((100*(mkt-cst)/cst),2))+'%'
     + Style.RESET_ALL)
print()
#print('Cost        $' + '{:<9}'.format (str(round(cst))) + 'Current  $' + '{:<17}'.format (str(round(mkt))) + 'Total gain $'+ '{:<16}'.format (ptgain) +
#     str(round((100*(mkt-cst)/cst),2))+'%'+ Style.RESET_ALL)
