import streamlit as st
from utils import generate_code, debug_code, explain_code, optimize_code, analyze_complexity

# Page config
st.set_page_config(page_title="AI Code Studio", layout="wide")

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Custom CSS (Blue + White Theme)
st.markdown("""
<style>
.main {
    background-color: #f5f9ff;
}
.title {
    font-size: 40px;
    font-weight: bold;
    color: #0066ff;
}
.subtitle {
    color: #555;
}
.stButton>button {
    background: linear-gradient(90deg, #0066ff, #00c6ff);
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
}
textarea {
    border-radius: 10px !important;
    border: 1px solid #ccc !important;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">🚀 AI Code Studio</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Generate • Debug • Optimize • Explain Code with AI</div>', unsafe_allow_html=True)

st.divider()

# Layout
col1, col2 = st.columns([1, 2])

# Sidebar (features)
with col1:
    st.subheader("⚙️ Features")

    option = st.radio(
        "Select Tool",
        ["Generate Code", "Debug Code", "Explain Code", "Optimize Code", "Analyze Complexity"]
    )

    st.divider()

    # Example prompts
    st.subheader("💡 Example Prompts")
    examples = [
        "Write Python code for binary search",
        "Debug this code: for i in range(5 print(i)",
        "Explain quicksort algorithm",
        "Optimize this code: nested loops example"
    ]

    for ex in examples:
        if st.button(ex):
            st.session_state.example = ex

# Main input
with col2:
    st.subheader("💻 Enter your code / prompt")

    user_input = st.text_area(
        "",
        height=200,
        placeholder="Type your prompt here...",
        value=st.session_state.get("example", "")
    )

    if st.button("🚀 Run AI"):
        if user_input.strip() == "":
            st.warning("Please enter something!")
        else:
            with st.spinner("Thinking... 🤖"):
                if option == "Generate Code":
                    output = generate_code(user_input)
                elif option == "Debug Code":
                    output = debug_code(user_input)
                elif option == "Explain Code":
                    output = explain_code(user_input)
                elif option == "Optimize Code":
                    output = optimize_code(user_input)
                elif option == "Analyze Complexity":
                    output = analyze_complexity(user_input)

            st.success("✅ Done!")

            st.subheader("📄 Output")
            st.code(output, language="python")

            # Save to history
            st.session_state.history.append({
                "type": option,
                "input": user_input,
                "output": output
            })

            # Copy + Download
            st.download_button("📥 Download Code", output, file_name="output.py")

# 🔥 Chat History Section
st.divider()
st.subheader("🕘 History")

if st.session_state.history:
    for item in reversed(st.session_state.history):
        st.markdown(f"### 🔹 {item['type']}")
        st.code(item["input"])
        st.code(item["output"], language="python")
else:
    st.info("No history yet. Run something!")