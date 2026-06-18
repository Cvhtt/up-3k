from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

TOPICS_DIR = "topics"

os.makedirs(TOPICS_DIR, exist_ok=True)

@app.route("/publish/<topic>", methods=["POST"])
def publish(topic):

    message = request.json

    filepath = os.path.join(
        TOPICS_DIR,
        f"{topic}.log"
    )

    with open(filepath, "a", encoding="utf-8") as f:

        f.write(
            json.dumps(message)
            + "\n"
        )

        f.flush()
        os.fsync(f.fileno())

    return jsonify({
        "status": "200 OK"
    })

@app.route("/messages/<topic>")
def messages(topic):

    offset = int(
        request.args.get("offset", 0)
    )

    limit = int(
        request.args.get("limit", 10)
    )

    filepath = os.path.join(
        TOPICS_DIR,
        f"{topic}.log"
    )

    if not os.path.exists(filepath):
        return jsonify([])

    with open(filepath, encoding="utf-8") as f:
        lines = f.readlines()

    result = []

    for line in lines[offset:offset + limit]:
        result.append(json.loads(line))

    return jsonify(result)

@app.route("/status")
def status():

    topics = os.listdir(TOPICS_DIR)

    return jsonify({
        "topics": topics
    })

if __name__ == "__main__":
    app.run(port=5000)