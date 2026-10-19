# LinkedIn Post Generator 🚀

An AI-powered LinkedIn Post Generator that helps users create engaging, professional, and personalized LinkedIn posts using Large Language Models (LLMs), LangChain, and GroqCloud.

Generate posts on different topics, customize their length, and choose between English and Hinglish to create content suited to your audience.

## ✨ Features

- **AI-Powered Content Generation:** Generate LinkedIn posts using an LLM through GroqCloud.
- **Customizable Post Length:** Choose between Short, Medium, and Long posts.
- **Multi-language Support:** Generate content in English or Hinglish (Hindi + English).
- **Prompt Engineering:** Use structured prompts to improve readability, relevance, and engagement.
- **Post Metadata Extraction:** Extract metadata such as line count, language, and tags from existing posts.
- **Tag Unification:** Standardize similar tags to make post categorization more consistent.
- **JSON-Based Data Processing:** Store raw and processed post data in JSON files.

## 🛠️ Tech Stack

- **Language:** Python
- **LLM Integration:** GroqCloud
- **LLM Framework:** LangChain
- **Model Access:** `langchain-groq`
- **Data Storage:** JSON
- **Development Environment:** Visual Studio Code

## 📁 Project Structure

```text
LinkedInPostGenerator/
│
├── data/
│   ├── raw_posts.json
│   └── processed_posts.json
│
├── .env                  # API key (not committed)
├── .gitignore
├── few_shot.py           # Few-shot examples
├── llm_helper.py         # LLM configuration and initialization
├── main.py               # Application entry point
├── post_generator.py     # LinkedIn post generation logic
├── preprocess.py         # Post metadata and tag preprocessing
└── README.md
```

## ⚙️ Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/LinkedInPostGenerator.git
cd LinkedInPostGenerator
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

**Command Prompt:**
```bash
.venv\Scripts\activate
```

**PowerShell:**
```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the required packages:

```bash
python -m pip install langchain-groq python-dotenv streamlit
```

If your project uses additional packages, install them as well.

For reproducible setup, consider creating a `requirements.txt` file:

```bash
python -m pip freeze > requirements.txt
```

Then future installations can use:

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API Key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from the [Groq Console](https://console.groq.com/).

**Important:** Never commit your real API key to GitHub. Keep `.env` in `.gitignore` and share only a placeholder in `.env.example`.

### 5. Run the Application

To generate a sample LinkedIn post:

```bash
python post_generator.py
```

If your application is configured as a Streamlit app in `main.py`, launch it with:

```bash
python -m streamlit run main.py
```

Use the command that matches the entry point implemented in your project.

## 💡 Example

**Input**

```text
Topic: Mental Health
Length: Short
Language: English
```

**Illustrative Output**

```text
Your mental health deserves the same attention as your career.

Taking a break isn't a sign of weakness.
It's a way to recharge, reflect, and return stronger.

What is one habit that helps you protect your mental well-being?

#MentalHealth #WellBeing #PersonalGrowth
```

*The output above is an example; actual results depend on the prompt and the selected model.*

## 🔄 Data Preprocessing

The preprocessing pipeline works with LinkedIn post data stored in JSON format.

1. Load existing posts from `data/raw_posts.json`.
2. Extract metadata such as line count, language, and tags using an LLM.
3. Identify unique tags across the dataset.
4. Standardize related tags using tag unification.
5. Save the processed results to `data/processed_posts.json`.

This helps organize post data and prepares it for downstream use in the application.

## 🔐 Security

- Store API credentials in environment variables.
- Keep `.env` and other secret files out of version control.
- Never publish private or sensitive post data.
- Use `.env.example` to document required environment variables without exposing secrets.

## 🚀 Future Improvements

- Add a user-friendly interface for entering topics and selecting writing preferences.
- Support multiple post styles, including storytelling, educational, motivational, and technical.
- Allow users to regenerate and edit generated posts.
- Add audience-specific and industry-specific customization.
- Save generated posts and let users revisit their content history.
- Add automated tests and error handling for API failures and rate limits.

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch to your fork.
5. Open a pull request.

---

**Built with Python, LangChain, and GroqCloud.**
