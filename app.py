"""
Example usage of the HealthWellnessAgent in other applications
"""

# Example 1: Basic usage
from main import HealthWellnessAgent

def example_basic_usage():
    """Demonstrate basic usage of the HealthWellnessAgent"""
    print("=== Basic Usage Example ===")
    
    # Create an instance of the agent
    agent = HealthWellnessAgent()
    
    # Set up user profile
    agent.set_user_profile(
        name="Sarah",
        age=28,
        height=165,
        weight=58,
        fitness_level="intermediate"
    )
    
    # Update some metrics
    agent.update_metrics(
        water_intake=6,
        steps=8500,
        sleep_hours=7.0,
        mood="Good",
        energy_level=7
    )
    
    # Get recommendations
    print(agent.get_daily_tip())
    print(agent.suggest_exercise())
    print(agent.get_recommendation())

# Example 2: Integration with a fitness app
class FitnessApp:
    """Example fitness application integrating the HealthWellnessAgent"""
    
    def __init__(self):
        self.agent = HealthWellnessAgent()
        self.user_logged_in = False
    
    def login(self, name, age, height, weight, fitness_level):
        """User login and profile setup"""
        result = self.agent.set_user_profile(name, age, height, weight, fitness_level)
        self.user_logged_in = True
        return result
    
    def log_workout(self, steps, water_intake):
        """Log workout data"""
        if not self.user_logged_in:
            return "Please log in first"
        
        return self.agent.update_metrics(steps=steps, water_intake=water_intake)
    
    def get_wellness_tip(self):
        """Get a wellness tip"""
        if not self.user_logged_in:
            return "Please log in first"
        
        return self.agent.get_daily_tip()
    
    def get_post_workout_advice(self):
        """Get post-workout advice"""
        if not self.user_logged_in:
            return "Please log in first"
        
        return f"{self.agent.suggest_mindfulness()}\n{self.agent.get_nutrition_advice()}"

def example_fitness_app():
    """Demonstrate integration with a fitness app"""
    print("\n=== Fitness App Integration Example ===")
    
    # Create fitness app instance
    app = FitnessApp()
    
    # User login
    print(app.login("Mike", 35, 180, 80, "beginner"))
    
    # Log a workout
    print(app.log_workout(steps=5000, water_intake=4))
    
    # Get wellness recommendations
    print(app.get_wellness_tip())
    print(app.get_post_workout_advice())

# Example 3: Customizing the agent
def example_customization():
    """Demonstrate how to customize the agent"""
    print("\n=== Customization Example ===")
    
    agent = HealthWellnessAgent()
    
    # Add custom wellness tips
    agent.wellness_tips.append("Remember to stretch after your workouts!")
    agent.wellness_tips.append("Try to eat a rainbow of colors in your meals!")
    
    # Add custom exercise routines
    agent.exercise_routines["beginner"].append("5-minute meditation and stretching")
    
    # Use the customized agent
    agent.set_user_profile("Emma", 25, 170, 62, "beginner")
    print(agent.get_daily_tip())
    print(agent.suggest_exercise("beginner"))

if __name__ == "__main__":
    # Run all examples
    example_basic_usage()
    example_fitness_app()
    example_customization()
    
    print("\n=== All examples completed ===")
