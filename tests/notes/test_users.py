import pytest


@pytest.mark.xfail(reason="registration with same credentials is not possible")
def test_user_registrations(user_service, email, password):
    response = user_service.post_users_registration(email, password)
    assert response["message"] == "User account created successfully"


def test_login(notes_service, email, password):
    response = notes_service.post_users_login(email, password)
    assert response["data"]["token"] is not None


def test_login_invalid_email(notes_service, password):
    response = notes_service.post_users_login("invalid@email.com", password, expected_status_code=401)
    assert response["message"] == "Incorrect email address or password"


def test_profile_unauthenticated(notes_service):
    response = notes_service.get_users_profile(expected_status_code=401)
    assert response["message"] == "No authentication token specified in x-auth-token header"


def test_profile(authenticated_notes_service, email):
    response = authenticated_notes_service.get_users_profile()

    assert response["message"] == "Profile successful"
    assert response["data"]["email"] == email, "Email address is not correct"


@pytest.mark.negative_test
def test_registration_with_short_pass(user_service, email):
    response = user_service.post_users_registration(email, password="12345", expected_status_code=400)
    assert response["message"] == "Password must be between 6 and 30 characters"


def test_profile_update(notes_service, email, password):
    response = notes_service.post_users_login(email, password)
    data = {
        "name": "New_test_name",
        "phone": "",
        "company": ""
    }
    updated_info = notes_service.patch_user_profile(updated_data=data)
    assert updated_info.json()["data"]["name"] == data["name"]


def test_user_forgot_password(notes_service, email):
    user_email = {
        "email": email
    }
    response = notes_service.password_reset(user_email=user_email)
    assert response["message"] == f"Password reset link successfully sent to {email}." \
                                  f" Please verify by clicking on the given link"


def test_verify_password_for_reset(authenticated_notes_service, email):
    response = authenticated_notes_service.change_password(email)
    assert response["message"] == "The password was successfully updated"


def test_delete_user_acc(authenticated_notes_service, email):
    response = authenticated_notes_service.delete_user_account(email)
    assert response["message"] == "Account successfully deleted"

