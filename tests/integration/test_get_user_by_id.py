from flask.testing import FlaskClient
from sqlalchemy.orm import Session

from api.application.outputs.user_output import UserOutput
from tests.helpers.user import create_fake_user


def test_get_user_by_id(client: FlaskClient, session: Session):
    user = create_fake_user(session).to_user()

    response = client.get(f"/users/{user.id}")
    assert response.status_code == 200

    data = response.get_json()
    user_output = UserOutput.model_validate_json(data)
    assert user_output.email == user.email
