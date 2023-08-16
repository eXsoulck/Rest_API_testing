import os
from logging import getLogger

import pytest

from rest.countries_rest import CountriesRest
from rest.notes_rest import NotesRest
from rest.user_client import Users
logger = getLogger(__name__)


@pytest.fixture
def email():
    return os.getenv("EMAIL")


@pytest.fixture
def password():
    return os.getenv("PASSWORD")


@pytest.fixture
def notes_service():
    return NotesRest()



@pytest.fixture
def authenticated_notes_service(notes_service, email, password):
    notes_service.post_users_login(email, password=password)
    yield notes_service
    notes_service._token = None




@pytest.fixture
def prepared_note(authenticated_notes_service) -> dict:
    logger.info("Preparing note for tests")
    response = authenticated_notes_service.post_notes(
        title="Test Title",
        description="Test Description",
        category="Home",
        expected_status_code=200
    )
    logger.info(f"Note prepared: {response['data']}")
    return response["data"]


@pytest.fixture
def countries_service():
    return CountriesRest()

@pytest.fixture
def user_service():
    return Users()

