import os
import random
import string

from rest.rest_client import RestClient


class NotesRest(RestClient):
    """
    Notes API service
    """
    BASE_URL = "https://practice.expandtesting.com/notes/api/"
    _token: str | None = None

    @property
    def _headers(self):
        return {"x-auth-token": self._token}

    def get_health_check(self):
        """
        Send a GET request to /health-check
        :return: response in JSON format
        """
        self._log.info("Checking health")
        response = self._get("health-check")
        return response

    def post_users_login(self, email=None, password=None, expected_status_code=200):
        """
        Send a POST request to /users/login
        :param email: email
        :param password: password
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Logging in as {email}")
        response = self._post("users/login",
                              json={"email": email, "password": password},
                              expected_status_code=expected_status_code)
        if response["status"] == 200:
            self._token = response["data"]["token"]
        return response

    def delete_users_logout(self, expected_status_code=200):
        """
        Send a DELETE request to /users/logout
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info("Logging out")
        response = self._delete("users/logout", expected_status_code=expected_status_code)
        if response["status"] == 200:
            self._token = None
        return response

    def get_users_profile(self, expected_status_code=200):
        """
        Send a GET request to /users/profile
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info("Getting user profile")
        response = self._get("users/profile", expected_status_code=expected_status_code)
        return response

    def post_notes(self, title=None, description=None, category=None, expected_status_code=200):
        """
        Send a POST request to /notes
        :param title: title of the note
        :param description: description of the note
        :param category: category of the note (Home, Work, Personal)
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Creating note with title: {title}")
        response = self._post("notes",
                              data={"title": title, "description": description, "category": category},
                              expected_status_code=expected_status_code)
        return response

    def delete_note_by_id(self, note_id=None, expected_status_code=200):
        """
        Send a DELETE request to /notes/{note_id}
        :param note_id: id of the note
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Deleting note with id: {note_id}")
        response = self._delete(f"notes/{note_id}", expected_status_code=expected_status_code)
        return response

    def patch_user_profile(self, updated_data, expected_status_code=200):
        self._log.info(f"User profile was updated")
        response = self._patch(path="users/profile", data=updated_data, header=self._headers,
                               expected_status_code=expected_status_code)
        return response

    def password_reset(self, user_email, expected_status_code=200):
        self._log.info(f"Password reset link successfully sent to {user_email}")
        response = self._post(path="users/forgot-password", data=user_email, expected_status_code=expected_status_code)
        return response

    def change_password(self, email):
        self._log.info(f"Password for {email} has been changed")
        letters = string.ascii_letters
        new = ''.join(random.choice(letters) for i in range(10))
        with open("/home/exsoul/PycharmProjects/REST_API_Testing/.env", 'r') as f:
            data = f.readlines()
        data[1] = "PASSWORD=" + new

        with open("/home/exsoul/PycharmProjects/REST_API_Testing/.env", "w") as f:
            f.writelines(data)

        new_password = {
            "currentPassword": os.getenv("PASSWORD"),
            "newPassword": new
        }
        os.environ["PASSWORD"] = new
        response = self._post(path="users/change-password", data=new_password, headers=self._headers)

        return response


    def delete_user_account(self, email):
        self._log.info(f"Account {email} has been deleted")
        response = self._delete(path="users/delete-account", headers=self._headers)
        return response

    def get_all_notes(self):
        self._log.info(f"Retrieve a list of notes")
        response = self._get(path="notes", headers=self._headers)
        return response

    def get_note_by_id(self, note_id=None, expected_status_code=200):
        self._log.info(f"Retrieve note by {note_id}")
        response = self._get(path=f"notes/{note_id}", expected_status_code=expected_status_code)
        return response

    def put_note(self, note_id=None):
        self._log.info(f"Update a note with id={note_id}")
        data = {
            "id": note_id,
            "title": "Some new test",
            "description": "Additional information",
            "completed": "false",
            "category": "Home"
        }
        response = self._put(path=f"notes/{note_id}", data=data, header=self._headers)
        return response

    def update_complete_attribute(self, note_id=None):
        self._log.info(f"Update the completed attribute of the note with the id={note_id}")
        data = {
            "id": note_id,
            "completed": "true"
        }
        response = self._patch(path=f"notes/{note_id}", data=data, header=self._headers)
        return response
