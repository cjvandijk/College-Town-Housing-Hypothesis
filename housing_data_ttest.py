def run_ttest():
    '''
    1. Create new data showing the decline or growth of housing prices
       between the recession start and the recession bottom.
    2. Run a ttest comparing the university town values to the
       non-university towns values. Return whether the alternative
       hypothesis (that the two groups are the same) is true or not,
       as well as the p-value of the confidence.     
    3. Return the tuple (different, p, better) where:
        - different=True if the t-test is True at a p<0.01 (we reject
          the null hypothesis)
        - different=False if otherwise (we cannot reject the null hypothesis).
        - The variable 'p' is the exact p value returned from
          scipy.stats.ttest_ind().
        - The value for 'better' is either "university town" or
          "non-university town" depending on which has a lower
          mean price ratio (which is equivilent to a reduced market loss).
    '''
    
    # get recession start and bottom quarters
    rec_start = get_recession_start()
    rec_bottom = get_recession_bottom()

    # read housing data, then keep only recession-related quarters
    housing = convert_housing_data_to_quarters()
    housing = housing.loc[:, housing.columns >= rec_start]
    housing = housing.loc[:, housing.columns <= rec_bottom]
    housing['PriceRatio'] = housing[rec_start].div(housing[rec_bottom])
    housing.reset_index(inplace = True)
    
    # build column for easy merge
    housing['SRcombo'] = housing['State'] + housing['RegionName']

    # read list of university towns, then build column for easy merge
    utowns = get_list_of_university_towns()
    utowns['SRcombo'] = utowns['State'] + utowns['RegionName']

    # separate housing info for uni towns and non-uni towns
    housing_uni = pd.merge(utowns, housing, 
                           left_on='SRcombo', right_on='SRcombo')
    housing_non_uni = housing[(~housing.SRcombo.isin(housing_uni.SRcombo))]

    # run ttest to test hypothesis
    p = ttest_ind(housing_uni.dropna()['PriceRatio'], 
                  housing_non_uni.dropna()['PriceRatio'])[1]
    different = p < 0.01  # check null hypothesis
    better = "non-university town"
    if housing_uni.PriceRatio.mean() < housing_non_uni.PriceRatio.mean():
        better = "university town"
    
    return (different, p, better)

# run_ttest()
