"""SQLite3 Assignment."""
import sqlite3
from datetime import date, datetime


def create_database(labpath: str, patientpath: str, dbpath: str) -> None:
    """Insert information into the ehr database and extracts
    information from the database to create a patient class that stores all
    the information. For the lab data we add an OBSID columns as primary key
    this serves as a unique idetifier."""

    con = sqlite3.connect(dbpath)
    cur = con.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS Patients(\
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
        """CREATE TABLE IF NOT EXISTS Labs(\
            [ObsID] INTEGER PRIMARY KEY AUTOINCREMENT,\
            [PatientID] TEXT NOT NULL,\
            [AdmissionID] TEXT NOT NULL,\
            [LabName] TEXT,\
            [LabValue] REAL,\
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
                line2[3] = float(line2[3])
                cur.execute(
                    "INSERT INTO Labs (PatientID, AdmissionID,\
                    LabName, LabValue, LabUnits, LabDateTime) values (?,?,?,?,?,?)",
                    line2,
                )
    con.commit()
    cur.close()


# Below we define a lab class
# This lab class takes lab ObsID to identify it and
# to make a lab class


class Lab:
    """Store Lab data."""

    def __init__(self, ObsID: int, dbpath: str) -> None:
        """Instantiate a class."""
        self.ObsID = ObsID
        con = sqlite3.connect(dbpath)
        self.cur = con.cursor()

    def __str__(self) -> str:
        """Lab Class Representation."""
        return str(self.ObsID) + " observation in database."  # O(1)

    @property
    def name(self) -> str:
        """Return lab units."""
        name: tuple = self.cur.execute(
            """select LabName from Labs where ObsID= ?""",
            (self.ObsID,),
        ).fetchone()
        return name[0]

    @property
    def unit(self) -> str:
        """Return lab units."""
        unit: tuple = self.cur.execute(
            """select LabUnits from Labs where ObsID= ?""",
            (self.ObsID,),
        ).fetchone()
        return unit[0]

    @property
    def value(self) -> float:
        """Return lab units."""
        value: tuple[str] = self.cur.execute(
            """select LabValue from Labs where ObsID = ?""", (self.ObsID,)
        ).fetchone()
        return float(value[0])

    @property
    def date(self) -> datetime:
        """Return the date of test."""
        DOB: str = self.cur.execute(
            """select LabDateTime from Labs where ObsID = ?""",
            (self.ObsID,),
        ).fetchone()[0]
        DOB_dt: datetime = datetime.strptime(DOB, "%Y-%m-%d %H:%M:%S.%f")
        return DOB_dt


# below we create a patient class that extracts
# relevant information from the database
# It also includes information about the Labs
# attended by the patient. These labs are storing
# information in form of lab class.
class Patient:
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
            """select ObsID from Labs where PatientID = ?""", (self.id,)
        ).fetchall()

        labs_cl: list[Lab] = [Lab(i[0], self.dbpath) for i in labs]
        return labs_cl

    @property
    def age(self):
        """Calculate patient age."""
        today = datetime.today()
        return int((today - self.dateofbirth).days / 365.25)

    @property
    def age_first_admission(self):
        """Calculate age at first lab test."""
        # get min lab date for the patient
        mindate = min([i.date for i in self.labs])
        # get age at the first lab visit
        return int((mindate - self.dateofbirth).days / 365.25)

    def __eq__(self, other):
        """Test if two Patient Classes are equal."""
        if self.id == other.id and self.dbpath == other.dbpath:
            return True
        else:
            return False


def store_patient_class(dbpath: str) -> dict[str, Patient]:
    """Store patient IDs in patient class using a dictionary."""
    con = sqlite3.connect(dbpath)
    cur = con.cursor()
    data_dict: dict[str, Patient] = {}
    ids: list[tuple[str]] = cur.execute("select PatientID from Patients").fetchall()
    for i in ids:
        data_dict[i[0]] = Patient(i[0], dbpath)
    return data_dict


def num_older_than(patient_dic: dict[str, Patient], age_thresh: int) -> int:
    """Calculate the number of people older than age Thresh."""
    counter: int = 0  # O(1)
    for i in patient_dic:  # O(N)
        if patient_dic[i].age > age_thresh:  # 0(1)
            counter += 1  # O(1)

    return counter


def sick_patients(
    dbpath: str, gt_lt: str, lab_value: float, lab_name: str
) -> list[str]:
    """Return sick patient with lab value greater or less than the given lab value."""
    con = sqlite3.connect(dbpath)
    cur = con.cursor()
    if gt_lt == ">":
        unique_ids = cur.execute(
            "select Distinct PatientID from Labs where LabName = ? and LabValue > ?",
            (lab_name, lab_value),
        )
    elif gt_lt == "<":
        unique_ids = cur.execute(
            "select Distinct PatientID from Labs where LabName = ? and LabValue < ?",
            (lab_name, lab_value),
        )
    else:
        raise ValueError

    return [i[0] for i in unique_ids]
