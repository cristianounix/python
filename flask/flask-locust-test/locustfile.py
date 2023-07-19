import time
from locust import HttpUser, task, between

#locust -f locustfile.py --host=http://127.0.0.1:5000

class MyWebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def load_main(self):
        self.client.get("/")

    @task
    def view_numbers_two_and_three(self):
        self.client.get("/?number=2")
        self.client.get("/?number=3")

    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(
                f"/item?id={item_id}", 
                name="/item"
            )
            time.sleep(1)

    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})