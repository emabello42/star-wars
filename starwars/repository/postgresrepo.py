from starwars.repository.postgres_objects import Base, Starship as pgStarship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starwars.domain import starship as domain


class PostgresRepo:
    def __init__(self, connection_data):
        connection_string = "postgresql+psycopg2://{}:{}@{}/{}".format(
            connection_data['user'],
            connection_data['password'],
            connection_data['host'],
            connection_data['dbname']
        )
        self.engine = create_engine(connection_string)
        Base.metadata.bind = self.engine

    def __create_starship_objects(self, results):
        starships = []
        for q in results:
            starships.append(domain.Starship(code=q.code, name=q.name, hyperdrive_rating=q.hyperdrive_rating))
        return starships

    def list_starships(self, params=None):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(pgStarship)
        if params is None:
            return self.__create_starship_objects(query.all())
        if 'orderby_hyperdrive_desc' in params:
            query = query.order_by(pgStarship.hyperdrive_rating.desc())
        elif 'orderby_hyperdrive_asc' in params:
            query = query.order_by(pgStarship.hyperdrive_rating.asc())
        return self.__create_starship_objects(query.all())
