# create a list with files of similar format

glob(<fileName>-*.<fileExtension>)

# example
glob("data/programfiles/excel-*.csv")

# output
['data/programfiles/excel-1.csv',
 'data/programfiles/excel-4.csv',
 'data/programfiles/excel-3.csv',
 'data/programfiles/excel-5.csv',
 'data/programfiles/excel-2.csv']

sorted(glob("data/programfiles/excel-*.csv"))

['data/programfiles/excel-1.csv',
 'data/programfiles/excel-2.csv',
 'data/programfiles/excel-3.csv',
 'data/programfiles/excel-4.csv',
 'data/programfiles/excel-5.csv']
