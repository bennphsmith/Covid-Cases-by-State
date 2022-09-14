# Covid Stats by State


## Description
Generates zip file of word documents containing N most recent 
days of Covid case data per State. Information is called from
the following API:
https://healthdata.gov/dataset/COVID-19-Diagnostic-Laboratory-Testing-PCR-Testing/j8mb-icvb


## Requirements
- python 3.10.2
- pandas 1.4.4
- python-docx 0.8.11
- PyYAML 6.0
- requests 2.28.1


## Setup
A config file is needed to run the module and should be
placed in a 'Config' folder. A standard 'yaml' file should
already be provided with the variables needed for set up
already populated with default values. They include:
- zip_file_name - Name of the output zip file
- number_of_days - Number of most recent days of Covid data requested. Set to 5
- url - URL for API requests
- expected_schema - Schema needed to generate data and output table requested
- positive_Table_Schema - Schema for table of Positive Covid cases
- negative_Table_Schema - Schema for table of Negative Covid cases
- output_columns - Columns expected in the output table
- state_names - List of states required in the output. Should be properly cased

## Errors
custom_errors.py file has been created to catch certain potential
errors when running the module.

## Run File
Program can be run using the following command from the Main folder:

- python3 main.py