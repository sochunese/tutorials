def load_temp(mindate, maxdate, plot=True):
    '''
    Downloads data from LOBO and makes a plot.
    
    Arguments:
        mindate (string): Start date
        maxdate (string): End date
        plot(boolean): If True, it produces a plot (default=True)
    
    Returns:
        DataFrame and a plot (if 'plot' argument = True)
    '''
    
    import pandas as pd
    import matplotlib.pyplot as plt

    #URL quering the LOBO server for data (in this case, temperature data)

    URL='http://lobo.satlantic.com/cgi-data/nph-data.cgi?min_date='+mindate+'&max_date='+maxdate+'&y=temperature'

    #import data from LOBO server
    data = pd.read_csv(URL, sep='\t')

    #change indices to DatetimeIndex objects
    data.index=pd.DatetimeIndex(data['date [AST]'])

    #now that we made "date indices" we can drop the "date" column
    data=data.drop('date [AST]', axis=1)

    if plot == True:
        # a bit fancier plot
        data.plot(style='-r', legend=False)
        plt.title('Temperature')
        plt.ylabel('Temperature(oC)')
        plt.xlabel('Dates')
        plt.show()
        
    return data
