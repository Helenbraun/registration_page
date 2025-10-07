import pydantic


class Config(pydantic.BaseSettings):
    base_url:str = 'https://demoqa.com'
    driver_name: str = 'chrome'
    window_height: int = 1024
    window_width: int = 768
    timeout: float = 3.0
