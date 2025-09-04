import json
import random
from datetime import datetime
from typing import Dict, List, Optional

class HealthWellnessAgent:
    """AI Agent for Health and Wellness Management"""
    
    def __init__(self):
        self.user_data = {}
        self.wellness_tips = [
            "Stay hydrated! Aim for 8 glasses of water per day.",
            "Take short breaks every hour if you sit for long periods.",
            "Try deep breathing exercises when feeling stressed.",
            "Aim for 7-9 hours of quality sleep each night.",
            "Include a variety of colorful fruits and vegetables in your diet.",
            "Regular physical activity can boost your mood and energy levels.",
            "Practice gratitude by noting three things you're thankful for each day.",
            "Limit processed foods and added sugars for better energy.",
            "Spend time outdoors to get natural sunlight and fresh air.",
            "Maintain social connections for better mental health."
        ]
        self.exercise_routines = {
            "beginner": [
                "5-minute walk",
                "10-minute stretching session",
                "Basic yoga poses for 10 minutes",
                "Light bodyweight exercises (10 squats, 5 push-ups)"
            ],
            "intermediate": [
                "20-minute brisk walk or jog",
                "15-minute yoga or Pilates routine",
                "Bodyweight circuit (20 squats, 10 push-ups, 30-second plank)",
                "Dance for 15 minutes to your favorite music"
            ],
            "advanced": [
                "30-minute run or cycling session",
                "20-minute HIIT workout",
                "Advanced yoga or strength training routine",
                "Sports activity or martial arts practice"
            ]
        }
        self.mindfulness_exercises = [
            "Try a 5-minute meditation focusing on your breath",
            "Practice progressive muscle relaxation",
            "Do a body scan meditation before sleep",
            "Listen to calming music for 10 minutes",
            "Write in a journal for 10 minutes about your day",
            "Practice mindful eating during your next meal"
        ]
    
    def greet_user(self) -> str:
        """Greet the user and provide an overview of the agent's capabilities"""
        greeting = """
        🌿 Welcome to your Health & Wellness AI Assistant! 🌿
        
        I'm here to help you maintain and improve your health and wellness.
        I can help you with:
        - Tracking your wellness metrics
        - Providing personalized health tips
        - Suggesting exercise routines
        - Offering mindfulness and stress management techniques
        - Providing nutrition guidance
        
        Let's get started on your wellness journey!
        """
        return greeting.strip()
    
    def set_user_profile(self, name: str, age: int, height: float, weight: float, 
                        fitness_level: str = "beginner", health_conditions: Optional[List[str]] = None) -> str:
        """Set up user profile with basic information"""
        self.user_data = {
            "name": name,
            "age": age,
            "height": height,  # in cm
            "weight": weight,  # in kg
            "fitness_level": fitness_level.lower(),
            "health_conditions": health_conditions or [],
            "metrics": {
                "water_intake": 0,
                "steps": 0,
                "sleep_hours": 0,
                "mood": "",
                "energy_level": 0  # 1-10 scale
            },
            "last_updated": datetime.now().isoformat()
        }
        
        # Calculate BMI
        height_m = height / 100  # convert to meters
        bmi = weight / (height_m ** 2)
        self.user_data["bmi"] = round(bmi, 1)
        
        return f"Profile created for {name}! Your BMI is {self.user_data['bmi']}."
    
    def update_metrics(self, water_intake: Optional[int] = None, steps: Optional[int] = None, 
                      sleep_hours: Optional[float] = None, mood: Optional[str] = None, 
                      energy_level: Optional[int] = None) -> str:
        """Update daily wellness metrics"""
        if "metrics" not in self.user_data:
            return "Please set up your profile first using set_user_profile()."
        
        metrics_updated = []
        if water_intake is not None:
            self.user_data["metrics"]["water_intake"] = water_intake
            metrics_updated.append("water intake")
        
        if steps is not None:
            self.user_data["metrics"]["steps"] = steps
            metrics_updated.append("steps")
        
        if sleep_hours is not None:
            self.user_data["metrics"]["sleep_hours"] = sleep_hours
            metrics_updated.append("sleep hours")
        
        if mood is not None:
            self.user_data["metrics"]["mood"] = mood
            metrics_updated.append("mood")
        
        if energy_level is not None:
            self.user_data["metrics"]["energy_level"] = energy_level
            metrics_updated.append("energy level")
        
        self.user_data["last_updated"] = datetime.now().isoformat()
        
        if metrics_updated:
            return f"Updated metrics: {', '.join(metrics_updated)}"
        else:
            return "No metrics were updated."
    
    def get_daily_tip(self) -> str:
        """Provide a random wellness tip"""
        tip = random.choice(self.wellness_tips)
        return f"💡 Wellness Tip: {tip}"
    
    def suggest_exercise(self, level: Optional[str] = None) -> str:
        """Suggest an exercise routine based on fitness level"""
        if not level:
            level = self.user_data.get("fitness_level", "beginner")
        
        if level not in self.exercise_routines:
            level = "beginner"
        
        exercise = random.choice(self.exercise_routines[level])
        return f"💪 Exercise Suggestion ({level} level): {exercise}"
    
    def suggest_mindfulness(self) -> str:
        """Suggest a mindfulness exercise"""
        exercise = random.choice(self.mindfulness_exercises)
        return f"🧘 Mindfulness Exercise: {exercise}"
    
    def get_nutrition_advice(self) -> str:
        """Provide personalized nutrition advice"""
        if not self.user_data:
            return "Please set up your profile first for personalized advice."
        
        bmi = self.user_data.get("bmi", 0)
        
        if bmi < 18.5:
            advice = "Consider nutrient-dense foods to maintain a healthy weight. Include nuts, avocados, and whole grains."
        elif 18.5 <= bmi < 25:
            advice = "Maintain your balanced diet with a variety of fruits, vegetables, lean proteins, and whole grains."
        elif 25 <= bmi < 30:
            advice = "Focus on portion control and include more fiber-rich foods and lean proteins in your diet."
        else:
            advice = "Consider consulting a nutritionist for a personalized plan focusing on whole foods and portion control."
        
        return f"🥗 Nutrition Advice: {advice}"
    
    def get_health_summary(self) -> str:
        """Provide a summary of user's health data"""
        if not self.user_data:
            return "No profile data available. Please set up your profile first."
        
        name = self.user_data.get("name", "User")
        bmi = self.user_data.get("bmi", "N/A")
        metrics = self.user_data.get("metrics", {})
        
        summary = f"""
        📊 Health Summary for {name}:
        
        BMI: {bmi}
        
        Today's Metrics:
        - Water Intake: {metrics.get('water_intake', 0)} glasses
        - Steps: {metrics.get('steps', 0)}
        - Sleep: {metrics.get('sleep_hours', 0)} hours
        - Mood: {metrics.get('mood', 'Not recorded')}
        - Energy Level: {metrics.get('energy_level', 0)}/10
        """
        
        return summary.strip()
    
    def get_recommendation(self) -> str:
        """Provide a personalized wellness recommendation based on user data"""
        if not self.user_data:
            return "Please set up your profile first for personalized recommendations."
        
        metrics = self.user_data.get("metrics", {})
        recommendations = []
        
        # Water intake recommendation
        water_intake = metrics.get("water_intake", 0)
        if water_intake < 6:
            recommendations.append("Try to increase your water intake to at least 6-8 glasses per day.")
        
        # Steps recommendation
        steps = metrics.get("steps", 0)
        if steps < 5000:
            recommendations.append("Aim to increase your daily steps. Try taking short walks throughout the day.")
        
        # Sleep recommendation
        sleep_hours = metrics.get("sleep_hours", 0)
        if sleep_hours < 7:
            recommendations.append("Try to get 7-9 hours of sleep for optimal health.")
        
        # Energy level recommendation
        energy_level = metrics.get("energy_level", 5)
        if energy_level < 5:
            recommendations.append("Consider incorporating more nutritious foods and regular exercise to boost energy.")
        
        if not recommendations:
            return "🌟 Great job! You're maintaining healthy habits. Keep up the good work!"
        
        # Add a random wellness tip
        tip = random.choice(self.wellness_tips)
        recommendations.append(f"💡 Wellness Tip: {tip}")
        
        return "🎯 Personalized Recommendations:\n- " + "\n- ".join(recommendations)

def main():
    """Main function to demonstrate the Health & Wellness Agent"""
    agent = HealthWellnessAgent()
    
    print(agent.greet_user())
    print("\n" + "="*50 + "\n")
    
    # Set up a sample user profile
    print(agent.set_user_profile(
        name="Alex",
        age=30,
        height=175,  # cm
        weight=70,   # kg
        fitness_level="intermediate",
        health_conditions=[]
    ))
    print("\n" + "="*50 + "\n")
    
    # Update some metrics
    print(agent.update_metrics(
        water_intake=5,
        steps=8000,
        sleep_hours=7.5,
        mood="Good",
        energy_level=8
    ))
    print("\n" + "="*50 + "\n")
    
    # Get various suggestions and advice
    print(agent.get_daily_tip())
    print()
    print(agent.suggest_exercise())
    print()
    print(agent.suggest_mindfulness())
    print()
    print(agent.get_nutrition_advice())
    print("\n" + "="*50 + "\n")
    
    # Get health summary and recommendations
    print(agent.get_health_summary())
    print("\n" + "="*50 + "\n")
    print(agent.get_recommendation())

if __name__ == "__main__":
    main()
