from sqlalchemy import Column, Integer, Float, String
from ..database.database import Base

class FBCResult(Base):
    __tablename__ = "fbc_results"

    id = Column(Integer, primary_key=True, index=True)

    patient_name = Column(String(150), nullable=False)
    age = Column(Integer)
    sex = Column(String(10))
    lab_number = Column(String(50), unique=True)

    hb = Column(Float)
    pcv = Column(Float)
    rbc = Column(Float)
    wbc = Column(Float)
    platelets = Column(Float)

    mcv = Column(Float)
    mch = Column(Float)
    mchc = Column(Float)
    rdw = Column(Float)

    neutrophils = Column(Float)
    lymphocytes = Column(Float)
    monocytes = Column(Float)
    eosinophils = Column(Float)
    basophils = Column(Float)
