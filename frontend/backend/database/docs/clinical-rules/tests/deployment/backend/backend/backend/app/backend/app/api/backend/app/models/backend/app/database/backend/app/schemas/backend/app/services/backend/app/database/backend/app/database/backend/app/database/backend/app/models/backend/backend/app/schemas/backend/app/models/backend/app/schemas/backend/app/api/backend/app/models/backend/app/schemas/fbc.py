from pydantic import BaseModel

class FBCRequest(BaseModel):
    patient_name: str
    age: int
    sex: str
    lab_number: str

    hb: float
    pcv: float
    rbc: float
    wbc: float
    platelets: float

    mcv: float
    mch: float
    mchc: float
    rdw: float

    neutrophils: float
    lymphocytes: float
    monocytes: float
    eosinophils: float
    basophils: float
