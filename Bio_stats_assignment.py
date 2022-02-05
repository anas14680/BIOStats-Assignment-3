"""Bio-Stats 821 Assignment 3 Mohammad Anas."""

from typing import Union, Any
from datetime import datetime


def parse_data(filename: str) -> dict[str, list[str]]:
    """Return data as dictionary, column names as keys, lists as values."""
    data_lst: list[list[str]] = []  # a list of  list of each data entry.  O(1)
    with open(filename, encoding="UTF-8-sig") as file:  # we open the file  O(1)
        for line in file:  # Loop over each line O(N)
            line_list: list[str] = line.split(  # O(N) -> for split function
                "\t"
            )  # to split we search for the delimiter through the string and
            if line_list[-1][-1] == "\n":  # O(2)
                line_list[-1] = line_list[-1][:-1]  # O(2)
            # the above code removes \n from the last elemnet
            # of each line if there is \n there

            # to do that, we have to loop over it.
            # we add element to each element.
            data_lst.append(line_list)  # O(1) (amortized)
    # returns blank dictionary if txt file contains nothing
    if (
        len(data_lst) == 0
    ):  # O(2) calculate length and check if 0                                      ###########test case
        return {}  # O(1)

    # O(1) + O(1) + O(N*(N+1 + 2)) complexity uptil now

    data_dict: dict = dict()  # O(1).  we create empty dictionary
    # we loop over the index of each element in a list (columns on the data)

    for i in range(len(data_lst[0])):  # O(N).
        values: list = []  # create a list of values O(1)
        for row in range(len(data_lst)):  # loop over each row.  O(N)
            if row == 0:  # check if its a header row O(1)
                key = data_lst[row][i]  # O(1) # create key variable as a column name
            else:  # either of the two operation performed
                values.append(
                    data_lst[row][i]
                )  # O(1)                                                 ##########test case on columns

            # check condition O(1) and performing required operation O(1)

        # append to values if not a column name
        # our final dictionary will have column names as keys and values will be
        # a list of all the elements corresponding to a column name for example
        # Patient ID is column name and a list of all patient IDs is the value
        # of that key
        data_dict[key] = values  # insert key and value into dictionary
    # O(1) +O(N((1+N(1+1)) +1))
    return data_dict  # O(1)


# complexity of parse data function
# O(1) + O(1) + O(N*(N+1 + 2)) + O(1) +O(N((1+N(1+1)) +1)) + O(1) + O(2)
# O(6) + O(N^2 + N) +  O(2N^2 + 2N) + O(2)
# O(3N^2 + 3N + 8) ->  `O(N^2)`


def num_older_than(
    age: Union[int, float], patient_data: dict[str, list[Any]]
) -> Union[str, int]:
    """Return number of patients greater than age."""
    today_date: datetime = datetime.today()  # O(1) generate todays date
    #####################test case######################
    if "PatientDateOfBirth" not in patient_data.keys():  # O(1)
        return "No information found regarding Age"  # O(1)

    patient_data["PatientDateOfBirth_dtformat"] = [
        datetime.strptime(i, "%Y-%m-%d %H:%M:%S.%f")
        for i in patient_data["PatientDateOfBirth"]  # list comprehension
    ]  # we just convert every date to datetime O(N) method and make a
    # list if it O(N). Insert this list as value to our
    # data dictionary  O(N+N+1) -> O(2N+ 1) -> O(N)

    patient_data["Age"] = [
        ((today_date - i).days / 365.25) for i in patient_data["PatientDateOfBirth"]
    ]
    # in the above list comprehension
    # we insert another value in dictionary,O(1)
    # make a list. Loop over birthdate of patients and subtract the todays date O(N)
    # extract days from the difference O(N)
    #  divide by 365.25 (0.25 for leap year) O(N)
    # append these values to the list.
    # O(N+N+N+N) -> O(4N) -> O(N)

    counter: int = 0  # create a new variable to count the number greater than age. O(1)
    for i in patient_data["Age"]:  # We loop over age and see if the age if
        if i > age:  # a number is greater than the given value
            counter += 1  # we add 1 to the value of counter and
            # than assign it to to the counter

    # complexity of the above loop O(N(1+2)) -> O(3N) -> O(N)

    return counter  # O(1)


# complexity of num_older_than function is
# O(N) + O(N) + O(N) + O(2) -> O(N)


