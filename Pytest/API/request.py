import json
from Pytest.Default import default_DB
from Pytest import client
from jsonschema import validate


def print_response(response_json, response_status_code):
    print("response:", response_json)
    print("response status_code:", response_status_code)


class Request():
    def get(self, url, validate_status_code, validate_response=None, validate_schema=None, **kwargs):
        response = client.get(url, **kwargs)
        print_response(response.json(), response.status_code)
        assert response.status_code == validate_status_code

        if validate_response:
            assert response.json() == validate_response

        if validate_schema:
            if isinstance(response.json(), list):
                for each_response in response.json():
                    assert validate(instance=each_response, schema=validate_schema) is None
            else:
                assert validate(instance=response.json(), schema=validate_schema) is None


    def post(self, url, validate_status_code, validate_response=None, validate_schema=None, **kwargs):
        response = client.post(url, **kwargs)
        print_response(response.json(), response.status_code)
        assert response.status_code == validate_status_code

        if validate_response:
            assert response.json() == validate_response

        if validate_schema:
            if isinstance(response.json(), list):
                for each_response in response.json():
                    assert validate(instance=each_response, schema=validate_schema) is None
            else:
                assert validate(instance=response.json(), schema=validate_schema) is None


    def patch(self, url, validate_status_code, validate_response=None, validate_schema=None, **kwargs):
        response = client.patch(url, **kwargs)
        print_response(response.json(), response.status_code)
        assert response.status_code == validate_status_code

        if validate_response:
            assert response.json() == validate_response

        if validate_schema:
            if isinstance(response.json(), list):
                for each_response in response.json():
                    assert validate(instance=each_response, schema=validate_schema) is None
            else:
                assert validate(instance=response.json(), schema=validate_schema) is None


    def delete(self, url, validate_status_code, validate_response=None, validate_schema=None, **kwargs):
        response = client.delete(url, **kwargs)
        print_response(response.json(), response.status_code)
        assert response.status_code == validate_status_code

        if validate_response:
            assert response.json() == validate_response

        if validate_schema:
            if isinstance(response.json(), list):
                for each_response in response.json():
                    assert validate(instance=each_response, schema=validate_schema) is None
            else:
                assert validate(instance=response.json(), schema=validate_schema) is None