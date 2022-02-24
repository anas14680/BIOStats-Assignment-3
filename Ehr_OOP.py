"""Bio stats assignment #OOP Mohammad Anas."""


from datetime import datetime


class Patient:
    """Store a patient data."""

    def __init__(self, PatientID):
        """Instantiate Patient Class."""
        self.patientID = PatientID
        self.gender = None
        self.DOB = None
        self.race = None

    def __repr__(self):
        """Patient Class Representation."""
        return self.patientID + " Class"

    def store_info(self, patientinfo):
        """Extract info of a patient ID from text file."""
        self.gender = patientinfo["PatientGender"]
        self.DOB = datetime.strptime(
            patientinfo["PatientDateOfBirth"], "%Y-%m-%d %H:%M:%S.%f"
        )
        self.race = patientinfo["PatientRace"]

    @property
    def age(self):
        """Calculate patient age."""
        today = datetime.today()
        return int((self.DOB - today).days / 365.25)


class Lab:
    """Store Lab data."""

    def __init__(self, Labname):
        """Instantiate Lab Class."""
        self.labname = Labname
        self.units = []
        self.value = []
        self.patientID = []

    def __repr__(self):
        """Lab Class Represenatation."""
        return self.labname + " Class"

    def store_info(self, lab_info):
        """Extract Lab info."""
        self.value.append(lab_info["LabValue"])
        self.units.append(lab_info["LabUnits"])
        self.patientID.append(lab_info["PatientID"])


# redefine the function parse data that returns a class


def parse_data(filename, pt_lb):
    """Parse patient or lab data."""
    assert pt_lb in [
        "patient",
        "lab",
    ], "pt_lb takes patient or lab as operation"

    data_dict = {}

    with open(filename, encoding="UTF-8-sig") as file:
        counter = 0

        for line in file:
            counter += 1
            line = line.split("\t")
            line[-1] = line[-1][:-1]
            if counter == 1:
                key = line
            else:
                val = line

                information_dict = dict(zip(key, val))

                if pt_lb == "patient":
                    patient_class = Patient(information_dict["PatientID"])
                    patient_class.store_info(information_dict)
                    data_dict[information_dict["PatientID"]] = patient_class

                elif pt_lb == "lab":
                    lab_n = information_dict["LabName"]
                    if lab_n not in data_dict:
                        lab_class = Lab(lab_n)
                        lab_class.store_info(information_dict)
                        data_dict[lab_n] = lab_class
                    else:
                        data_dict[lab_n].store_info(information_dict)

    return data_dict
