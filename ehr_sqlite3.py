"""SQLite3 Assignment."""
import sqlite3
from datetime import date, datetime


# the function insert information into the ehr database
# and extracts information from the database to create
# a patient class that stores all the information.
def create_database(labpath: str, patientpath: str, dbpath: str) -> None:
    """Extract information from txt file."""
    con = sqlite3.connect(dbpath)
    cur = con.cursor()

    cur.execute(
        """CREATE TABLE Patients(\
            [PatientID] TEXT PRIMARY KEY,\
            [PatientGender] TEXT,\
            [PatientDateofBirth] TEXT,\
            [PatientRace] TEXT,\
            [PatientMaritalStatus] TEXT,\
            [PatientLanguage] TEXT,\
            [PatientPopulationPercentageBelowPoverty] TEXT\
            )"""
    )

    cur.execute(
        """CREATE TABLE labs(\
            [PatientID] TEXT NOT NULL,\
            [AdmissionID] TEXT NOT NULL,\
            [LabName] TEXT,\
            [LabValue] TEXT,\
            [LabUnits] TEXT,\
            [LabDateTime] TEXT\
            )"""
    )

    with open(patientpath, encoding="UTF-8-sig") as file:
        counter: int = 0

        for line in file:
            counter += 1
            line1: list[str] = line.split("\t")
            line1[-1] = line[-1][:-1]

            if counter == 1:
                pass
            else:
                cur.execute("INSERT INTO Patients values (?,?,?,?,?,?,?)", line1)

    with open(labpath, encoding="UTF-8-sig") as file:
        counter2: int = 0

        for line in file:
            counter2 += 1
            line2: list[str] = line.split("\t")
            line2[-1] = line2[-1][:-1]

            if counter2 == 1:
                pass
            else:
                cur.execute("INSERT INTO Labs values (?,?,?,?,?,?)", line2)
    cur.close()


# Below we define a lab class
# This lab class takes lab name and patientID
# to make a lab class
# we take into account the lab and patient
# becasue we do not have a unique identifier in
# our lab class.


class Lab:
    """Store Lab data."""

    def __init__(self, name: str, patientID: str, dbpath: str) -> None:
        """Instantiate a class."""
        self.name: str = name
        self.patientID: str = patientID
        con = sqlite3.connect(dbpath)
        self.cur = con.cursor()

    def __str__(self) -> str:
        """Lab Class Representation."""
        return str(self.name) + " attended by " + str(self.patientID)  # O(1)

    @property
    def units(self) -> str:
        """Return lab units."""
        unit: tuple = self.cur.execute(
            """select LabUnits from Labs where LabName = ? and PatientID = ?""",
            (
                self.name,
                self.patientID,
            ),
        ).fetchone()
        return unit[0]

    @property
    def value(self) -> float:
        """Return lab units."""
        value: tuple[str] = self.cur.execute(
            """select LabValue from Labs where LabName = ? and PatientID = ?""",
            (self.name, self.patientID),
        ).fetchone()
        return float(value[0])

    @property
    def labdate(self) -> datetime:
        """Return the date of test."""
        DOB: str = self.cur.execute(
            """select LabDateTime from Labs where LabName = ? and PatientID = ?""",
            (self.name, self.patientID),
        ).fetchone()[0]
        DOB_dt: datetime = datetime.strptime(DOB, "%Y-%m-%d %H:%M:%S.%f")
        return DOB_dt


# below we create a patient class that extracts
# relevant information from the database
class patient:
    """Store a patient data."""

    def __init__(self, id: str, dbpath: str) -> None:
        """Instantiate patient class."""
        self.id: str = id
        self.dbpath: str = dbpath
        con = sqlite3.connect(dbpath)
        self.cur = con.cursor()

    def __str__(self) -> str:
        """Patient Class Representation."""
        return self.id + " Class"  # O(1)

    @property
    def dateofbirth(self) -> datetime:
        """Extract DOB from database."""
        DOB: str = self.cur.execute(
            """select PatientDateofBirth from Patients where PatientID = ?""",
            (self.id,),
        ).fetchone()[0]
        DOB_dt: datetime = datetime.strptime(DOB, "%Y-%m-%d %H:%M:%S.%f")
        return DOB_dt

    @property
    def gender(self) -> str:
        """Extract gender from database."""
        gen: tuple[str] = self.cur.execute(
            """select PatientGender from Patients where PatientID = ?""", (self.id,)
        ).fetchone()
        return gen[0]

    @property
    def race(self) -> str:
        """Extract race from database."""
        race: tuple[str] = self.cur.execute(
            """select PatientRace from Patients where PatientID = ?""", (self.id,)
        ).fetchone()
        return race[0]

    @property
    def labs(self) -> list[Lab]:
        """Exctract all labs attended by patient."""
        labs: list[tuple[str]] = self.cur.execute(
            """select LabName, PatientID from Labs where PatientID = ?""", (self.id,)
        ).fetchall()

        labs_cl: list[Lab] = [Lab(i[0], i[1], self.dbpath) for i in labs]
        return labs_cl


# patient classes instantiated and stored
# to a dictionary
def parse_data(patient_path, dbpath: str) -> dict[str, patient]:
    """Parse the data."""
    patient_data: dict[str, patient] = {}
    with open(patient_path, encoding="UTF-8-sig") as file:
        counter: int = 0

        for line in file:
            counter += 1
            line1: list[str] = line.split("\t")
            if counter == 1:
                pass
            else:
                patient_data[line[0]] = patient(line[0], dbpath)

    return patient_data
