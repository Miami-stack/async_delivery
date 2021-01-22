from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        self.client.post("/creategoods", json={
            "identificator": "test",
            "status": "performed"
        })

    @task
    def index(self):
        self.client.get("/checkstatus")


    @task
    def about(self):
        self.client.get("/heartbeat")
