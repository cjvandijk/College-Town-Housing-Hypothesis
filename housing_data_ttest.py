def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    
    rec_st = get_recession_start()
    rec_bot = get_recession_bottom()

    housing = convert_housing_data_to_quarters()
    # keep only recession-related quarters
    housing = housing.loc[:, housing.columns >= rec_st]
    housing = housing.loc[:, housing.columns <= rec_bot]
    housing['PriceRatio'] = housing[rec_st].div(housing[rec_bot])
    housing.reset_index(inplace = True)
    
    # build column for easy merge
    housing['SRcombo'] = housing['State'] + housing['RegionName']

    utowns = get_list_of_university_towns()
    #build column for easy merge
    utowns['SRcombo'] = utowns['State'] + utowns['RegionName']

    # separate housing info for uni towns and non-uni towns
    housing_uni = pd.merge(utowns, housing, 
                           left_on='SRcombo', right_on='SRcombo')
    housing_non_uni = housing[(~housing.SRcombo.isin(housing_uni.SRcombo))]

    #run ttest to test hypothesis
    p = ttest_ind(housing_uni.dropna()['PriceRatio'], 
                  housing_non_uni.dropna()['PriceRatio'])[1]
    different = p < 0.01  # check null hypothesis
    better = "non-university town"
    if housing_uni.PriceRatio.mean() < housing_non_uni.PriceRatio.mean():
        better = "university town"
    
    return (different, p, better)

run_ttest()
