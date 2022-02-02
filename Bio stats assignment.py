"""Bio-Stats 821 Assignment 3 Mohammad Anas."""

from typing import Union, Any
from datetime import datetime


def parse_data(filename: str) -> dict[str, list[str]]:
    """Return data as dictionary, column names as keys, lists as values."""
    data_lst = []  # a list of  list of each data entry.  O(1)
    with open(filename, encoding="UTF-8-sig") as file:  # we open the file  O(1)
        for line in file:  # Loop over each line O(N)
            line1 = line.split(  # O(N) -> for split function
                "\t"
            )  # to split we search for the delimiter through the string and
            # to do that, we have to loop over it.
            # we add element to each element.
            data_lst.append(line1)  # O(1) (amortized)

    # O(1) + O(1) + O(N*(N+1)) complexity uptil now

    data_dict = dict()  # O(1).  we create empty dictionary
    # we loop over the index of each element in a list (columns on the data)

    for i in range(len(data_lst[1])):  # O(N).
        values = []  # create a list of values O(1)
        for row in range(len(data_lst)):  # loop over each row.  O(N)
            if row == 0:  # check if its a header row O(1)
                key = data_lst[row][i]  # O(1) # create key variable as a column name
            else:  # either of the two operation performed
                values.append(data_lst[row][i])  # O(1)

            # check condition O(1) and performing required operation O(1)

        # append to values if not a column name
        # our final dictionary will have column names as keys and values will be
        # a list of all the elements corresponding to a column name for example
        # Patient ID is column name and a list of all patient IDs is the value of that key
        data_dict[key] = values  # insert key and value into dictionary
    # O(1) +O(N((1+N(1+1)) +1))
    return data_dict  # O(1)


# complexity of parse data function
# O(1) + O(1) + O(N*(N+1)) + O(1) +O(N((1+N(1+1)) +1)) + O(1)
# O(4) + O(N^2 + N) +  O(2N^2 + 2N)
# O(3N^2 + 3N + 4) ->  `O(N^2)`


def num_older_than(age: Union[int, float], patient_data: dict[str, list[Any]]) -> int:
    """Return number of patients greater than age."""
    today_date: datetime = datetime.today()  # O(1) generate todays date

    patient_data["PatientDateOfBirth"] = [
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
    lab: str, gt_lt: str, value: float, data: dict[str, list[Any]]
) -> list[str]:
    """Return unique Patients visiting given lab with results >/< value."""
    # we raise a value error if the gt_lt does not have correct value
    if gt_lt != ">" and gt_lt != "<":  # O(2) two conditions checked
        raise ValueError(f"Arguement gt_lt does not accept the value {gt_lt}")  # O(1)

    patients = []  # create an empty list  O(1)
    for i in range(len(data["LabName"])):  # O(N)

        # loop over the index of lists in our data dictionaries
        # if the opertion is > (greater than)
        # check if labname for that index is the given lab and if the lab
        # value is greater than given value. If yes then append
        # patient ID to patients.

        if gt_lt == ">":  # O(1)
            if (data["LabName"][i] == lab) and (
                float(data["LabValue"][i]) > value
            ):  # O(2)
                patients.append(data["PatientID"][i])  # O(1)

        # we do the exact opposite here and given the time
        # complexity of both  conditions is the same
        # and only one of the conditions will run for each value
        elif gt_lt == "<":  # O(1)
            if (data["LabName"][i] == lab) and (
                float(data["LabValue"][i]) < value
            ):  # O(2)
                patients.append(data["PatientID"][i])  # O(1)

        # even in the worst case the statements under condition gt_lt =='>'
        # will run or gt_lt == '<' will run
        # complexity of above loop is O(N(1+2+1)) -> O(4N) -> O(N)

    unique_patients = set(patients)  # O(N)
    unique_patients_ = list(unique_patients)  # O(N)
    # both the conversions above have a linear time complexity as
    # we iterate over each element and add the element to a
    # (list or set) depending on the conversion
    return unique_patients_  # O(1)


# complexity of the above function is O(2+1+1+N+N+N+1) -> O(5+3N) -> O(N)

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
