
def get_access_token(client, username, password):
    response = client.post("/api/token/", {
        "username": username,
        "password": password
    }, format="json")
    return response.data["access"]


def create_new_task(client, title="test", description="testtask"):
    response = client.post("/tasks/", {
        "title": title,
        "description": description
    }, format="json")

    if response.status_code == 401:
        return {"error": "the provided client was not authenticated!"}

    return response.data