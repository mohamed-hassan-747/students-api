from flask import Flask, jsonify, request

app = Flask(__name__)


students = [
    {"id": 1, "name": "Ahmed", "age": "19"},
    {"id": 2, "name": "Mohammed", "age": "20"},
    {"id": 3, "name": "Mahmoud", "age": "21"},
    {"id": 4, "name": "Omar", "age": "20"},
    {"id": 5, "name": "Khaled", "age": "23"}
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s["id"] == id), None)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    if not new_student:
        return jsonify({"error": "Request body is empty"}), 400
    
    if "name" not in new_student or "age" not in new_student:
        return jsonify({"error": "Missing required field"}), 400
    
    new_student['id'] = students[-1]['id'] + 1 if students else 1
    students.append(new_student)
    return jsonify(new_student), 201

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s["id"] == id), None)
    if student:
        new_info = request.get_json()
        student.update(new_info)
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    student = next((s for s in students if s["id"] == id), None)
    if student:
        students = [s for s in students if s["id"] != id]
        return jsonify({"message": "Student deleted"}), 200  
    return jsonify({"error": "Student not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)

