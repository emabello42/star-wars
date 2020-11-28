import sqlalchemy
import sqlalchemy_utils
import uuid
import pandas as pd

from starwars.repository.postgres_objects import Base, Starship as pgStarship

setup = {
    'dbname': "starwarsdb",
    'user': "postgres",
    'password': "",
    'host': "localhost"
}

conn_str = "postgresql+psycopg2://{}:{}@{}/{}".format(
    setup['user'],
    setup['password'],
    setup['host'],
    setup['dbname']
)

engine = sqlalchemy.create_engine(conn_str)
if not sqlalchemy_utils.database_exists(engine.url):
    sqlalchemy_utils.create_database(engine.url)

conn = engine.connect()

Base.metadata.create_all(engine)

# create initial data
df = pd.read_csv("starships.csv")
DBSession = sqlalchemy.orm.sessionmaker(bind=engine)
session = DBSession()

for idx, row in df.iterrows():
    new_starship = pgStarship(
        code=uuid.uuid4(),
        name=row['name'],
        hyperdrive_rating=row['hyperdrive_rating']
    )
    session.add(new_starship)
    session.commit()
