# Research_ITDR
Working prototype of an AI-based behavioral biometrics system that adds an extra layer of IAM security
Step-by-Step Guide: Running AI-Based Behavioral Biometrics System
This guide provides detailed instructions to set up and run an AI-based behavioral biometrics system using Python, Flask, and Visual Studio Code (VS Code). The system captures user behavior (mouse movement, typing speed) and uses a trained machine learning model to assess identity risk.
Here's a working prototype of an AI-based behavioural biometrics system that adds an extra layer of IAM security:
________________________________________
What This Code Does
🧠 Behavioral Features
We'll now track and analyze:
•	Mouse speed (pixels/second)
•	Mouse direction (angle of movement)
•	Mouse acceleration (change in speed)
•	Key dwell time (how long a key is held)
•	Key flight time (time between key releases and next key presses)
•	Navigation method (Tab vs. Mouse)

🚨 Aggressive Detection Logic
We'll flag behavior as phishing or suspicious if:
•	Mouse speed is too fast or too slow compared to training
•	Mouse direction is erratic or unusual
•	Acceleration is spiky or inconsistent
•	Navigation method changes (e.g., trained with Tab, tested with Mouse)
Feature	Tracked	Used in Model
Mouse Speed	✅	✅
Mouse Direction	✅	✅ (angle + variance)
Mouse Acceleration	✅	✅
Key Dwell Time	✅	✅
Key Flight Time	✅	✅
Navigation Method	✅	✅

•	Trains a Random Forest model to distinguish between legitimate users and impostors.
•	Evaluates the model and simulates a new session to compute a risk score.
•	Outputs a trained model file for integration into a real-time IAM system.
________________________________________
Model Evaluation
The model achieved 100% accuracy on the test set (small simulated dataset), and the risk score for a new session was:
Risk score for the new session: 0.37
This means the session is likely legitimate (low risk).


Step 1: Prerequisites
• Python 3.8 or later installed on your system.
• Visual Studio Code (VS Code) installed.
• Python extension installed in VS Code.
• behavior_model.pkl (trained model file) available in your project folder.
Step 2: Create Project Folder
1. Open VS Code.
2. Create or open a folder, e.g., behavioral-biometrics.
3. Inside this folder, create the following files:
   • app.py – Flask API to serve the model.
   • behavior_model.pkl – Trained ML model.
   • index.html – Frontend to collect user behavior.
Step 3: Set Up Virtual Environment
1. Open terminal in VS Code (Ctrl + `).
2. Run the following command:
   python -m venv venv
3. Activate the environment:
   • Windows: .\venv\Scripts\activate
   • macOS/Linux: source venv/bin/activate
Step 4: Install Required Libraries
Run the following command in the terminal:
   pip install flask numpy scikit-learn
Step 5: Create Flask API (app.py)
Step 6: Run the Flask Server
1. Ensure your virtual environment is activated.
2. Run the following command:
   python app.py
3. You should see: Running on http://127.0.0.1:5000/
Step 7: Create Frontend (index.html)
Create a file named index.html and paste the JavaScript + HTML code below to capture mouse and keyboard behavior.
Step 8: Test the System
1. Open index.html in a browser.
2. Interact with the page (move mouse, type).
3. Click Login to send data to the Flask API.
4. You will see a risk score alert based on your behavior.

Now you can also send POST requests to http://localhost:5000/analyze with behavioural data.
________________________________________
Example Request (via Postman or JavaScript)
{
  "mouse_speed": 0.58,
  "click_interval": 0.27,
  "key_dwell_time": 0.12,
  "key_flight_time": 0.08
}

To make the system user-specific, it needs to:
Learn and Adapt to Each User's Behavior Over Time
Here’s how you can achieve that:
________________________________________
1. Data Storage (User Profiles)
You’ll need a database to store behavioral data per user. For example:
Schema:
{
  "user_id": "user123",
  "sessions": [
    {
      "mouse_speed": 0.58,
      "click_interval": 0.27,
      "key_dwell_time": 0.12,
      "key_flight_time": 0.08,
      "timestamp": "2025-07-08T21:30:00"
    },
    ...
  ]
}
You can use:
•	SQLite (for local testing)
•	PostgreSQL / MongoDB (for production)
•	Firebase / Supabase (for cloud-based apps
2. Model Training Per User
Instead of one global model, train a personalized ML model for each user:
Workflow:
1.	Collect multiple sessions for each user.
2.	Extract features and label them as "legitimate".
3.	Use anomaly detection models (e.g., Autoencoders, One-Class SVM) to learn what’s normal for that user.
4.	When a new session comes in, compare it to the user’s profile.
________________________________________
3. Continuous Learning
Each time a user logs in successfully:
•	Store the session data.
•	Retrain the model periodically (e.g., nightly or weekly).
•	Use incremental learning to avoid retraining from scratch.
________________________________________
4. Risk-Based IAM Integration
If the model detects a deviation:
•	Trigger step-up authentication (e.g., MFA).



How to Run the System
1.Activate your virtual environment:
bash
.\venv\Scripts\activate
2.Start the Flask server:
bash
python app.py
3.Open index.html in your browser and begin training.
4. Now you can also send POST requests to http://localhost:5000/analyze with behavioral data.
________________________________________
Example Request (via Postman or JavaScript)
{
  "mouse_speed": 0.58,
  "click_interval": 0.27,
  "key_dwell_time": 0.12,
  "key_flight_time": 0.08
}

 


•	Alert the security team.
•	Log the event for audit.
<img width="940" height="383" alt="image" src="https://github.com/user-attachments/assets/e4c0e530-4b8e-4983-953e-98d5c9fc1370" />




