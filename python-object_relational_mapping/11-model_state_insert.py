#!/usr/bin/python3
"""Script that adds the State object Louisiana to the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    )

    Session = sessionmaker(engine)
    session = Session()

    state = State(name='Louisiana')

    session.add(state)
    session.commit()

    print(state.id)

    session.close()
