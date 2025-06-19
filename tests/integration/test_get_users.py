from flask.testing import FlaskClient
from sqlalchemy.orm import Session

from api.application.outputs.user_output import UserOutput
from tests.helpers.user import create_fake_user


def test_get_users(client: FlaskClient, session: Session):
    user_1 = create_fake_user(session).to_user()

    response = client.get("/users")
    assert response.status_code == 200

    data = response.get_json()
    assert len(data) == 1
    user_output_1 = UserOutput.model_validate_json(data[0])
    assert user_output_1.email == user_1.email
