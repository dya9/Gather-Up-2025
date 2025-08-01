from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for simplicity (use a database in production)
availability_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/api/save-availability', methods=['POST'])
def save_availability():
    data = request.json
    availability_data.append(data)
    # Here you can process the data to find the most popular hours
    return jsonify({"status": "success"})

@app.route('/popular-hours')
def popular_hours():
    # Process availability_data to find the most popular hours
    # This is a placeholder; implement your logic here
    popular_hours = {"Monday": "9:00 AM", "Tuesday": "10:00 AM"}  # Example data
    return render_template('popular_hours.html', popular_hours=popular_hours)

if __name__ == '__main__':
    app.run(debug=True)