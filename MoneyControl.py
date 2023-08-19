import pandas as pd
import numpy as np

urls=['https://www.moneycontrol.com/markets/indian-indices/top-nse-50-companies-list/9?classic=true&categoryId=1&exType=N','https://www.moneycontrol.com/markets/indian-indices/top-nsebank-companies-list/23?classic=true&categoryId=1&exType=N','https://www.moneycontrol.com/markets/indian-indices/top-nsemidcap-100-companies-list/27?classic=true&categoryId=1&exType=N','https://www.moneycontrol.com/markets/indian-indices/top-nse-100-companies-list/28?classic=true&categoryId=1&exType=N','https://www.moneycontrol.com/markets/indian-indices/top-nse-200-companies-list/49?classic=true&categoryId=1&exType=N','https://www.moneycontrol.com/markets/indian-indices/top-indiavix-companies-list/36?classic=true&categoryId=1&exType=N']
for url in urls:
    '''scraping from money control of a link'''
    edf=pd.DataFrame()
    list_df=pd.read_html(url)
    for df in list_df:
        edf=pd.concat([edf,df])
    edf=edf.reset_index(drop=True)
    edf=edf.replace('No Data',np.NAN)
    edf=edf.dropna()
    edf.to_excel(f'Money Control - {url.split("/")[5]}.xlsx')
    '''scraping from money control of a link'''