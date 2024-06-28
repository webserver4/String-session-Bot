import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', True)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', "23080322"))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', "b3611c291bf82d917637d61e4a136535")
    BOT_TOKEN = os.environ.get('BOT_TOKEN', "6616252751:AAEHX0kpIqUr-vvqDWzR-oq0tdgwzQC4Y0s")
    DATABASE_URL = os.environ.get('DATABASE_URL', "postgresql://postgres.adldmnbzdckqwrckabtj:Aaryanary1097@aws-0-ap-south-1.pooler.supabase.com:6543/postgres")
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', "leechbot449")
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 0
    API_HASH = ""
    BOT_TOKEN = ""
    DATABASE_URL = ""
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
