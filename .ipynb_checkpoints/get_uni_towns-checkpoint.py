def get_list_of_university_towns(utowns):
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt file.

    The format of the DataFrame will have two columns: "State" and "RegionName"
    
    The following cleaning will be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character
       from " (" to the end.
    3. Depending on how the data is read, a newline character ('\n')
       may need to be removed.
    '''

    cur_state, edit = '', '[edit]'
    utowns['State'] = utowns.apply(fill_state, axis = 1)
    utowns = utowns[~utowns['RegionName'].str.endswith(edit)]
    utowns.loc[:,'State'] = utowns.loc[:,'State'].str[0:-6]
    utowns['RegionName'] = utowns.apply(clean_region, axis = 1)
    states = utowns['State']
    utowns.drop(labels=['State'], axis=1,inplace = True)
    utowns.insert(0, 'State', states)
    utowns.reset_index(drop=True, inplace = True)
    
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


