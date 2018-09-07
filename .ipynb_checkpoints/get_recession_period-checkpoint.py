def clean_gdp(gdp):
    # get needed columns from gdplev excel file
    columns_to_keep = ['Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6']
    gdp = gdp[columns_to_keep]
    gdp.columns = ['Quarter', 'GDP Current', 'GDP Chained']
    gdp = gdp[~gdp['Quarter'].isnull()]
    
    # only keep data from 2000 onwards
    gdp = gdp[gdp['Quarter'].str.startswith('2')]
    gdp.reset_index(drop = True, inplace = True)
    
    # create column to compare GDP change from quarter to quarter
    gdp['GDP Change'] = gdp['GDP Current'] - gdp['GDP Current'].shift(1)

    return gdp

def get_recession_start(gdp):
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3
    '''
    
    # look for two successive quarters with negative change in GDP
    start_qtr = ''
    for j in range(1,len(gdp)-1):
        if gdp.iloc[j]['GDP Change']<0 and gdp.iloc[j-1]['GDP Change']<0:
            start_qtr = gdp.iloc[j-2]['Quarter']
            break

    return start_qtr

def get_recession_end(gdp, rec_start):
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3
    '''
    
    # start at the beginning of the recession
    rec_start_ix = gdp.Quarter[gdp.Quarter == rec_start].index.tolist()[0]
    end_qtr = ''
    # look for 2 successive quarters of increasing GDP
    for j in range(rec_start_ix,len(gdp)-1):
        if gdp.iloc[j]['GDP Change']>0 and gdp.iloc[j+1]['GDP Change']>0:
            end_qtr = gdp.iloc[j+1]['Quarter']
            break
    return end_qtr

def get_recession_bottom(gdp, rec_start, rec_end):
    '''Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3
    '''
    
    # get index locations of recession start and end
    rec_start_ix = gdp.Quarter[gdp.Quarter == rec_start].index.tolist()[0]
    rec_end_ix = gdp.Quarter[gdp.Quarter == rec_end].index.tolist()[0]
    
    gdp['GDP Current'] = gdp['GDP Current'].astype(float).fillna(0.0)
    bottom_qtr = ''
    lowest_gdp = gdp.iloc[rec_start_ix]['GDP Current']
    # look for 2 successive quarters of increasing GDP
    for j in range(rec_start_ix, rec_end_ix):
        if gdp.iloc[j]['GDP Current'] < lowest_gdp:
            bottom_qtr = gdp.iloc[j]['Quarter']
            lowest_gdp = gdp.iloc[j]['GDP Current']
            
    return bottom_qtr


