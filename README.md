# A tool to generate seeds data for rails and markdown tables based on csv files  


## Usage


- Put csv file containing all of your data in the same folder. It should have a header line, consisting of column names. Those column names will be the variable names in generated seeds data file.
- Run `generateSeeds.py` to generate `seeds.rb`
    - you may need to move items up or down in order to have dependent models （has foreign keys) after their ancestors.
- Run `writeMdTable.py` to generate markdown file.
