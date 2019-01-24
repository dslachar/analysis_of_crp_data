# analysis_of_crp_data


## Dataset Attributes

We plan to use data from the Campaign Finance and Campaign Contributions tables. Interesting attributes include the following:

1) Contributor Occupation - noisy data - i.e. CEO/Chairman, CEO&Chairman
                          - normal - i.e. Attorney 
                          
2) Columns Date and Amount - Appear to be in the same data field, although meta data states otherwise. Will need to break different two columns

3) RecipCode - This attribute gives political affiliation and second is whether the candidate won or lost.

4) Gender - Four gender options including 'U' for unknown and 'N' for ambiguous. We will need to determine whether or not to use include the ambiguous and unknown types.

5) Transaction code type - Transaction code will need to be parsed based on whether the contribution is earmarked (15e), joint contribution (15j), refund (10y), or contribution (15).

6) Org name - Organization affiliated with contribution. Missing values are found in this field. 

Additional attributes that are of interest, that do not have potential for cleaning include the following:

    -Zip code 
    -State
    -Cycle (election year)
    -ContribID (unique id for each candidate)
    

Note that metadata can be found at the following site:
https://www.opensecrets.org/resources/datadictionary/UserGuide.pdf
