from rest.rest_client import RestClient


class Users(RestClient):
    """
    Notes API service
    """
    BASE_URL = "https://practice.expandtesting.com/notes/api/"
    _token: str | None = None

    @property
    def _headers(self):
        return {"x-auth-token": self._token}

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

    def user_register(self):
        """
        Send a POS request to /users/register
        :return: response in JSON format
        """
        self._log.info("User registration")
        response = self._get("users/register")
        return response

    def post_users_registration(self, email=None, password=None, expected_status_code=201):
        """
        Send a POST request to /users/login
        :param email: email
        :param password: password
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        response = self._post("users/register",
                              data={"name": "Jeka", "email": email, "password": password},
                              expected_status_code=expected_status_code)
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

    def patch_user_profile(self, updated_data, header ):
        self._log.info(f"User profile was updated")
        response = self._patch(path="/users/profile", data=updated_data, headers=header)
        return response
