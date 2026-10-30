
import streamlit as st
from dotenv import load_dotenv

from translator import (
    SUPPORTED_LANGUAGES,
    translate_text,
    validate_translation_input,
)

# Load NVIDIA API key from .env
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Translator | LangChain",
    page_icon="🌍",
    layout="centered",
)

# Custom styling
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        max-width: 850px;
    }

    h1 {
        text-align: center;
    }

    .subtitle {
        text-align: center;
        color: #888;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.title("🌍 AI Language Translator")

st.markdown(
    '<p class="subtitle">'
    'Powered by LangChain & NVIDIA Riva Translate V2'
    '</p>',
    unsafe_allow_html=True,
)

st.divider()

# Language selection
languages = list(SUPPORTED_LANGUAGES.keys())

col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "🌐 Source Language",
        languages,
        index=languages.index("English"),
    )

with col2:
    target_language = st.selectbox(
        "🎯 Target Language",
        languages,
        index=languages.index("French"),
    )

# Input text
text_to_translate = st.text_area(
    "✍️ Enter text to translate",
    placeholder="Type your text here...",
    height=180,
)

# Translate button
if st.button(
    "✨ Translate",
    type="primary",
    use_container_width=True,
):
    try:
        validate_translation_input(
            text_to_translate,
            source_language,
            target_language,
        )

        with st.spinner("Translating with NVIDIA Riva..."):
            translated_text = translate_text(
                text=text_to_translate,
                source_language=source_language,
                target_language=target_language,
            )

        # Save translation in session state
        st.session_state["translation"] = translated_text
        st.session_state["source_text"] = text_to_translate
        st.session_state["source_language"] = source_language
        st.session_state["target_language"] = target_language

    except ValueError as error:
        st.warning(str(error))
        st.session_state.pop("translation", None)

    except Exception as error:
        st.error(
            "Translation failed. Check your NVIDIA API "
            "connection and selected language pair."
        )
        st.session_state.pop("translation", None)

# Display translation
if "translation" in st.session_state:

    st.divider()
    st.subheader("✅ Translation Result")

    st.text_area(
        "Translated Text",
        value=st.session_state["translation"],
        height=180,
    )

    st.download_button(
        label="📥 Download Translation",
        data=st.session_state["translation"],
        file_name="translation.txt",
        mime="text/plain",
        use_container_width=True,
    )

# Sidebar
with st.sidebar:
    st.header("⚙️ About This Project")

    st.markdown(
        """
        **Project:** AI Translator

        **Framework:** LangChain

        **AI Model:** NVIDIA Riva Translate 4B Instruct V2

        **Interface:** Streamlit

        **Language:** Python
        """
    )

    st.divider()

    st.info(
        "This application uses LangChain to execute "
        "a translation workflow powered by NVIDIA's API."
    )

    st.caption("LLM Assignment — Project 1")
