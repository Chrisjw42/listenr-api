import numpy as np

def get_random_session():
    """An incredibly unsophosticated function that returns one of 5 random mock responses"""

    i = np.random.randint(5)

    responses = [
        {"count": 1,
        "sessions": 
        [
            {
            "name": "Product Testing - Project 1",
            "notes": "Performed a testing session with users for project 1.",
            "analysis_output": 
            {
                "anger": 0.07,
                "digust": 0.64,
                "fear": 0.03,
                "happy": 0.1,
                "neutral": 0.4,
                "sad": 0.85
            }
            }
        ]},
        {"count": 1,
        "sessions": 
        [
            {
            "name": "Initial product interviews",
            "notes": "Testing product with user group",
            "analysis_output": 
            {
                "anger": 0.0,
                "digust": 0.05,
                "fear": 0.05,
                "happy": 0.5,
                "neutral": 0.3,
                "sad": 0.1
            }
        }
        ]},
        {"count": 1,
        "sessions": 
        [
            {
            "name": "UX interview # 42",
            "notes": "Testing with SME around usability of legacy system",
            "analysis_output": 
            {
                "anger": 0.4,
                "digust": 0.27,
                "fear": 0.0,
                "happy": 0.23,
                "neutral": 0.06,
                "sad": 0.04
            }
            }
        ]},
        {"count": 1,
        "sessions": 
        [
            {
            "name": "A Grand Day Out",
            "notes": "Wallace and gromit go to the moon in search of cheese",
            "analysis_output": 
            {
                "anger": 0.0,
                "digust": 0.0,
                "fear": 0.14,
                "happy": 0.76,
                "neutral": 0.1,
                "sad": 0.0
            }
            }
        ]},
        {"count": 1,
        "sessions": 
        [
            {
            "name": "Group interview #5",
            "notes": "Hands-on testing of the latest app version",
            "analysis_output": 
            {
                "anger": 0.43,
                "digust": 0.27,
                "fear": 0.1,
                "happy": 0.03,
                "neutral": 0.07,
                "sad": 0.1
            }
            }
        ]}
        ]

    return responses[i]