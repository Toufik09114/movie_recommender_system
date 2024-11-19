## Introduction
__The Content-Based Movie Recommendation System is a personalized application that suggests movies to users based on their preferences. By leveraging data science and machine learning, this system helps users navigate through the overwhelming number of choices available and find movies that match their tastes.__

***

## Features
* User registration and login functionality.
* Movie recommendations tailored to user preferences.
* Ability to view recommendation history.
* Interactive and user-friendly interface built using Streamlit.

***

## Technologies Used
* __Python:__ Backend logic and data processing.
* __Pandas:__ For data cleaning and manipulation.
* __Scikit-learn:__ Used for machine learning algorithms (cosine similarity).
* __Streamlit:__ Framework for creating the user interface.
* __Database:__ SQLite for user authentication and storing recommendation history.
* __hashlib:__ To encode the user password.

***

## System Architecture
__Here’s the high-level workflow of the system:__

1. __User Registration/Login:__
Users register with their details and log in to access the system.

2. __Preference Collection:__
Users input preferences such as genre, cast, or favorite directors.

3. __Recommendation Generation:__
Using content-based filtering, movies similar to user preferences are recommended.

4. __Recommendation History:__
Users can view previously recommended movies in their history.

***

## Installation
__Follow these steps to run the project locally:__

1. ___Clone the Repository:__
<div class="code-container">
        <button class="copy-button" onclick="copyCode()">Copy</button>
        <pre><code id="code-snippet">
git clone https://github.com/Toufik09114/movie-recommendation-system.git
</div>

2. __Navigate to the Project Directory:__
<div class="code-container">
        <button class="copy-button" onclick="copyCode()">Copy</button>
        <pre><code id="code-snippet">
cd movie-recommendation-system
</div>

3. __Install Dependencies: Install the required Python libraries using pip:__
<div class="code-container">
        <button class="copy-button" onclick="copyCode()">Copy</button>
        <pre><code id="code-snippet">
pip install -r requirements.txt
</div>

4. __Run the Application: Launch the Streamlit application:__
<div class="code-container">
        <button class="copy-button" onclick="copyCode()">Copy</button>
        <pre><code id="code-snippet">
streamlit run app.py
</div>

***

## Usage
1. Open the application in your browser (usually runs on http://localhost:8501).
2. Register or log in using your credentials.
3. Input your preferences (e.g., genres, favorite movies).
4. Get personalized movie recommendations.
5. View your recommendation history on the dashboard.

***

## Screenshots

__Login Page__
![Screenshot (14)](https://github.com/user-attachments/assets/4c9bef43-bd0d-4073-ad7d-c4b0b4565b0c)
***

__Recommendation Screen__
![Screenshot (15)](https://github.com/user-attachments/assets/0d3c7ca6-a3c8-4f5a-92f2-9b58109a6565)
![Screenshot (16)](https://github.com/user-attachments/assets/3a437284-c04b-4258-9293-5f9c05571c14)

***

__History Tab__
![Screenshot (19)](https://github.com/user-attachments/assets/98fa9ca6-ea5d-4a44-b41e-7de7d1ae2371)

***

## Future Enhancements
* Integrate collaborative filtering for better recommendations.
* Add user reviews and rating systems.
* Implement advanced login methods like Google OAuth.
* Incorporate a larger and more diverse movie dataset.

***

## Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch-name`).
3. Make your changes and commit them (`git commit -m 'Add some feature`).
4. Push to the branch (`git push origin feature-branch-name`).

***

## Demo.
[Watch the video](https://github.com/Toufik09114/movie_recommender_system/blob/main/movie_recommendation_video.mp4)
<video width="320" height="240" controls>
  <source src="(https://github.com/Toufik09114/movie_recommender_system/blob/main/movie_recommendation_video.mp4)" type="video/mp4">
  Your browser does not support the video tag.
</video>
