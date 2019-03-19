SEE FINAL PROJECT REPORT IN BINDER DEMO HERE:


https://mybinder.org/v2/gh/dslachar/analysis_of_crp_data/master?filepath=Colorado's_Political_Landscape.ipynb

IF ABOVE LINK DOES NOT WORK, PLEASE REFERENCE THIS JUPYTER NOTEBOOK OF OUR FINAL REPORT WITH ALL CELLS RUN:

https://github.com/dslachar/analysis_of_crp_data/blob/master/FinalReport.ipynb



# analysis_of_crp_data

## 1. Team Members
* Samantha Werdel
* David Palazzo
* David Lacharite

## Objective
For this project we plan to do data collection, data cleaning, and exploratory data analysis (EDA) on political demographic data collected from the Center For Responsive Politics. We intend to conduct EDA which will address trends in campaing contributions across different demographic categories.

## 2. Dataset Attributes

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

## 3. Timeline

|Task                 |Completion Date   |   
|---------------------|------------------|
|Data collection      |  February 4th    |
|Data cleanup         |  February 18th   |
|Transformation       |  February 25th   |
|Feature engineering  |  March 3rd       |
|Statistical summary  |  March 7th       |
|Visualization        |  March 11th      |

### Project presentation March 13th
### Project report due March 15th 
