# Content-Based Movie Recommendation System

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
```bash
git clone https://github.com/Toufik09114/movie-recommendation-system.git
```

2. __Navigate to the Project Directory:__
```bash
cd movie-recommendation-system
```

3. __Install Dependencies: Install the required Python libraries using pip:__
```bash
pip install -r requirements.txt
```

4. __Run the Application: Launch the Streamlit application:__
```bash
streamlit run app.py
```
___ 
                
## Usage
Follow these steps to use the application:

1. Open your web browser and navigate to the local server where the application is running (usually `http://localhost:8501`).
2. **Registration**:
   - Enter your details (e.g., username, email, password) to create a new account.
   - Submit the registration form to save your credentials.
3. **Login**:
   - Use your registered username and password to log in.
4. **Preference Input**:
   - Enter your preferences such as favorite genres, cast, or movies to customize the recommendations.
5. **View Recommendations**:
   - The system will display the top 5 movie recommendations matching your preferences.
   - Each recommendation includes details such as title, genre, and an overview.
6. **History Tab**:
   - Access the history tab to view previously recommended movies.

***
## Screenshots
Here are some visual representations of the application:

### **Login Page**
![Screenshot (14)](https://github.com/user-attachments/assets/4c9bef43-bd0d-4073-ad7d-c4b0b4565b0c)
_Description: The login page allows users to securely access their accounts._

### **Recommendation Screen**
![Screenshot (15)](https://github.com/user-attachments/assets/0d3c7ca6-a3c8-4f5a-92f2-9b58109a6565)
![Screenshot (16)](https://github.com/user-attachments/assets/3a437284-c04b-4258-9293-5f9c05571c14)
_Description: The screen displays the top 5 movie recommendations with relevant details._

### **History Tab**
![Screenshot (19)](https://github.com/user-attachments/assets/98fa9ca6-ea5d-4a44-b41e-7de7d1ae2371) 
_Description: The history tab shows the user’s past movie recommendations._

---

## Future Enhancements
The project can be further improved with the following features:
- **Collaborative Filtering**: Include recommendations based on user behavior and preferences of similar users.
- **Review and Ratings Integration**: Allow users to rate recommended movies and provide feedback.
- **Advanced Authentication**: Add Google OAuth or other third-party login options.
- **Dataset Expansion**: Use a more extensive and diverse movie dataset for better recommendations.

---

## Contributing
Contributions are welcome! To contribute:  
### 1. Fork the Repository:  
   Click the "Fork" button on the top right corner of this repository.  

### 2. Create a new branch.
To make your changes, create a new branch using the following command:
```bash
 git checkout -b feature-branch-name
```

Replace feature-branch-name with a descriptive name for your branch (e.g., add-new-feature or fix-issue)

### 3. Make your changes and commit them.
Edit files, implement features, or fix bugs as required.

### 4. Add and Commit Your Changes
After making changes, stage the files and commit them with a meaningful message:
```bash
git add .
git commit -m "Add feature or fix issue"
```

### 5. Push to the branch
Push the branch to your forked repository.
```bash
git push origin feature-branch-name
```

### 6. Create a Pull Request
Go to the original repository and open a Pull Request (PR) from your branch. Add a clear description of the changes you've made

***

## Demo.
[Watch the video](https://github.com/Toufik09114/movie_recommender_system/blob/main/movie_recommendation_video.mp4)
<video width="320" height="240" controls>
  <source src="(https://github.com/Toufik09114/movie_recommender_system/blob/main/movie_recommendation_video.mp4)" type="video/mp4">
  Your browser does not support the video tag.
</video>
