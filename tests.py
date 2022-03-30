"""Testing module."""
from datetime import datetime
import pytest
from ehr_sqlite3 import Patient, Lab, store_patient_class, create_database


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

