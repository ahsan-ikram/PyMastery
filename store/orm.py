"""
Relational database CRUD operations using SQL
Using ORM library like SQLAlchemy
Recommended for serious applications

Reference: https://www.tutorialspoint.com/sqlalchemy/index.htm
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    manufacturer = Column(String)
    expiry = Column(String)

    def __str__(self):
        return f'id = {self.id} ' \
               f'name = {self.name} ' \
               f'manufacturer = {self.manufacturer} ' \
               f'expiry={self.expiry}'


def create(engine):
    Base.metadata.create_all(engine)


def read(engine):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        query = session.query(Product).all()
        filter_query = session.query(Product).filter(Product.id > 10)

    for row in query:
        print(row)

    for row in filter_query:
        print(row)


def update(engine):
    Session = sessionmaker(bind=engine)
    product = Product(name='Safety knife', manufacturer='xyz GmbH', expiry='NA')

    with Session() as session:
        session.add(product)
        session.add_all([
            Product(name='Hula hup', manufacturer='abc GmbH', expiry='NA'),
            Product(name='Moto G', manufacturer='Lenevo China', expiry='NA'),
            Product(name='iphone 6', manufacturer='Apple, Pune', expiry='NA')]
        )
        session.commit()


def delete():
    pass


def main():
    engine = create_engine('sqlite:///:memory:', echo=True)
    create(engine)
    read(engine)
    update(engine)


if __name__ == '__main__':
    main()
