from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, String, Integer, ForeignKey


engine = create_engine("sqlite:///")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True)


class Address(BaseModel):
    __tablename__ = "addresses"

    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)

    user_id = Column(ForeignKey("users.id"))

    user = relationship("User", back_populates="addresses")


    def __repr__(self):
        return f"Address(id={self.id}, city={self.city}, user_id={self.user_id}, user={self.user})"


class User(BaseModel):
    __tablename__ = "users"

    name = Column(String)
    age = Column(Integer)

    addresses = relationship(Address, back_populates="user")


    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, address={self.addresses})"


Base.metadata.create_all(bind=engine)