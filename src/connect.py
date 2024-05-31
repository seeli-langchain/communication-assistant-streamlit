from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///data.db', echo=True)

with engine.connect() as connection:
    result = connection.execute(text('select "Hallo" '))

    print (result.all())