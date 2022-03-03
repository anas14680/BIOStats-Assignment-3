### EHR LIBRARY

This package has been made to facilitate patient data analytics. This can be useful in evaluating clinical trials and analyzing medical data. The package has been written in python. 

#### Installation and Requirements

To install this package, you can clone the github repository it has been placed on. The following python modules are required for successful implimentation of this module.

1) Time
2) Pytests

#### Functionalities

The package facilitates a number of functionalities. Below we have gone over each of these, the function name associated with each functionality, and the how to sucessfully execute each function. All the functions take the arguements in the below mentioned order. 

#### Data Storage
The data is stored in class objects called `Patient` and `Lab`. To extract the data from the text files and store it in these classes, we have defined a function called parse data. We will go over what our class objects store data and how our parse data function works.

**Class Lab**

The Lab Class stores the following information in form of class attributes.
1. Labname
2. Lab Units
3. Lab Value
4. Lab Date Time of Patient Visit

**Class Patient**

The Patient Class stores the following information in form of class attributes.
1. PatientID
2. Patient Gender
3. Patient Date Of Birth
4. Patient Race
5. Labs visited by that patient in form of a list of lab class explained above.

The Patient Class also provides us with additional information in form for property methods that behave as attributes.
1. The Pateint's current age.
2. Patient's age on his first lab test.


**Parse Data Function**

Description: Restructures that data into a `dictionary` data type that can be easily manipulated to suit your needs.

Arguements: 

1. lab_file_path -> this is the path for `TAB` delimited `txt` file which contains all the data. 
2. patient_file_path -> this is the path for `TAB` delimited `txt` file which contains all the data.
3. get lab dict -> takes a boolean value. By default set to false.

Output: Returns data as a `dictionary`, whose keys are the 'PatientID' and the value for each key will a be class object corresponding to the patient.



#### Analytical Functions

**num_older_than**

Description: This function tells us the number of patients older than a certain age.

Arguements: 

1. age -> Can be an `integer` or a `float`.
2. Patient_dictionary -> This dictionary have key as patient ID and the value should be the Patient Class

Outputs: Returns the number of patients older than the specified age.

**Sick_patients**


Description: Returns the ID of all the `unique` patients that are visiting a certain lab. 

Arguements: 

1. labname -> a `string` datatype stating the name of the lab.
2. labs_data -> a dictionary containing keys as patientID and the values are a list of Labs attended by that patient. 
3. gt_lt -> a comparison operator. This would take `string` datatype and should take only `>` or `<` as value.
4. value -> a `float` data type that indicated the value of a particular lab test.


Output: Returns a list of unique PatientIDs that have visited that lab atleast once have a labvalue for that test greater than the specified level.

#### Testing

To test the functions, you will require the `Pytest` module and will also require you to load the test data files uploaded on the same repository. All the functions have been tested in the `test.py` file. We shall run the command `pytest tests.py` in the terminal to check if the function pass the tests.


