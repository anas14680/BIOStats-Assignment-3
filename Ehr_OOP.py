"""Bio stats assignment #OOP Mohammad Anas."""


from datetime import datetime
from typing import Union


class Patient:
    """Store a patient data."""

    def __init__(
        self,
        PatientID: str,
        gender: str,
        DOB: Union[str, datetime],
        race: str,
        labs: list[str],
    ) -> None:
        """Instantiate Patient Class."""
        self.patientID: str = PatientID  # O(1)
        self.gender: str = gender  # O(1)
        self.DOB: datetime = datetime.strptime(DOB, "%Y-%m-%d %H:%M:%S.%f")  # O(2)
        self.race: str = race  # O(1)
        self.labs: list[str] = labs  # O(1)
        # class instantiation takes O(6) complexity

    def __str__(self):
        """Patient Class Representation."""
        return self.patientID + " Class"  # O(1)

    @property
    def age(self):
        """Calculate patient age."""
        today = datetime.today()  # O(2)
        return int((today - self.DOB).days / 365.25)  # O(4)

    @property
    def age_first_admission(self):
        """Calculate age at first lab test."""
        # get min lab date for the patient
        mindate = min([i.labDate for i in self.labs])  # O(P)
        # get age at the first lab visit
        return int((mindate - self.DOB).days / 365.25)  # O(4)


class Lab:
    """Store Lab data."""

    def __init__(
        self,
        Labname: str,
        units: str,
        value: Union[str, float],
        labDate: Union[str, datetime],
    ) -> None:
        """Instantiate Lab Class."""
        self.labname: str = Labname  # O(1)
        self.units: str = units  # O(1)
        self.value: Union[float, str] = float(value)  # O(1)
        self.labDate: Union[str, datetime] = datetime.strptime(
            labDate, "%Y-%m-%d %H:%M:%S.%f"
        )  # O(2)
        # instantiation of this class takes #O(5)

    def __str__(self):
        """Lab Class Representation."""
        return self.labname  # O(1)


def parse_data(
    lab_file: str, patient_file: str, get_lab_dict: bool = False
) -> dict[str, Patient]:
    """Parse lab and patient data.

    The first thing that happens is that we parse our lab data
    and create a class of each lab. These classes are stored in
    a dictionary where key is a patient ID and the value is a
    list of lab classes visited by that patient.

    Then we parse the patient data. We create another dictionary
    where the key PatientID and value is the Patient class. Within the
    patient class, we store the lab classes, visited by that patient.
    To do this we use the lab dictionary used above. This dictionary
    is returned as the output."""

    lab_dict: dict[str, list[Lab]] = {}  # O(1)
    patient_dict: dict[str, Patient] = {}  # O(1)

    with open(lab_file, encoding="UTF-8-sig") as file:  # O(1)
        counter: int = 0  # O(1)

        for line_ in file:  # O(M)
            counter += 1  # O(1)
            line = line_.split("\t")  # O(L)
            # where L is the number of columns
            # in the text file.
            line[-1] = line[-1][:-1]  # O(2)

            if counter == 1:  # O(1)
                pass
            else:
                patientID: str = line[0]  # O(2)
                labname: str = line[2]  # O(2)
                labvalue: str = line[3]  # O(2)
                labunits: str = line[4]  # O(2)
                labDate: str = line[5]  # O(2)
                # all the above have O(2) complexity
                # because we extract and assign (2 operations)

                lab_class: Lab = Lab(labname, labunits, labvalue, labDate)  # O(6)
                # instantion of lab class is O(5) and we assign this to
                # lab_class variable

                if patientID not in lab_dict:  # O(1)
                    lab_dict[patientID] = [lab_class]  # O(2)
                else:
                    lab_dict[patientID].append(lab_class)  # O(2)

    with open(patient_file, encoding="UTF-8-sig") as file:  # O(1)

        counter = 0  # O(1)

        for line_ in file:  # O(N)
            counter += 1  # O(1)
            line = line_.split("\t")  # O(L)
            # where L is number of columns
            # in patient file.
            line[-1] = line[-1][:-1]  # O(3)

            if counter == 1:  # O(1)
                pass
            else:
                patientID = line[0]  # O(2)
                gender = line[1]  # O(2)
                DOB = line[2]  # O(2)
                race = line[3]  # O(2)
                labs = lab_dict[patientID]  # O(2)

                patient_dict[patientID] = Patient(
                    patientID, gender, DOB, race, labs
                )  # O(7)

    if get_lab_dict:  # O(1)
        return patient_dict, lab_dict  # O(1)
    else:  # O(1)
        return patient_dict  # O(1)


# The O(N) complexity of the above function:
# parsing the lab data file part :
# O(2) + O(M{(1+L 2 + 1 +10 + 9)})
# O(2 + M(L+23))
# O(ML) where L is vey low (number of columns in lab class)
# Now we look at the complexity of parse patient file
# O(2) +O(N(1+L+3+1+10 +7))
# O(2 +N(22+L))
# O(NL)
# There are 5 additional operations in the function with O(1)
# Total complexity -> O(5 +ML +Nl) -> O(ML +NL)
# if we assume that L remains fixed we have
# O(M+N) complexity which is linear


def num_older_than(patient_dic: dict[str, Patient], age_thresh: int) -> int:
    """Calculate the number of people older than age Thresh."""
    counter: int = 0  # O(1)
    for i in patient_dic:  # O(N)
        if patient_dic[i].age > age_thresh:  # 0(1)
            counter += 1  # O(1)

    return counter  # O(1)


# complexity for this function is
# O(1) + O(N + 1 +1) + O(1)
# O(N+2) + O(2)
# O(N+4) -> O(N)


def sick_patients(
    lab_name: str, lab_dict: dict[str, Lab], gt_lt: str, lab_value: float
) -> list[str]:
    """Return sick patient with lab value greater or less than the given lab value."""
    if gt_lt != ">" and gt_lt != "<":  # O(2) two conditions checked
        raise ValueError(f"Arguement gt_lt does not accept the value {gt_lt}")  # O(1)

    patients = []  # O(1)
    if gt_lt == ">":  # O(1)
        for i in lab_dict:  # O(N)
            for j in lab_dict[i]:  # O(N)
                if (j.labname == lab_name) and (j.value > lab_value):  # O(3)
                    patients.append(i)  # (1)
                    break  # we break to save time reduces time complexity
                # as the inner loop stops as soon as the conditions are met
                # and we dont need to convert our patients to a unique list
                # later
    # exact same complexity as the previous statement
    # note only one of the conditional statement would be run
    elif gt_lt == "<":
        for i in lab_dict:
            for j in lab_dict[i]:
                if (j.labname == lab_name) and (j.value < lab_value):
                    patients.append(i)
                    break

    return patients


# Complexity for sick patients function.
# O(3) + O(3) +O(N(N + 4))
# O(N^2 + 4N + 6) -> O(N^2) -> O(N^2)
