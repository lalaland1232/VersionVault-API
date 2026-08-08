import pytest
from unittest.mock import patch,MagicMock

from app.login.service import LoginService

repo=MagicMock()
db=MagicMock()
request=MagicMock()
def test_login():
    service = LoginService(repo,db)
    repo.get_user_by_email.return_value = MagicMock(id=1)
    repo.get_hashed_password.return_value = MagicMock(artifact=b'$2b$12')
    with patch("app.login.service.bcrypt.checkpw",
                side_effect=Exception("Invalid password")):
        with pytest.raises(Exception) as e:
            service.login(request)
               