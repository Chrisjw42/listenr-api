import numpy as np

def get_random_session():
    """Return a set of configured sessions."""

    response = {
  "count": 5,
  "sessions": 
  [
    {
      "name": "Product Testing - Project 1",
      "notes": "Performed a testing session with users for project 1.",
      "analysis_output": 
      {
        "anger": 0.07,
        "disgust": 0.64,
        "fear": 0.03,
        "happy": 0.1,
        "neutral": 0.4,
        "sad": 0.85
      }
    },
    {
      "name": "Initial product interviews",
      "notes": "Testing product with user group",
      "analysis_output": 
      {
        "anger": 0,
        "disgust": 0.05,
        "fear": 0.05,
        "happy": 0.5,
        "neutral": 0.3,
        "sad": 0.1
      }
    },
    {
      "name": "UX interview # 42",
      "notes": "Testing with SME around usability of legacy system",
      "analysis_output": 
      {
        "anger": 0.4,
        "disgust": 0.27,
        "fear": 0,
        "happy": 0.23,
        "neutral": 0.06,
        "sad": 0.04
      }
    },
    {
      "name": "A Grand Day Out",
      "notes": "Wallace and gromit go to the moon in search of cheese",
      "analysis_output": 
      {
        "anger": 0,
        "disgust": 0,
        "fear": 0.14,
        "happy": 0.76,
        "neutral": 0.1,
        "sad": 0
      }
    },
    {
      "name": "Group interview #5",
      "notes": "Hands-on testing of the latest app version",
      "analysis_output": 
      {
        "anger": 0.43,
        "disgust": 0.27,
        "fear": 0.1,
        "happy": 0.03,
        "neutral": 0.07,
        "sad": 0.1
      }
    }
  ]
}

    return responses
