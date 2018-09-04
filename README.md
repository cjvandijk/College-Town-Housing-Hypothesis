# Housing-Hypothesis
This project uses data from several sources to test the hypothesis that housing prices in university towns do not suffer from economic recession as much as in non-university towns.

Data is prepared: 
- Housing prices are converted into quarterly chunks for comparison to GDP info.
- GDP info is evaluated to determine the start and end of a recession.
- A list of university towns is cleaned for comparison against the housing town column.

Analysis:
- New data is created, showing the decline or growth of housing prices
    between the recession start and the recession bottom. 
- A ttest is run comparing the university town values to the non-university towns values, 
    returning whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
 - The value for better will be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'
