from flask import Flask, request, jsonify

app = Flask(__name__)
notes = []


@app.route("/notes", methods=["POST"])
def create_note():
    data = request.json
    note = {"id": len(notes) + 1, "text": data["text"]}
    notes.append(note)
    return jsonify(note), 201


@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes), 200


@app.route("/notes/<int:note_id>", methods=["GET"])
def get_note(note_id):
    note = next((n for n in notes if n["id"] == note_id), None)
    if note:
        return jsonify(note), 200
    return jsonify({"error": "Note not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
