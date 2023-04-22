# QRkot_spreadseetsОписание проекта QRKot:
    Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

Как запустить проект:

    Клонировать репозиторий и перейти в него в командной строке:

        git clone https://github.com/stas-zatushevskii/cat_charity_fund

    Cоздать и активировать виртуальное окружение:

        python / python3  -m venv env
        source env/bin/activate

    Установить зависимости из файла requirements.txt:

        python3 -m pip install --upgrade pip
        pip install -r requirements.txt

    Выполнить миграции:

        alembic revision --autogenerate -m "Name" -- создание миграции 
        alembic upgrade head  -- применение всех созданных миграций

    Запуск проекта:

        uvicorn main:app --reload

.env:

    APP_TITLE=Благотворительнный фонд поддержки котиков QRKot
    APP_DESC=Сервис предназначенный для благотворительного фонда поддержки котиков QRKot!
    DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
    SECRET=brunchik
    FIRST_SUPERUSER_EMAIL = s@s.ru
    FIRST_SUPERUSER_PASSWORD = 123
    TYPE = "service_account"
    PROJECT_ID = "flowing-depot-384114"
    PRIVATE_KEY_ID = "3e3ee0582b3666bdfbe716eaec62b487db04e945"
    PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDwqXfq/eXl+JZC\nzynuPijd5izli58QZBbwdXpwad40uZak1ptFW6smrHEFA23m3dBi939ZVTg5pi/h\nmHH1I/9/SpzhptjSBI3hje2DO7W4UHJ+svKX4BKSq7hcyIidEaGfVRLJeAEvu4HU\n6TonzSioIakl7nVuI/JfnBlxq24kTEOUBrf8vZkP3vSjn5C+AMqaIWDfOkUr4JP+\nITqPyy/4rqRVaybjEhCOQjRGydpn5Nn4xgXnDm1BJzx+2KilvDcSebaSpJ2Rufv2\new62EesZYd17GANBJzbSsc0Wbu3EXpGZbS5XZw7iLRZD3AIDlyIVdGA2U1j7eWxK\nXqfhCNQxAgMBAAECggEADrT8jBLKCty/KgQI9vM7ghv/4GNA7DqBoF49hkMh/izd\nROOMh5eLhQiCu6CzBanGg1XGpYnsrrE2Od4cELQLeBbyMWQF2gfHN+J5gkyS1Vmt\nNYrwAlICMI5n7NugZaDfNKJ5THCV+fnGfGFoWWhTNLsh4ByLdpihxi/+6hBk4bjd\nDNscjibk3pwsjYP6OeepNLqyYyKn/hPx/6ZXSJ4DgjtEHa59z6xbA/cYz/dX3tFV\nWl4tKZNVhjBXRuWspY92oWCKAzpdDElEGoNVEwnzhwFoQv2s/WbgfJbl63kHMRr6\npKTHwiNE/zMtvEzYznvvAL1IMdvfZkiL+p/jkxmJQQKBgQD8kCeSpYa9BTQwkbBe\nh4YdUr8hS22Llz8NtugvxUGtec8aPVw4yYhJWdhJ2OvpQpKIZjN3HXbW7TLIT8hv\nXgtlayf98K4UtkDxiyucSb1XpvqUsGs8zUbJZich5bdR6+0LFVDV1aUMEv3g4VnC\nTsUxavPqNziKNHmHfYK5cqh1eQKBgQDz79q1hw/NkEHc07TKKI1FQYJkiKzBtybb\nYbpbVUnmtOZrq93fMiMDt3FYPWfT/Ok5HDj4yGjrTunw8M7tMzqusxHXEtJm8Cmw\n4Zk8tODHzNrFWLWY78MovnZv+gFEI3mIEwJN9x0GS39usMYPrmF5OGLewKaFQl5q\nMMZQSyY+eQKBgQC0qemk3QMk8zQCCjU/aXJmR2qxRmN2FxrjlJNCmLgCf7/F5V6y\nwHbdAYfWS3V1xklLiNAHxOvdko9g+rFF+N/uDFjvLdtYtYZ/Qi5P/e+TY76b3hbX\nx397UbdsaAZac4l9BCJu1ATcPjmdQ5YRiIdGcltIj3fCZQcKBJ4eSgZ3AQKBgQCC\nvGYHLB+4GDx0UbJvNlSgbX+oyeds2vAkW7g5AvjcgM+NnUsIOCKz9zj0BdUDtGR6\nizmtfBtfIagXzbfZQL+OqcJB9oB1UvnFJuOtuXNPIeeOJQEOulFqIMnxMZhEII8d\n8rIlfu87VHMzq+I6vUbYZPP4Vl/ow60+VG200tHoYQKBgAuTEWlNFdona9Q5UTPH\n7A+ZQ2IlaMf/fBA8/5zgHlrpWVHFn+z6K2CdYULmcUrdym2bgffzsyhJGOX9Mw3d\nJDYN+cmfViB4bcQQyZ1WqIZkQaW4szpXpYWWqYJt5YsGhJMqcMpuyKeRoUO7Qfjc\nyHW/MldGzCqx5XfXB7rdVRKc\n-----END PRIVATE KEY-----\n"
    CLIENT_EMAIL = "practicum-account@flowing-depot-384114.iam.gserviceaccount.com"
    CLIENT_ID = "108707518303148931996"
    AUTH_URI = "https://accounts.google.com/o/oauth2/auth"
    TOKEN_URI = "https://oauth2.googleapis.com/token"
    AUTH_PROVIDER_X509_CERT_URL = "https://www.googleapis.com/oauth2/v1/certs"
    CLIENT_X509_CERT_URL = "https://www.googleapis.com/robot/v1/metadata/x509/practicum-account%40flowing-depot-384114.iam.gserviceaccount.com"
    EMAIL = "smartkalina583@gmail.com"
