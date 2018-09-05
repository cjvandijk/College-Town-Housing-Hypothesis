# script to test convert_housing_data_to_quarters

import re
q5 = convert_housing_data_to_quarters()
pattern = re.compile("\d\d\d\dq[1-4]")
res = 'Columns type test: '
if type(q5.columns) == pd.Index: 
    res += 'Passed' 
    res += '\nColumns names test: '
    if q5.columns.map(pattern.match).astype(bool).all():
        res += 'Passed'
    else:
        res += 'Failed'
        res += "\n Do the column names look like ['2000q1','2000q2'....]"
        res += '\n PS. column names are case sensitive'
else:
    res +='Failed'
    res += "\n Did you remember to change the column names back "
    res += "to strings in the format e.g. Index(['2000q1', '2000q2',...],dtype='object')"
res += "\nState name test: "    
if set(q5.index.get_level_values(0)).issubset(set(states.values())):
    res += 'Passed' 
else:
    res += 'Failed'
    res += "\n Did you map the abbreviated state names to the full names using the precoded states dictionary"
res += "\nShape test: "
if q5.shape == (10730,67):
    res += 'Passed'
else:
    res += 'Failed'

#generate all column names
columns = set(pd.date_range(
    start="2000", end="2017", freq='Q').map(
    lambda x: "{:}q{:}".format(x.year,x.quarter))[:-1])
res += "\nColumn Names test: "
if set(q5.columns)==columns:
    res += 'Passed'
else:
    res += 'Failed'
    res += "\nmissing columns" + str(columns-set(q5.columns))

print(res)
