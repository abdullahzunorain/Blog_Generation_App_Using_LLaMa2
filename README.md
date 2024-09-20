# Blog Generation App Using LLaMa2

## Overview
This project is a **Streamlit-based web application** that generates blog posts using the **LLaMa2 language model**. It allows users to input a blog topic, specify a word limit, and choose a writing style for different audiences. The application leverages the **LangChain** library to interact with the **LLaMa2 model** for natural language generation.

The app is designed to be user-friendly, making it easy for users to create blog content quickly and efficiently with just a few inputs. The app can generate content tailored to specific audiences like researchers, data scientists, or common readers, making it a versatile tool for content creation.

---

## Features
- **Custom Blog Generation**: Users can specify a topic, word count, and the target audience for the blog.
- **Supports Multiple Styles**: Users can choose from various writing styles like:
  - Researchers
  - Data Scientists
  - Common People
- **Real-time Content Creation**: Upon entering the inputs and clicking the "Generate" button, the app generates and displays a blog post in real-time.
- **Powered by LLaMa2**: The application uses the **LLaMa2-7B** model (a state-of-the-art language model) for generating coherent and high-quality blog content.

---

## Technology Stack

### Frontend:
- **Streamlit**: Used to build the user interface of the web application. Streamlit simplifies the process of building interactive apps and displaying machine learning results in real-time.

### Backend:
- **LangChain**: A library that integrates LLMs (Large Language Models) like LLaMa2, simplifying the task of building applications that use language models.
- **CTransformers**: This library handles the interaction with transformer-based models like LLaMa2. It allows for loading the model and configuring its response behavior (e.g., temperature, max tokens).

---

## How It Works

1. **User Inputs**:
   - **Blog Topic**: The user inputs a topic for the blog (e.g., "Artificial Intelligence in Healthcare").
   - **Word Count**: The user specifies the number of words for the blog.
   - **Writing Style**: The user selects a style from the dropdown list. Options include "Researchers," "Data Scientists," and "Common People."

2. **Prompt Generation**:
   - The app uses a **PromptTemplate** from LangChain to create a structured prompt based on the user’s inputs (topic, word count, and style).
   - For example:  
     _"Write a blog for **Researchers** job profile for a topic **Artificial Intelligence in Healthcare** within **500** words."_

3. **Blog Generation**:
   - The prompt is sent to the **LLaMa2 model** (7 billion parameter version) using **CTransformers**.
   - The model generates the blog content based on the prompt.

4. **Displaying the Blog**:
   - Once the LLaMa2 model generates the blog content, it is displayed on the app in real-time for the user to read and use.

---

## Setup and Installation

### Prerequisites
Before running the project, make sure you have the following installed:
- Python 3.8+
- **Streamlit**
- **LangChain**
- **CTransformers**
- A local copy of the **LLaMa2 model** (`llama-2-7b-chat.ggmlv3.q8_0.bin`), placed in the `models/` directory.

### Installation Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo-name/blog-generation-llama2.git
    cd blog-generation-llama2
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Place the **LLaMa2 model** in the `models/` folder. You can download the model from **Meta's AI repository** or wherever you have access to the model.

4. Run the application:
    ```bash
    streamlit run app.py
    ```

5. Open your web browser and go to the displayed URL, typically `http://localhost:8501/`.

---

## Folder Structure

```bash
blog-generation-llama2/
│
├── models/
│   └── llama-2-7b-chat.ggmlv3.q8_0.bin  # LLaMa2 model binary
│
├── app.py                               # Main Streamlit app
├── README.md                            # Project documentation
├── requirements.txt                     # List of Python dependencies
└── ...
```

---

## Future Enhancements

Some features to consider adding in the future:
- **Support for additional writing styles**: Expanding the audience options, e.g., technical writers, marketers, etc.
- **Support for additional languages**: Allowing users to generate blogs in languages other than English.
- **Post-editing tools**: Offering the ability to edit or refine the generated content within the app.
- 
