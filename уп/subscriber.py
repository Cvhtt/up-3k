from sdk import Subscriber
from queue_manager import QueueManager

subscriber = Subscriber()

qm = QueueManager()

GROUP = "group1"
TOPIC = "news"

offset = qm.claim_messages(
    GROUP,
    TOPIC,
    5
)

messages = subscriber.receive(
    TOPIC,
    offset,
    5
)

print(
    f"Получено {len(messages)} сообщений"
)

for msg in messages:
    print(msg)