### EHR LIBRARY

This package has been made to facilitate patient data analytics. This can be useful in evaluating clinical trials and analyzing medical data. The package has been written in python. 

#### Installation and Requirements

To install this package, you can clone the github repository it has been placed on. The following python modules are required for successful implimentation of this module.

1) Time
2) Pytests

#### Functionalities

The package facilitates a number of functionalities. Below we have gone over each of these, the function name associated with each functionality, and the how to sucessfully execute each function. All the functions take the arguements in the below mentioned order. 

**Function 1**

Name: parse_data

Description: Restructures that data into a `dictionary` data type that can be easily manipulated to suit your needs.

Arguements: 

1. filename -> this is the path for `TAB` delimited `txt` file which contains all the data. 

Output: Returns data as a `dictionary`, whose keys are the column names and the value for each key will a be list of `strings` the column entries.

**Function 2**

Name: num_older_than

Description: This function tells us the number of patients older than a certain age.

Arguements: 

1. age -> Can be an `integer` or a `float`.
2. Patient_dataset -> a dictionary containing information on all the patients. This dictionary should have the format that is similar to the one returned by the parse_data function above. The data should have a `PatientDateOfBirth` column.  The values corresponding to `PatientDateOfBirth` key should follow the format `YYYY-mm-dd HH:MM:SS.MS` where `SS.MS` indicated seconds and microseconds.

Outputs: Returns the number of patients older than the specified age. Sometimes can return a string that explains why the required number can be calculated, for example patient data file not meeting the exact requirements.

**Function 3**

Name: sick_patients

Description: Returns the ID of all the `unique` patients that are visiting a certain lab. 

Arguements: 

1. labname -> a `string` datatype stating the name of the lab.
2. gt_lt -> a comparison operator. This would take `string` datatype and should take only `>` or `<` as value.
3. value -> a `float` data type that indicated the value of a particular lab test.
4. labs_data -> a dictionary contain data on all the labs. The dictionary should have the format as returned by the parse data function and must have `labname`, `PatientID` and `LabValue` as keys.

Output: Returns a list of unique PatientIDs that have visited that lab atleast once have a labvalue for that test greater than the specified level.


**Function 4**

Name: patient_age_on_first_test

Description: This function gives a the age of a specific patient on the data of their first test.

Arguements: 

1. patientID: a `string` datatype stating the ID of the patient, whose age we want.
2. labs_data: -> a dictionary contain data on all the labs. The dictionary should have the format as returned by the parse data function and must have `PatientID` and `LabDateTime` as keys. The values corresponding to `LabDateTime` key should follow the format `YYYY-mm-dd HH:MM:SS.MS` where `SS.MS` indicated seconds and microseconds.
3. patient_data: a dictionary containing information on all the patients. This dictionary should have the format that is similar to the one returned by the parse_data function above. The data should have a `PatientDateOfBirth` column and `PatientID` column.  The values corresponding to `PatientDateOfBirth` key should follow the format `YYYY-mm-dd HH:MM:SS.MS` where `SS.MS` indicated seconds and microseconds.

Output: Returns an `integer` that tells us the age of the specified patient on their first test.

#### Testing

To test the functions, you will require the `Pytest` module and will also require you to load the test data files uploaded on the same repository. All the functions have been tested in the `test.py` file. We shall run the command `pytest tests.py` in the terminal to check if the function pass the tests.