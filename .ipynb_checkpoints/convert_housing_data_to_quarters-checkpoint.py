def convert_housing_data_to_quarters(housing):
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. Only using columns from 2000q1 through
    2016q3. Uses a State/RegionName multi-index. Returns housing dataframe.
    '''

    start=housing.columns.get_loc('2000-01')
    end = housing.columns.get_loc('2016-08')


    # iterate across every third column from 2001-01 to 2016-08
    columns_to_keep = []
    for i in range(start, end, 3):
        mon = housing.columns[i][5:7]  # get month
        yr = housing.columns[i][0:4]   # get year
        q = (int(mon) // 3) + 1        # calculate quarter
        col_name = yr + 'q' + str(q)   # get column name for yr/qtr
    
        # sum values from columns for quarter
        qsum1 = housing[housing.columns[i]].astype(float)
        qsum2 = housing[housing.columns[i+1]].astype(float)
        qsum3 = housing[housing.columns[i+2]].astype(float)
    
        # create column for this quarter
        housing[col_name] = ((qsum1 + qsum2 + qsum3)/3).astype(float)
        columns_to_keep.append(col_name)

    # make multi-index State,RegionName
    housing = housing.replace({'State':states})
    housing = housing.set_index(['State', 'RegionName'])

    # Keep quarter columns
    housing = housing[columns_to_keep]
    return housing


