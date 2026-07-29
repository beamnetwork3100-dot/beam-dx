import os

class Settings:
    PROJECT_NAME = "Beam Dx"
    VERSION = "0.1.0"

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://beamdx:password@localhost:5432/beamdx"
    )

settings = Settings()
