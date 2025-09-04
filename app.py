import sys
import os

# Add the current directory to the Python path
# Handle case where __file__ might be None in some environments
if __file__ is not None:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
else:
    sys.path.append(os.getcwd())

from main import HealthWellnessAgent
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Global agent instance
agent = HealthWellnessAgent()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/greet')
def greet():
    return jsonify({"message": agent.greet_user()})

@app.route('/api/profile', methods=['POST'])
def set_profile():
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    
    name = data.get('name')
    age = data.get('age')
    height = data.get('height')
    weight = data.get('weight')
    fitness_level = data.get('fitness_level', 'beginner')
    
    result = agent.set_user_profile(name, age, height, weight, fitness_level)
    return jsonify({"message": result})

@app.route('/api/metrics', methods=['POST'])
def update_metrics():
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    
    result = agent.update_metrics(
        water_intake=data.get('water_intake'),
        steps=data.get('steps'),
        sleep_hours=data.get('sleep_hours'),
        mood=data.get('mood'),
        energy_level=data.get('energy_level')
    )
    return jsonify({"message": result})

@app.route('/api/tip')
def daily_tip():
    return jsonify({"tip": agent.get_daily_tip()})

@app.route('/api/exercise')
def exercise():
    level = request.args.get('level')
    return jsonify({"exercise": agent.suggest_exercise(level)})

@app.route('/api/mindfulness')
def mindfulness():
    return jsonify({"mindfulness": agent.suggest_mindfulness()})

@app.route('/api/nutrition')
def nutrition():
    return jsonify({"nutrition": agent.get_nutrition_advice()})

@app.route('/api/summary')
def summary():
    return jsonify({"summary": agent.get_health_summary()})

@app.route('/api/recommendation')
def recommendation():
    return jsonify({"recommendation": agent.get_recommendation()})

if __name__ == '__main__':
    print("Starting Health & Wellness Agent Web Application...")
    print("Visit http://127.0.0.1:5000 in your browser")
    app.run(debug=True, host='127.0.0.1', port=5000)

