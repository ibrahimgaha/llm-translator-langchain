
# Technical Report: AI Translator with LangChain

## 1. Introduction

The objective is to develop an AI-powered application that translates
text between languages using a large language model (LLM).

## 2. Problem Statement

Manual translation can be time-consuming, while conventional
translation systems may struggle with context, tone, and idioms.

This project explores the use of prompt engineering and LLM integration
to produce context-aware translations.

## 3. Architecture

The application has three main layers:

1. User interface: Streamlit collects the text and language choices.
2. Translation logic: translator.py validates input and builds a
   LangChain processing chain.
3. Language model: ChatOpenAI generates the translation.

The chain consists of a prompt template, a chat model, and an output
parser.

## 4. Implementation

ChatPromptTemplate defines the translation instructions.

ChatOpenAI connects to the configured language model.

StrOutputParser extracts the generated text as a string.

The validation function rejects empty text, unsupported languages,
and identical source and target languages.

Streamlit presents the application through a web interface.

## 5. Testing Strategy

Automated tests cover:
- Supported languages
- Empty input
- Whitespace-only input
- Identical source and target languages
- Unsupported languages
- Valid input

Real-model tests should separately evaluate translation quality.

## 6. Demonstration Plan

Test English-to-French translation with a simple sentence.

Test French-to-English translation with a short paragraph.

Test English-to-Arabic translation.

Test an empty input and identical source and target languages.

Record actual outputs and any observed errors during execution.

## 7. Results

Complete this section after executing the application.

Record the test results, sample translations, response times,
and any observed translation errors.

Do not report unexecuted tests as successful.

## 8. Limitations

Translation quality may vary depending on context, dialect, ambiguity,
and model capabilities. The application requires a configured model
provider and internet access when using a hosted model.

Automated input tests do not establish translation accuracy.

## 9. Future Improvements

- Automatic language detection
- Translation quality metrics and human evaluation
- Support for additional model providers
- Caching and improved error handling
- Translation history and document processing

## 10. Conclusion

This project demonstrates how LangChain can connect prompt templates,
language models, and output parsing to build a practical translation
application.
