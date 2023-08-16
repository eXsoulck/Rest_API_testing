import pytest


@pytest.mark.parametrize("category", ["Home", "Work", "Personal"])
def test_create_note(authenticated_notes_service, category):
    title = "Test note"
    description = "Test Description"

    response = authenticated_notes_service.post_notes(title, description, category)

    assert response["message"] == "Note successfully created"
    assert response["data"]["title"] == title
    assert response["data"]["description"] == description
    assert response["data"]["category"] == category
    assert response["data"]["id"] is not None


def test_create_note_invalid_category(authenticated_notes_service):
    title = "Test note"
    description = "Test Description"
    category = "Invalid"

    response = authenticated_notes_service.post_notes(title, description, category, expected_status_code=400)

    assert response["message"] == "Category must be one of the categories: Home, Work, Personal"


def test_delete_note_by_id(authenticated_notes_service, prepared_note):
    response = authenticated_notes_service.delete_note_by_id(prepared_note["id"])
    assert response["message"] == "Note successfully deleted"


def test_get_all_notes(authenticated_notes_service):
    response = authenticated_notes_service.get_all_notes()
    assert len(response["data"])


def test_get_note_by_id(authenticated_notes_service, prepared_note):
    response = authenticated_notes_service.get_note_by_id(prepared_note["id"])
    assert response["message"] == "Note successfully retrieved"


def test_put_note(authenticated_notes_service, prepared_note):
    note_id = prepared_note["id"]
    response = authenticated_notes_service.put_note(note_id)
    assert response.json()["message"] == "Note successfully Updated"


def test_update_complete_attribute(authenticated_notes_service, prepared_note):
    note_id = prepared_note["id"]
    response = authenticated_notes_service.update_complete_attribute(note_id)
    assert response.json()["message"] == "Note successfully Updated"


@pytest.mark.negative_test
def test_create_note_missing_title(authenticated_notes_service):
    title = ""
    description = "Test Description"
    category = "Work"
    response = authenticated_notes_service.post_notes(title, description, category, expected_status_code=400)
    assert response["message"] == "Title must be between 4 and 100 characters"

@pytest.mark.negative_test
def test_create_note_missing_description(authenticated_notes_service):
    title = "Test missing description"
    description = ""
    category = "Work"
    response = authenticated_notes_service.post_notes(title, description, category, expected_status_code=400)
    assert response["message"] == "Description must be between 4 and 1000 characters"
