from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    app_name: str = "Job Tracker App" 

    #Database Settings Configuration
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    secret_key: str
    
    @property
    def database_url(self) -> URL:
        database_url_info = URL.create(
            drivername = "postgresql+asyncpg",
            username = self.postgres_user,
            password = self.postgres_password,
            host = self.postgres_host,
            port = self.postgres_port,
            database = self.postgres_db, 
        )
        return database_url_info

#read and check all settings
settings = Settings()