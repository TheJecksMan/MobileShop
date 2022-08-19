TITLE: str = 'Mobile API Service'
DESCRIPTION: str = 'Mobile API Service - служит сервисом для мобильного сайта.'
VERSION: str = '1.0.0'


DATABASE_USERNAME: str = "user"
DATABASE_PASSWORD: str = "Dmitry_321011"
DATABASE_IP: str = "192.168.1.103"
DATABASE_NAME: str = "test_magazine"

SQLALCHEMY_DATABASE_URL: str = f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_IP}/{DATABASE_NAME}"
