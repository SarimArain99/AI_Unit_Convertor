# AI Unit Converter

## Overview

The **AI Unit Converter** is a manual unit conversion tool built using **Streamlit**. It allows users to input a numerical value, select the current unit, and choose the desired conversion unit from a list—similar to Google’s unit converter.

## Features

- 📏 **Supports multiple unit types** (Length, Weight, Temperature, etc.)
- 🔄 **Instant conversion results**
- 🎨 **Simple and user-friendly UI** built with Streamlit
- 🔐 **Secure handling of API keys** (if using external APIs)

## Installation

To run the project locally, follow these steps:

### Prerequisites

Ensure you have **Python 3.8+** installed on your system.

### Clone the Repository

```bash
git clone https://github.com/yourusername/ai-unit-converter.git
cd ai-unit-converter
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables (if applicable)

If the project requires an API key, create a `.env` file and add:

```bash
API_KEY=your_secret_api_key
```

### Run the Application

```bash
streamlit run app.py
```

## Usage

1. Enter the numerical value in the input field.
2. Select the current unit from the dropdown list.
3. Choose the target unit for conversion.
4. View the converted result instantly!

## Deployment

The project can be deployed on **Streamlit Cloud**, **Heroku**, or any cloud service supporting Python apps.

To deploy on Streamlit Cloud:

1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/), log in, and create a new app.
3. Connect your GitHub repository and deploy!

## Contributing

Contributions are welcome! If you'd like to improve this project, please:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the **MIT License**.

---
🌟 **Enjoy using AI Unit Converter!** 🌟
