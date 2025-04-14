from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug: bool = False

    database_url: str

    reset_password_token_secret: str
    verification_token_secret: str
    access_token_lifetime: int = 60 * 60 * 24 * 30

    upload_book_images_dir: str = "uploads"
    upload_book_images_url: str = "/uploads"

    pagination_page_size: int = 50

    celery_broker_url: str
    celery_result_backend: str

    frontend_url: str = "http://localhost:8001/"

    jinja_password_reset_template: str = "password_reset.html"
    jinja_password_verify_template: str = "verify_account.html"

    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_user: str
    smtp_password: str
    smtp_from_email: str = "noreply@ibook.com"
    smtp_tls: bool = True

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
