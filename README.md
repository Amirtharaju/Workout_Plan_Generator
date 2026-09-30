**🏋️ Workout Plan Generator**
An AI-powered personalized workout plan generator built with Python, Streamlit, and Groq.

The application collects fitness preferences from the user and uses an AI model through the Groq API to generate a customized workout plan.

**📌 Project Overview**
The Workout Plan Generator creates personalized workout plans based on:

**Fitness goal**
**Experience level
Number of workout days per week
Available equipment
Injuries or physical limitations**

The application uses Streamlit for the web interface and the Groq API to generate the workout plan using an LLM.

✨ Features
🏋️ Select fitness goal
📈 Select experience level
📅 Select number of workout days per week
🏠 Select available equipment
⚠️ Enter injuries or physical limitations
🤖 Generate an AI-powered workout plan
📝 Display a structured workout plan
🌐 Simple Streamlit web interface
🛠️ Technologies Used
Technology	Purpose
Python	Application development
Streamlit	Web UI
Groq API	LLM / AI generation
python-dotenv	Environment variable management
Git	Version control
GitHub	Source code repository

**📂 Project Structure**
**Workout_Plan_Generator/**
│
├── .venv/                 # Python virtual environment - not committed
├── .env                   # API key - not committed
├── .gitignore             # Git ignore rules
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── LICENSE                # MIT License
⚠️ **The .env file contains the API key and is intentionally excluded from GitHub using .gitignore.**

**🚀 Getting Started
1. Clone the Repository**
git clone https://github.com/Amirtharaju/Workout_Plan_Generator.git
Move into the project directory:

cd Workout_Plan_Generator
**2. Create a Virtual Environment**
On Windows:

python -m venv venv
Activate the virtual environment:

.\venv\Scripts\Activate.ps1
After activation, your terminal should show something similar to:

(venv) PS D:\Amir\Projects\Workout_Plan_Generator>
**3. Install Dependencies**
Make sure the virtual environment is activated.

Install the required packages:

python -m pip install -r requirements.txt
Verify Streamlit:

streamlit --version
Or:

python -m streamlit --version
**🔐 4. Configure the Groq API Key**
The application requires a Groq API key.

Create a file named:

.env
in the project root directory.

Example:

GROQ_API_KEY=your_api_key_here
Do not replace the placeholder in this README with your real API key.

Important Security Rule
Never commit your API key to GitHub.

The .gitignore file contains:
**
.env**
Therefore Git ignores the .env file.

You can verify this with:

git check-ignore -v .env
▶️** 5. Run the Application**
Make sure the virtual environment is activated.

Run:

streamlit run app.py
Streamlit will display a URL similar to:

Local URL: http://localhost:8501
Open the URL in your web browser.

🖥️ Using the Application
Step 1 — Select Fitness Goal
Choose one of the available goals:

Build muscle

Lose fat

General fitness

Improve endurance

Step 2 — Select Experience Level
Choose:

Beginner

Intermediate

Advanced

Step 3 — Select Workout Days
Select the number of days you are available to work out each week.

Example:

4 days per week
Step 4 — Select Equipment
Choose the equipment available to you:

No equipment

Home dumbbells

Full gym

Step 5 — Enter Limitations
Optionally provide injuries or physical limitations.

Example:

Bad knees
Step 6 — Generate Workout Plan
Click the generate button.

The application sends the user's preferences to the Groq-powered LLM and displays a personalized workout plan.

🧠 Example User Profile
Fitness Goal: Build Muscle
Experience Level: Beginner
Days Available: 4
Equipment: No Equipment
Limitations: Bad knees
The application generates a workout plan based on the provided requirements.

🔄 Application Flow
User
  │
  ▼
Streamlit Web Interface
  │
  ▼
Collect User Inputs
  │
  ├── Fitness Goal
  ├── Experience Level
  ├── Workout Days
  ├── Equipment
  └── Limitations
  │
  ▼
Build AI Prompt
  │
  ▼
Groq API
  │
  ▼
LLM Response
  │
  ▼
Personalized Workout Plan
  │
  ▼
Display in Streamlit
📋 Requirements
Project dependencies are listed in:

requirements.txt
Install them with:

python -m pip install -r requirements.txt
🔒 Security
API keys and sensitive configuration should never be committed to GitHub.

This project uses a .env file for the Groq API key.

The .gitignore file includes:

.env
.venv/
venv/
__pycache__/
*.pyc
If an API key is accidentally exposed or pushed to a public repository, revoke the exposed key and create a new one.

🧪 Complete Local Setup
From a new machine:

git clone https://github.com/Amirtharaju/Workout_Plan_Generator.git

cd Workout_Plan_Generator

python -m venv venv

.\venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
Create .env:

GROQ_API_KEY=your_api_key_here
Run the application:

streamlit run app.py
🔧 Common Commands
Activate virtual environment
.\venv\Scripts\Activate.ps1
Install dependencies
python -m pip install -r requirements.txt
Run Streamlit
streamlit run app.py
Check Git status
git status
Add changes
git add .
Commit changes
git commit -m "Update workout plan generator"
Push changes
git push
🐛 Troubleshooting
Streamlit is not recognized
Make sure the virtual environment is activated:

.\venv\Scripts\Activate.ps1
Then install dependencies:

python -m pip install -r requirements.txt
You can also run Streamlit through Python:

python -m streamlit run app.py
.env is not found
Make sure .env exists in the project root:

Workout_Plan_Generator/
│
├── .env
├── app.py
└── requirements.txt
Example:

GROQ_API_KEY=your_api_key_here
Port 8501 is already in use
Run Streamlit on another port:

streamlit run app.py --server.port 8502
Then open:

http://localhost:8502
🚧 Future Enhancements
Possible future improvements:

Save generated workout plans

Download workout plan as PDF

Workout history

Progress tracking

Calorie and nutrition recommendations

Exercise demonstration images

Exercise video links

User authentication

Database integration

Cloud deployment

Automated testing

CI/CD pipeline

⚠️ Disclaimer
This application generates AI-based workout suggestions for educational and informational purposes.

It is not a substitute for advice from a qualified fitness professional or healthcare professional.

Users should consider their individual health conditions and physical limitations before starting an exercise program.

👩‍💻 Author
Amirtharaju

GitHub:
https://github.com/Amirtharaju

📄 License
This project is licensed under the MIT License.

See the LICENSE file for details.
