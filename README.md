Introduction
The Content-Based Movie Recommendation System is a personalized application that suggests movies to users based on their preferences. By leveraging data science and machine learning, this system helps users navigate through the overwhelming number of choices available and find movies that match their tastes.

Features
User registration and login functionality.
Movie recommendations tailored to user preferences.
Ability to view recommendation history.
Interactive and user-friendly interface built using Streamlit.

Technologies Used
Python: Backend logic and data processing.
Pandas: For data cleaning and manipulation.
Scikit-learn: Used for machine learning algorithms (cosine similarity).
Streamlit: Framework for creating the user interface.
Database: SQLite for user authentication and storing recommendation history.

System Architecture
Here’s the high-level workflow of the system:

User Registration/Login:
Users register with their details and log in to access the system.

Preference Collection:
Users input preferences such as genre, cast, or favorite directors.

Recommendation Generation:
Using content-based filtering, movies similar to user preferences are recommended.

Recommendation History:
Users can view previously recommended movies in their history.

(Include a simple diagram or flowchart here, if possible.)

Installation
Follow these steps to run the project locally:

Clone the Repository:
bash
Copy code
git clone https://github.com/Toufik09114/movie-recommendation-system.git

Navigate to the Project Directory:
bash
Copy code
cd movie-recommendation-system

Install Dependencies: Install the required Python libraries using pip:
bash
Copy code
pip install -r requirements.txt

Run the Application: Launch the Streamlit application:
bash
Copy code
streamlit run app.py

Usage
Open the application in your browser (usually runs on http://localhost:8501).
Register or log in using your credentials.
Input your preferences (e.g., genres, favorite movies).
Get personalized movie recommendations.
View your recommendation history on the dashboard.

Example:
Login Page
![Screenshot (14)](https://github.com/user-attachments/assets/4c9bef43-bd0d-4073-ad7d-c4b0b4565b0c)


Recommendation Screen
![Screenshot (15)](https://github.com/user-attachments/assets/0d3c7ca6-a3c8-4f5a-92f2-9b58109a6565)
![Screenshot (16)](https://github.com/user-attachments/assets/3a437284-c04b-4258-9293-5f9c05571c14)



History Tab
![Screenshot (19)](https://github.com/user-attachments/assets/98fa9ca6-ea5d-4a44-b41e-7de7d1ae2371)


Future Enhancements
Integrate collaborative filtering for better recommendations.
Add user reviews and rating systems.
Implement advanced login methods like Google OAuth.
Incorporate a larger and more diverse movie dataset.
Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch-name).
Make your changes and commit them (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch-name).

Demo.
<video width="320" height="240" controls>
  <source src="path/to/your/video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
