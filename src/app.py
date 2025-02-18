import streamlit as st
import librosa
import numpy as np
import tensorflow as tf
import pickle
from sklearn.preprocessing import StandardScaler

# Load trained model
model = tf.keras.models.load_model("C:/Users/shahk/OneDrive/Desktop/updated chords/chord_classification_model.h5")

# Load label encoder
with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# Load scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Function to extract chroma features from uploaded audio
def extract_chroma_features(audio_file, sr=22050, n_chroma=12):
    y, sr = librosa.load(audio_file, sr=sr)

    # Extract chroma features
    chroma = librosa.feature.chroma_stft(y=y, sr=sr, n_chroma=n_chroma)
    chroma_mean = np.mean(chroma, axis=1)  # Take mean across time axis
    
    return chroma_mean

# Streamlit UI
st.title("🎸 Chord Classification App")
st.markdown("Upload an audio file to predict the chord.")

# Upload audio file
uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

if uploaded_file is not None:
    # Extract chroma features
    features = extract_chroma_features(uploaded_file)
    features = features.reshape(1, -1)  # Reshape for model input

    # Normalize using the saved scaler
    features = scaler.transform(features)

    # Predict
    prediction = model.predict(features)
    predicted_index = np.argmax(prediction)

    # Convert index to chord name
    predicted_chord_name = label_encoder.inverse_transform([predicted_index])[0]

    # Display result
    st.write(f"🎵 **Predicted Chord: {predicted_chord_name}**")
