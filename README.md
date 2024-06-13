# WordWeaver: The Blog Generator 📚✒️

WordWeaver is an interactive web application built with MistralAI model of HuggingFace with the help of LangChain framework to generate blog articles based on user-provided topics and preferences. Whether you need a technical tutorial, a lifestyle piece, travel recommendations, or any other topic, WordWeaver automates the process of creating engaging and informative blog content.

## Features

- **Topic Selection**: Choose from a variety of suggested topics or enter your own custom topic.
- **Blog Style**: Select the style of the blog (e.g., Technical, Lifestyle, Travel) to tailor the content generation.
- **Word Count**: Adjust the length of the generated blog article from 50 to 1000 words.
- **Instant Generation**: Quickly generate blog content with just a click of a button.
- **Feedback**: Visual feedback during content generation with a loading spinner and success message.

## Project Structure

The project structure is organized as follows:
```
WordWeaver/
│
├── app.py # Main Streamlit application script
├── requirements.txt # Dependencies required for the project
├── .env # Environment variable configuration file (not included in repository)
├── README.md # Project documentation (you are here)
├── assets/ # Folder for project assets
│ └── images/ # Folder for images used in the application
│ ├── image1.png # Example image 1 (replace with your own)
│ └── image2.png # Example image 2 (replace with your own)
└── LICENSE # License file for the project
```

### Installing

Follow these steps to set up WordWeaver on your local machine:

1. Clone the repository:
```
git clone https://github.com/iSathyam31/WordWeaver.git
cd WordWeaver
```   

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Set up environment variables:

- Create a `.env` file in the root directory.
- Add your HuggingFace API token to the `.env` file
```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here
```

## Using 
Run the application:
```
streamlit run app.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
* Thanks to Streamlit for providing an intuitive framework for building interactive web applications.
* Thanks to HuggingFace and LangChain for their powerful models and ecosystem that make natural language processing accessible.