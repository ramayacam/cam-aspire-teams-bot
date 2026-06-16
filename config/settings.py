from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    # Azure
    AZURE_APP_ID: str = os.getenv("AZURE_APP_ID", "")
    AZURE_APP_PASSWORD: str = os.getenv("AZURE_APP_PASSWORD", "")
    AZURE_TENANT_ID: str = os.getenv("AZURE_TENANT_ID", "")

    # Supabase
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_ANON_KEY: str = os.getenv("SUPABASE_ANON_KEY", "")
    SUPABASE_SERVICE_ROLE_KEY: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")

    # Claude
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")

    # Bot
    BOT_PORT: int = int(os.getenv("BOT_PORT", "8000"))

    class Config:
        env_file = ".env"

settings = Settings()
