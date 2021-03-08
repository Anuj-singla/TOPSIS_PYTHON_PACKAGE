# TOPSIS_Anuj_101803638
With this you can calculate the TOPSIS score and RANK of the data provided in '.csv' format.
- Input file:
  - contain three or more columns
  - First column is the object/variable name.
  - From 2nd to last column contain numeric values only

# Overview
  - You can check intermediate steps as well as the final score i.e it provides functions to calculate normalized matrix, weight normalized decision matrix , ideal best , ideal worst lists and so on.

## Usage

In the following paragraphs, I am going to describe how you can get and use TOPSIS for your own projects.

### Getting it
To download TOPSIS, either fork this github repo or simply use Pypi via pip.

    $ pip install TOPSIS_Anuj_101803638

### Using it
TOPSIS was programmed with ease-of-use in mind. Just, import topsis from TOPSIS-Aditi-101803650

    from TOPSIS_Anuj_101803638.topsis1 import topsis
    topsis('inputfilename','Weights','Impacts','Outputfilename')

And you are ready to go! 

## topsis
There are 5 steps in this:
  - normalized_matrix
  - weight_normalized
  - ideal_best_worst
  - euclidean_distance
  - topsis_score
## License
[MIT](https://choosealicense.com/licenses/mit/)

## Pre-requisite
The data should be enclosed in the csv file. There must be more than 2 columns

## Result
the output(outputfilename)  is saved in the project folder with extra 2 columns with topsis score and rank.

