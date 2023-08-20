import csv

def load_csv_data(csv_path):
    meals = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            meals.append(row)
    return meals

def get_workout_suggestions(user_inputs):
    workout_suggestions = {
        "30 minutes of Cardio Exercises":[
            "Running",
            "Cycling",
            "Swimming",
            "Jumping rope"
            "Dancing",
        ],
        "Strength Training with Weights":[
            "Weightlifting",
            "Dumbbell exercises",
            "Barbell exercises",
            "Resistance band exercises",
        ],
        "Yoga and Stretching Routine":[
            "Yoga practice",
            "Stretching exercises",
            "Pilates",
            "Tai Chi"
        ]
    }
    return workout_suggestions

