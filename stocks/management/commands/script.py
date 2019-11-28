from django.core.management.base import BaseCommand

# from core.models import Problem

import bs4
import requests
import datetime
import os
import yfinance as yf



class Command(BaseCommand):
    help = 'Scrapes capitalassets.com.ng to obtain the details of all the stock.'
    
    def handle(self, *args, **options):
        
        msft = yf.Ticker("MSFT")
        print(msft.info)

        
        self.stdout.write(f'\nScraping ended at {datetime.datetime.now()}\n')



