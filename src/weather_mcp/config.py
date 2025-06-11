"""
配置管理模块
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    """应用配置"""
    amap_api_key: str = Field(..., env="AMAP_API_KEY")
    host: str = Field("0.0.0.0", env="HOST")
    port: int = Field(8000, env="PORT")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings() 