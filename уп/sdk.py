import requests

class Publisher:

    def send(
        self,
        topic,
        message
    ):

        requests.post(
            f"http://localhost:5000/publish/{topic}",
            json=message
        )

class Subscriber:

    def receive(
        self,
        topic,
        offset,
        limit
    ):

        response = requests.get(

            f"http://localhost:5000/messages/{topic}",

            params={
                "offset": offset,
                "limit": limit
            }
        )

        return response.json()