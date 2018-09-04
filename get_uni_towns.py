def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''

    utowns = pd.read_table('university_towns.txt', header=None, names = ['RegionName'])

    cur_state, edit = '', '[edit]'
    utowns['State'] = utowns.apply(fill_state, axis = 1)
    utowns = utowns[~utowns['RegionName'].str.endswith(edit)]
    utowns['State'] = utowns['State'].str[0:-6]
    utowns['RegionName'] = utowns.apply(clean_region, axis = 1)
    states = utowns['State']
    utowns.drop(labels=['State'], axis=1,inplace = True)
    utowns.insert(0, 'State', states)
    utowns.reset_index(drop=True, inplace = True)
    # utowns = utowns.set_index('State')
    
    return utowns

def fill_state(row):
    rowval = row.loc['RegionName']
    sep = '\['
    if 'edit' in rowval:
        global cur_state
        cur_state = rowval
    return cur_state.split(sep, 1)[0]

def clean_region(row):
    rowval = row.loc['RegionName']
    sep = ' ('
    return rowval.split(sep, 1)[0]

get_list_of_university_towns()
