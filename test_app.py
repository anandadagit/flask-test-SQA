from app import app

def test_home_route():
    # Create a test client for our Flask app
    client = app.test_client()

    # Perform a GET request on the home route
    response = client.get("/")

    # Assert a successful (200 OK) status code
    assert response.status_code == 200

    # Assert the body text matches expected result
    assert response.data == b"Flask is running!"