from pydantic import BaseSettings


class Settings(BaseSettings):
    Start_DT: str
    END_DT: str


settings = Settings()