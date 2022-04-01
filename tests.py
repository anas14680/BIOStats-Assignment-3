"""Testing module."""
from datetime import datetime
import pytest
import os
from ehr_sqlite3 import (
    Patient,
    Lab,
    store_patient_class,
    create_database,
    num_older_than,
    sick_patients,
)

# test the parse data function
def test_sqlite3_file():
    """Test Parse data function."""
    dbtest = "testdb.db"
    labtest = "LABS TEST.txt"
    pattest = "Patient test.txt"
    names = [
        "METABOLIC: TOTAL PROTEIN",
        "CBC: HEMATOCRIT",
        "URINALYSIS: RED BLOOD CELLS",
    ]
    values = [4.2, 3.5, 10.8]
    units = ["mg", "mg", "cm"]
    dates = [
        "2021-07-01 01:36:17.910",
        "2022-01-01 01:36:17.910",
        "2021-10-01 01:36:17.910",
    ]
    os.remove(dbtest)
    create_database(labtest, pattest, dbtest)

    anas = Patient("ANAS123", dbtest)

    assert anas.dateofbirth == datetime.strptime(
        "1996-04-04 02:45:40.547", "%Y-%m-%d %H:%M:%S.%f"
    )
    assert anas.gender == "M"
    assert anas.race == "Asian"

    for i in range(len(names)):
        assert anas.labs[i].name == names[i]
        assert anas.labs[i].unit == units[i]
        assert anas.labs[i].value == values[i]
        assert anas.labs[i].date == datetime.strptime(dates[i], "%Y-%m-%d %H:%M:%S.%f")


def test_store_patient_data():
    """Test Store Patient data."""
    dbtest = "testdb.db"
    labtest = "LABS TEST.txt"
    pattest = "Patient test.txt"
    os.remove(dbtest)
    create_database(labtest, pattest, dbtest)
    answer = store_patient_class(dbtest)
    test = {
        "ANAS123": Patient("ANAS123", dbtest),
        "JON234": Patient("JON234", dbtest),
        "RUMI874": Patient("RUMI874", dbtest),
        "JONNA465": Patient("JONNA465", dbtest),
    }

    assert answer == test


def test_age():
    """Test Store Patient data."""
    dbtest = "testdb.db"
    labtest = "LABS TEST.txt"
    pattest = "Patient test.txt"
    os.remove(dbtest)
    create_database(labtest, pattest, dbtest)
    answer = store_patient_class(dbtest)
    anas = Patient("ANAS123", dbtest)
    assert anas.age == 25


def test_age_first_admission():
    """Test Store Patient data."""
    dbtest = "testdb.db"
    labtest = "LABS TEST.txt"
    pattest = "Patient test.txt"
    os.remove(dbtest)
    create_database(labtest, pattest, dbtest)
    answer = store_patient_class(dbtest)
    anas = Patient("ANAS123", dbtest)
    assert anas.age_first_admission == 25


def test_number_older_than():
    """Test num older than function."""
    dbtest = "testdb.db"
    labtest = "LABS TEST.txt"
    pattest = "Patient test.txt"
    os.remove(dbtest)
    create_database(labtest, pattest, dbtest)
    test = {
        "ANAS123": Patient("ANAS123", dbtest),
        "JON234": Patient("JON234", dbtest),
        "RUMI874": Patient("RUMI874", dbtest),
        "JONNA465": Patient("JONNA465", dbtest),
    }
    assert num_older_than(test, 24) == 4


def test_sick_patients():
    """Test num older than function."""
    dbtest = "testdb.db"
    labtest = "LABS TEST.txt"
    pattest = "Patient test.txt"
    os.remove(dbtest)
    create_database(labtest, pattest, dbtest)
    answer = sick_patients(dbtest, ">", 10.0, "METABOLIC: TOTAL PROTEIN")
    assert answer == ["JONNA465"]
