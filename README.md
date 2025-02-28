🎸 Chord Classification
🚀 Project Overview
This project is a deep learning-based chord classification system that identifies musical chords from audio recordings. By leveraging Convolutional Neural Networks (CNNs) and Chroma feature extraction, the model can accurately recognize chords from WAV files.
![Screenshot 2025-02-19 033312](https://github.com/user-attachments/assets/eb33313d-8bfb-41a7-8551-afd1fd7552dd)

✨ Features
The dataset is created by myself
Supports a wide range of chords: major, minor, diminished, augmented, 7th, and more.
Advanced audio processing: Uses Chroma feature extraction for precise chord identification.
Deep learning-powered: Built with Python, TensorFlow/Keras, and Librosa.
User-friendly interface: Interactive UI with Streamlit for real-time predictions.
Customizable and extensible: Train the model with additional chord samples for improved accuracy.

📂 Project Structure

📦 chord-classification
 ┣ 📂 dataset/           # Chord audio samples  
 ┣ 📂 models/            # Trained CNN models  
 ┣ 📂 scripts/           # Feature extraction & training scripts  
 ┣ 📂 docs/              # Documentation and references  
 ┣ 📜 app.py             # Streamlit UI for chord classification  
 ┣ 📜 model.py           # CNN model implementation  
 ┣ 📜 requirements.txt   # Dependencies  
 ┗ 📜 README.md          # Project documentation  
 
📊 Model Performance

Training Accuracy: 87%

Test Accuracy: 77%

Note: Performance metrics will improve with a larger dataset.

🛠 How It Works
Feature Extraction: Converts audio files into chroma spectrograms.
CNN Model: Classifies the chord based on the extracted features.
Interactive UI: Users upload audio files and receive real-time predictions.
📌 Future Improvements
Expand dataset for better generalization.
Implement real-time audio input processing.
Optimize the CNN model for faster inference.

MADE WITH LOVE BY KAVISH :)❤

