import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Sree Vidya Alivelu</title>" in html
        # TODO Add more tests relating to the home page
        assert '    <h5 class="title-left">\n      MLH Fellow - Production Engineering (June, 2022 - Present)\n    </h5>' in html
        assert '<iframe src="https://www.google.com/maps/d/embed?mid=1hutyxRuHGGheUAWBQe95sTdXGE3O00g&hl=en&ehbc=2E312F" width="1040" height="500">\n                            </iframe>' in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # TODO Add more tests relating to the /api/timeline_post GET and POST apis

        response = self.client.post("/api/timeline_post", data = {
            "name": "John Doe",
            "email": "john@example.com",
            "content": "Test"
        })
        assert response.status_code == 200

        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1
        assert json["timeline_posts"][0]["name"] == "John Doe"
        assert json["timeline_posts"][0]["content"] == "Test"
        assert json["timeline_posts"][0]["email"] == "john@example.com"

        # TODO Add more tests relating to the timeline page
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<th>Name</th>&nbsp;' in html
        assert '<input name="email" id="email" >' in html
        assert '<label>Name:</label>\n       <input name="name" id="name" >' in html


    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data=
        {"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        response = self.client.get("/timeline")
        html = response.get_data(as_text=True)
        assert "Invalid name" in html


        # POST request with empty content
        response = self.client.post("/api/timeline_post", data=
        {"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        response = self.client.get("/timeline")
        html = response.get_data(as_text=True)
        assert "Invalid content" in html


        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data=
        {"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        response = self.client.get("/timeline")
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
