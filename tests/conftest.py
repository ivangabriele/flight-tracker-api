from flask import Flask
import pytest
from sqlalchemy.orm import scoped_session, sessionmaker

from api import create_app
from api.adapters import database as db


@pytest.fixture(scope="session")
def app():
    app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
    )

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture(scope="function")
def client(app: Flask):
    return app.test_client()


@pytest.fixture(scope="function", autouse=True)
def session():
    connection = db.engine.connect()
    txn = connection.begin()
    SessionFactory = sessionmaker(bind=connection)
    scoped = scoped_session(SessionFactory)

    # swap Flask-SQLAlchemy’s session for the duration
    old_session = db.session
    db.session = scoped  # type: ignore[assignment]

    try:
        yield scoped
    finally:
        scoped.remove()
        txn.rollback()
        connection.close()
        db.session = old_session


@pytest.fixture(autouse=True)
def reset_faker():
    from tests.helpers.faker import faker

    faker.unique.clear()
