# FarmerAid: Crop Disease Detection

FarmerAid is a web application that utilizes deep learning to detect diseases in tomato plants. With just a click of a button, farmers can upload images of their crops and receive instant diagnosis for common diseases.

## Features

- Detects Tomato Target Spot, Tomato Yellow Leaf Curl Virus, and Tomato Mosaic Virus
- Simple user interface for easy image upload and disease detection
- Provides confidence level for each prediction

## Getting Started

### Prerequisites

- Python 3.x
- Streamlit
- Keras
- OpenCV
- PIL

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/farmer-aid.git
```
## Step-by-Step Approach

1. **Install Dependencies**:
   - Ensure Python 3.x is installed.
   - Install required packages using pip:
     ```bash
     pip install streamlit keras opencv-python-headless pillow
     ```

2. **Download Pre-trained Model**:
   - Obtain a pre-trained deep learning model for crop disease detection (e.g., '95.h5').

3. **Set Up Streamlit App**:
   - Create a Python script (e.g., `app.py`) and import necessary libraries.
   - Define the Streamlit app title and introduction.

4. **Load the Model**:
   - Use `load_model` from `keras.models` to load the pre-trained model.

5. **Define Image Preprocessing Function**:
   - Create a function to preprocess the uploaded image before feeding it into the model.
   - Convert the image to an array, resize it to the required input size, and normalize pixel values.

6. **Create Streamlit Interface**:
   - Use Streamlit's `st.title`, `st.info`, `st.header`, and `st.file_uploader` to create the user interface.
   - Allow users to upload an image of a tomato plant for disease detection.

7. **Perform Disease Detection**:
   - Process the uploaded image using the preprocessing function.
   - Use the loaded model to predict the probability of each class.
   - Display the predicted class and confidence level.

8. **Run the Streamlit App**:
   - Run the Streamlit app using the command:
     ```bash
     streamlit run app.py
     ```

9. **Interact with the App**:
   - Open a web browser and navigate to the provided URL to interact with the FarmerAid app.
   - Upload images of tomato plants to detect diseases and view the predictions.
