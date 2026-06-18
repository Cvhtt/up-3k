from sdk import Publisher

publisher = Publisher()

for i in range(10):

    publisher.send(
        "news",
        {
            "id": i,
            "text": f"Сообщение {i}"
        }
    )

print("Отправлено")