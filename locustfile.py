from locust import HttpUser, TaskSet, task, between

class SimpleTasks(TaskSet):
    @task(1)
    def home(self):
        # Test the home route
        self.client.get("/", name="Simple User - /")

    @task(2)
    def fast(self):
        # Test the fast route
        self.client.get("/fast", name="Simple User - /fast")

    @task(3)
    def medium(self):
        # Test the medium route
        self.client.get("/medium", name="Simple User - /medium")

    @task(4)
    def heavy(self):
        # Test the heavy route
        self.client.get("/heavy", name="Simple User - /heavy")

    @task(1)
    def echo(self):
        # Test the echo route
        payload = {"message": "Hello, Locust!"}
        self.client.post("/echo", json=payload, name="Simple User - /echo")

class HeavyTasks(TaskSet):
    @task(1)
    def home(self):
        # Test the home route
        self.client.get("/", name="Heavy User - /")

    @task(2)
    def fast(self):
        # Test the fast route
        self.client.get("/fast", name="Heavy User - /fast")

    @task(3)
    def medium(self):
        # Test the medium route
        self.client.get("/medium", name="Heavy User - /medium")

    @task(4)
    def heavy(self):
        # Test the heavy route
        self.client.get("/heavy", name="Heavy User - /heavy")

    @task(1)
    def echo(self):
        # Test the echo route
        payload = {"message": "Hello, Locust!"}
        self.client.post("/echo", json=payload, name="Heavy User - /echo")


class SimpleUser(HttpUser):
    tasks = [SimpleTasks]
    wait_time = between(1, 5)  # Simulate a wait time between requests
    weight = 1

class HeavyUser(HttpUser):
    tasks = [HeavyTasks]
    wait_time = between(10, 15)  # Simulate a wait time between requests
    weight = 49
