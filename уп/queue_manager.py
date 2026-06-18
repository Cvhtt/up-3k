import json
import threading
import os

class QueueManager:

    def __init__(self):

        self.lock = threading.Lock()

        if os.path.exists("offsets.json"):

            with open(
                "offsets.json",
                "r",
                encoding="utf-8"
            ) as f:

                self.offsets = json.load(f)

        else:
            self.offsets = {}

    def save(self):

        with open(
            "offsets.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.offsets,
                f,
                indent=4
            )

    def get_offset(
        self,
        group,
        topic
    ):

        return (
            self.offsets
            .get(group, {})
            .get(topic, 0)
        )

    def ack(
        self,
        group,
        topic,
        offset
    ):

        with self.lock:

            if group not in self.offsets:
                self.offsets[group] = {}

            self.offsets[group][topic] = offset

            self.save()

    def claim_messages(
        self,
        group,
        topic,
        count
    ):

        with self.lock:

            current = self.get_offset(
                group,
                topic
            )

            self.ack(
                group,
                topic,
                current + count
            )

            return current

    def status(self):

        return self.offsets