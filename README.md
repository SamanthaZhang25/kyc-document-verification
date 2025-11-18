# Multi-Modal KYC Document Verification with LLMs

## Overview
An intelligent document verification system that automates the validation of KYC documents (ID cards, utility bills) using computer vision and Large Language Models (LLMs). It extracts structured data, validates consistency, and detects potential fraud.

## Key Features
- **Intelligent OCR**: Extracts text from documents using EasyOCR/Tesseract.
- **LLM Validation**: Uses GPT/LLMs to validate logic (e.g., address matching, date consistency).
- **Fraud Detection**: Checks for image manipulation and metadata anomalies.
- **User Interface**: Streamlit-based frontend for uploading and reviewing documents.

## Project Structure
- `src/ocr/`: Optical Character Recognition modules.
- `src/llm/`: LLM integration for reasoning and validation.
- `src/fraud/`: Image forensics and fraud detection logic.
- `frontend/`: Streamlit application code.

## Getting Started

### Prerequisites
- Python 3.10+
- OpenAI API Key (or other LLM provider)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SamanthaZhang25/kyc-document-verification.git
   cd kyc-document-verification
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

### Usage
1. **Start the App**: Launch the Streamlit interface.
   ```bash
   streamlit run frontend/app.py
   ```
2. **Upload Documents**: Use the web interface to upload ID images for verification.
