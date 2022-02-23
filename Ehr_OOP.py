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

    def extract_info(self, filename):
        """Extract info of a patient ID from text file."""
        with open(filename, encoding="UTF-8-sig") as file:
            counter = 0
            for line in file:
                counter += 1
                line = line.split("\t")
                line[-1] = line[-1][:-1]
                if counter == 1:
                    key = line

                else:
                    if line[0] == self.PatientID:
                        val = line

        patientinfo = dict(zip(key, val))

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


class lab:
    """Store Lab data."""

    def __init__(self, Labname):
        """Instantiate Lab Class."""
        self.labname = Labname
        self.units = None
        self.value = None

    def extract_lab_info(self, filename):
        """Extract Lab info."""
        Units = []
        Values = []
        with open(filename, encoding="UTF-8-sig") as file:
            counter = 0
            for line in file:
                counter += 1
                line = line.split("\t")
                if counter == 1:
                    unitindex = line.index("LabValue")
                    valueindex = line.index("LabUnits")
                else:
                    if line[0] == self.labname:
                        Units.append(line[unitindex])
                        Values.append(line[valueindex])

        self.units = Units
        self.value = Values
