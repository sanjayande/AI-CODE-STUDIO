# 🚀 AI Code Studio

AI Code Studio is an intelligent code assistant that leverages Large Language Models (LLMs) to help users generate, debug, explain, optimize, and analyze code efficiently. This project demonstrates the practical integration of AI in software development workflows.

---

## 📌 Problem Statement

Developers often spend significant time writing, debugging, and understanding code. Beginners face difficulty in learning programming concepts, while professionals need faster solutions.

This project aims to solve these challenges by providing an AI-powered assistant that simplifies coding tasks.

---

## 🎯 Objectives

- Automate code generation from natural language prompts  
- Assist in debugging and fixing errors  
- Provide clear explanations for better understanding  
- Optimize code for performance improvements  
- Analyze time and space complexity  

---

## 💡 Key Features

### 🔹 Code Generation
Generate clean and structured code from user prompts.

### 🔹 Debugging Support
Identify and fix errors in user-provided code.

### 🔹 Code Explanation
Explain code logic in simple and understandable language.

### 🔹 Code Optimization
Improve efficiency and readability of code.

### 🔹 Complexity Analysis
Analyze time and space complexity (Big-O notation).

### 🔹 Chat History
Stores previous inputs and outputs for better usability.

### 🔹 Example Prompts
Provides sample queries to guide users.

### 🔹 Download Option
Allows users to download generated code.

---

## 🛠️ Tech Stack

| Component        | Technology Used |
|----------------|----------------|
| Frontend        | Streamlit |
| Backend         | Python |
| AI Model        | Groq API (LLaMA 3.1) |
| Environment     | Python-dotenv |
| Version Control | GitHub |

---

## 🧱 System Architecture
User Input → Streamlit UI → Backend (utils.py) → Groq API → Response → UI Display
ai_code_studio/
│── app.py # Streamlit UI
│── utils.py # Backend logic (LLM calls)
│── requirements.txt # Dependencies
│── .env # API keys (not uploaded)
│── README.md # Project documentation

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Setup Environment Variables
Create a `.env` file:GROQ_API_KEY=your_api_key_here

### 4️⃣ Run Application
streamlit run python app.py

---

## 🖥️ Application Workflow

1. User selects a feature (Generate, Debug, Explain, Optimize, Analyze)
2. User enters input (code or prompt)
3. Request is sent to backend (`utils.py`)
4. Backend calls Groq API
5. Response is processed and displayed in UI

---

## 🔐 Security Considerations

- API keys are stored using `.env` file  
- Sensitive data is not exposed in GitHub  
- Environment variables ensure secure access  

---

## ⚠️ Limitations

- Depends on API availability  
- May generate incorrect or incomplete code  
- Limited context understanding for very large projects  

---

## 🚀 Future Enhancements

- ChatGPT-style conversational interface  
- Code execution environment (sandbox)  
- User authentication system  
- Deployment as a web application  
- Fine-tuned models for better accuracy  

---

## 📸 Screenshots

*(Add screenshots of your UI here)*

---

## 📊 Use Cases

- Students learning programming  
- Developers debugging code  
- Rapid prototyping  
- Interview preparation  

---

## 👨‍💻 Author

**Sanjay Ande**  
Artificial Intelligence & Machine Learning Student  

---

## ⭐ Acknowledgements

- Groq API for LLM access  
- Streamlit for UI framework  

---

## 📌 Conclusion

AI Code Studio demonstrates how artificial intelligence can significantly enhance developer productivity by automating repetitive coding tasks and improving code understanding.

---

## ⭐ If you like this project, consider giving it a star!
