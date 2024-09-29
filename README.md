<a href="https://health-companion.onrender.com/" target="_blank">Health Companion Application &#128279;</a>
<h1>Health Companion</h1>

<h2>Overview</h2>
<p>Many individuals worldwide encounter challenges in accessing healthcare due to geographical barriers, costs, and a lack of medical professionals. This often results in misdiagnosis and delayed treatment, leading to patient harm. Our project addresses these issues by utilizing machine learning algorithms for symptom analysis and disease prediction. It offers personalized insights such as disease descriptions, medication recommendations, diets, health tips, and first aid precautions. The system also features a chatbot for health-related queries and integrates language translation and text-to-speech functionality for enhanced user interaction.</p>

<h2>Features</h2>
<ul>
  <li><strong>Symptom Checker and Disease Prediction:</strong> Analyzes user symptoms and predicts diseases using a pre-trained Random Forest model.</li>
  <li><strong>Chatbot:</strong> Responds to user queries using a deep learning model trained for intent classification.</li>
  <li><strong>Medical Recommendations:</strong> Provides precautions, medications, diets, and workouts based on disease predictions.</li>
  <li><strong>Multilingual Support:</strong> Integrated with Google Translate API to translate symptom inputs into the user's preferred language.</li>
  <li><strong>Text-to-Speech:</strong> Uses Google Text-to-Speech API to read out the recommendations for better accessibility.</li>
  <li><strong>Image Fetching:</strong> Fetches images related to recommended diets dynamically using the Unsplash API.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
  <li>Python (Flask, TensorFlow/Keras, Random Forest)</li>
  <li>SQLite database for managing user data</li>
  <li>Google Translate API for language translation</li>
  <li>Google Text-to-Speech (gTTS) for converting text to audio</li>
  <li>Unsplash API for fetching relevant images</li>
</ul>

<h2>Project Structure</h2>
<pre>
Health Companion
├── static/                    - Static files (CSS, JS, images)
├── templates/                 - HTML templates for web pages
├── model/                     - Pre-trained models (Random Forest, Chatbot)
├── app.py                     - Main Flask application
├── health_companion.db         - SQLite database file
├── requirements.txt           - Python dependencies
└── README.md                  - Project documentation (this file)
</pre>

<h2>Installation</h2>
<p>Clone the repository:</p>
<pre><code>git clone https://github.com/HarikaCheruku/HealthCompanion.git
cd HealthCompanion
</code></pre>
<p>Install the dependencies:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h2>Usage</h2>
<p>Start the Flask application:</p>
<pre><code>python app.py</code></pre>
<p>Visit <a href="http://localhost:5000">http://localhost:5000</a> to access the Health Companion system.</p>

<h2>Future Improvements</h2>
<ul>
  <li>Expand the disease prediction model to include a wider range of diseases and symptoms.</li>
  <li>Develop a mobile application for easier access on smartphones.</li>
  <li>Enhance chatbot accuracy and extend its database for better health advice.</li>
</ul>

<h2>Contributing</h2>
<p>If you want to contribute to this project, feel free to open issues or submit pull requests. Make sure to follow the contribution guidelines.</p>

