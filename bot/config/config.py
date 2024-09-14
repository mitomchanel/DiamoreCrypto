from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    CLICKS: list[int] = [800, 1000]

    AUTO_UPGRADE_CLICKING_POWER: bool = True
    AUTO_UPGRADE_CLICKING_POWER_LEVEL: int = 20

    AUTO_UPGRADE_TIMER: bool = True
    AUTO_UPGRADE_TIMER_LEVEL: int = 20

    AUTO_UPGRADE_REDUCE_COOLDOWN: bool = True
    AUTO_UPGRADE_REDUCE_COOLDOWN_LEVEL: int = 20

    REF_ID: str = '350874250'

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()


