from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Route for serving the calculator interface
@app.route('/')
def home():
    return render_template('index.html')

# Route for performing calculations (already created)
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        num1 = float(data.get("num1"))
        num2 = float(data.get("num2"))
        operation = data.get("operation")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return jsonify({"error": "Division by zero is not allowed."}), 400
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operation. Use +, -, *, or /"}), 400

        return jsonify({"num1": num1, "num2": num2, "operation": operation, "result": result})

    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Please provide valid numbers."}), 400

if __name__ == '__main__':
    app.run(debug=True)


