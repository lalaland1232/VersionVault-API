import pytest
from unittest.mock import MagicMock,patch

from app.db.models import User
from app.signup.service import SignUpService
repo = MagicMock()
req=MagicMock()
db=MagicMock()
def test_signup():
    service=SignUpService(repo,db)
    repo.get_user_by_email_and_name.return_value=None
    