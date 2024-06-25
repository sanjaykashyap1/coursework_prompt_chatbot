
# Healthcare Chatbot

This project is a simple healthcare chatbot that provides remedies for various symptoms using a pre-defined dataset and OpenAI's GPT-3.5-turbo model. The chatbot is built using Streamlit for the user interface.

## Features

- Provides immediate remedies for common symptoms from a predefined dataset.
- Uses OpenAI's GPT-3.5-turbo model to generate remedies for symptoms not found in the dataset.
- Ensures responses are focused on healthcare-related advice.

## Demo

Watch the video demo of the Healthcare Chatbot on YouTube:

[![Healthcare Chatbot Demo](https://img.youtube.com/vi/mCFzmJy1G3g/0.jpg)](https://youtu.be/mCFzmJy1G3g)

## Setup

### Prerequisites

- Python 3.7 or higher
- Streamlit
- OpenAI API key

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    cd your-repository-name
    ```

2. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.streamlit` directory**:

    ```bash
    mkdir .streamlit
    ```

4. **Create a `secrets.toml` file in the `.streamlit` directory and add your OpenAI API key**:

    ```toml
    [secrets]
    OPENAI_API_KEY = "your_openai_api_key_here"
    ```

### Usage

1. **Ensure the `healthcare_data.json` file is in the project directory**.

2. **Run the Streamlit application**:

    ```bash
    streamlit run app.py
    ```

3. **Open your web browser and go to `http://localhost:8501` to interact with the chatbot**.

### Examples

#### Example 1

**User Input:**
```
What symptom are you experiencing?
I have a headache
```

**Chatbot Response:**
```
Remedy for I have a headache:
Remedy: Drink plenty of water, rest in a quiet dark room, apply a cold compress to the forehead, and consider taking over-the-counter pain relief medication such as ibuprofen or acetaminophen. If headaches persist or worsen, consult a healthcare provider.
```

#### Example 2

**User Input:**
```
What symptom are you experiencing?
I have teeth pain
```

**Chatbot Response:**
```
Remedy for I have teeth pain:
Remedy: Rinse your mouth with warm salt water to help alleviate tooth pain. Contact a dentist for further evaluation and treatment if the pain persists.

Note: This chatbot is for informational purposes only. Please consult a healthcare professional for medical advice.
```

#### Example 3

**User Input:**
```
What symptom are you experiencing?
How to play basketball?
```

**Chatbot Response:**
```
Sorry, I can only provide information and remedies for healthcare-related symptoms. Please consult a healthcare professional for other inquiries.

Note: This chatbot is for informational purposes only. Please consult a healthcare professional for medical advice.
```

#### Example 4

**User Input:**
```
What symptom are you experiencing?
How to perform a surgery?
```

**Chatbot Response:**
```
Sorry, I can only provide information and remedies for healthcare-related symptoms. Please consult a healthcare professional for other inquiries.

Note: This chatbot is for informational purposes only. Please consult a healthcare professional for medical advice.
```

## File Structure

- `app.py`: The main Streamlit application script.
- `healthcare_data.json`: The JSON file containing healthcare symptoms and remedies.
- `.streamlit/secrets.toml`: The secrets file containing the OpenAI API key.
- `README.md`: This readme file.

### Example `healthcare_data.json`

Ensure your `healthcare_data.json` is structured as follows:

```json
[
    {
        "symptom": "Headache",
        "remedy": "Take a pain reliever such as ibuprofen or acetaminophen. Rest in a quiet, dark room. Apply a cool compress to your forehead."
    },
    {
        "symptom": "Sore Throat",
        "remedy": "Gargle with warm salt water. Drink warm liquids such as tea with honey. Suck on throat lozenges."
    },
    {
        "symptom": "Fever",
        "remedy": "Stay hydrated by drinking plenty of fluids. Take a lukewarm bath. Use fever-reducing medications such as acetaminophen or ibuprofen."
    }
    // Add more entries as needed
]
```

### Notes

- This chatbot is for informational purposes only. Always consult a healthcare professional for medical advice.
- Ensure your OpenAI API key is kept secure and not shared publicly.