def sick_patients(
    labname: str, gt_lt: str, value: float, labs_data: dict[str, list[Any]]
) -> Union[str, list[str]]:
    """Return unique Patients visiting given lab with results >/< value."""
    # we raise a value error if the gt_lt does not have correct value
    if (
        gt_lt != ">" and gt_lt != "<"
    ):  # O(2) two conditions checked                                                       ######## test case
        raise ValueError(f"Arguement gt_lt does not accept the value {gt_lt}")  # O(1)

    patients: list[str] = []  # create an empty list to store patient names  O(1)
    for i in range(len(labs_data["LabName"])):  # O(N)

        # loop over the index of lists in our data dictionaries
        # if the opertion is > (greater than)
        # check if labname for that index is the given lab and if the lab
        # value is greater than given value. If yes then append
        # patient ID to patients.

        if gt_lt == ">":  # O(1)
            if (labs_data["LabName"][i] == labname) and (
                float(labs_data["LabValue"][i]) > value
            ):  # O(2)
                patients.append(labs_data["PatientID"][i])  # O(1)

        # we do the exact opposite here and given the time
        # complexity of both  conditions is the same
        # and only one of the conditions will run for each value
        elif gt_lt == "<":  # O(1)
            if (labs_data["LabName"][i] == labname) and (
                float(labs_data["LabValue"][i]) < value
            ):  # O(2)
                patients.append(labs_data["PatientID"][i])  # O(1)

        # even in the worst case the statements under condition gt_lt =='>'
        # will run or gt_lt == '<' will run
        # complexity of above loop is O(N(1+2+1)) -> O(4N) -> O(N)

    unique_patients: set[str] = set(patients)  # O(N)
    unique_patients_: list[str] = list(unique_patients)  # O(N)
    # both the conversions above have a linear time complexity as
    # we iterate over each element and add the element to a
    # (list or set) depending on the conversion
    return unique_patients_  # O(1)                                       #################test case on zero patients meeting requirement

    # complexity of the above function is O(2+1+1+N+N+N+1) -> O(5+3N) -> O(N)


def patient_age(
    patientID: str, labs_data: dict[str, list[str]], patient_data: dict[str, list[str]]
) -> Union[int, str]:
    """Return the age oof patient on their first test date."""
    # returns this string if Patient not in data
    if (
        patientID not in patient_data["PatientID"]
    ):  # O(1)                                                                                  ###########test case
        return f"No information available on patient with ID:{patientID}"  # O(1)

    if (
        "PatientDateOfBirth" not in patient_data.keys()
    ):  # O(1)                                                                                  ###########test cast
        return "No information found regarding Age"  # O(1)

    # create an empty list to store Visit dates on the patient
    labvisit_dates: list[str] = []  # O(1)
    # loop of patients in labs data and store their information
    # on visit dates in the above list
    # we use indices to do this where ever the patient name is found
    # their index position in the list to access their information on
    # visit date
    for i in range(len(labs_data["PatientID"])):  # O(N)
        if labs_data["PatientID"][i] == patientID:  # O(3) extract list from dictionary
            # then extract element from that list
            #  then equate
            labvisit_dates.append(
                labs_data["LabDateTime"][i]
            )  # O(3) # extract list from dictionary
            # extract element from list
            # append to labvisit date
    # O(N(3+3))-> O(6N)-> O(N)

    # we use list comprehension to convert string dates to datetime format
    # time complexity of below string: O(N) since interate over visit lists and
    # converts each element to datetime format
    visit_dates_dt: list[datetime] = [
        datetime.strptime(i, "%Y-%m-%d %H:%M:%S.%f") for i in labvisit_dates
    ]  # O(N)

    # we loop over patients data and extract their date of birth
    # we loop of patientID and extract the index from the list
    # use that index to extract the patients date of birth
    for i in range(len(patient_data["PatientID"])):  # O(N)
        if (
            patient_data["PatientID"][i] == patientID
        ):  # O(3) extract list from dictionary
            # extract element from list
            # check if equal to patientID
            patient_DOB = patient_data["PatientDateOfBirth"][
                i
            ]  # O(3) extract list, extract
            # extract element and assign
    # time complexity of above loop: O(N(3+3))-> #O(N)

    # patient date of birth is stored in the datetime format
    patient_DOB_dtformat = datetime.strptime(
        patient_DOB, "%Y-%m-%d %H:%M:%S.%f"
    )  # O(1)
    # we then take the minimum date from that
    # patients visiting dates to labs
    first_test_date = min(visit_dates_dt)  # O(N) since it loops over each element
    # and compares them
    # subtract patients date of birth from first test date to get age in years
    age = int((first_test_date - patient_DOB_dtformat).days / 365.25)  # O(4)
    # the above line does 4 four operation: subtract dates, extract days,
    #  divideby 365 to get years and assign
    return age  # O(N)

    # O(5) +O(N) + O(N) +O(N) +O(1) +O(N) +O(4) -> O(8+4N)-> O(N)


if __name__ == "__main__":
    patient = parse_data(
        "/Users/mohammadanas/Desktop/Duke MIDS/Spring 2021/SoftwareTools/\
Assignment 2/PatientCorePopulatedTable.txt"
    )
    tests = parse_data(
        "/Users/mohammadanas/Desktop/Duke MIDS/Spring 2021/SoftwareTools/\
Assignment 2/LabsCorePopulatedTable.txt"
    )

    print(sick_patients("METABOLIC: ALBUMIN", ">", 3.1, tests))
    print(num_older_than(51.2, patient))
    print(tests["LabDateTime"])
