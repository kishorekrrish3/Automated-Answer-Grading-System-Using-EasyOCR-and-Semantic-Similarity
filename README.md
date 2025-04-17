### GitHub Project Title:
**Automated Answer Grading System Using OCR and Semantic Similarity**

### README.md

```markdown
# Automated Answer Grading System Using OCR and Semantic Similarity

This project implements an automated grading system for answer sheets using Optical Character Recognition (OCR) and semantic text similarity. The system extracts text from uploaded images of student answer sheets, performs spelling correction, and compares the extracted answers with a reference (model) answer using sentence embeddings. It then calculates a similarity score, converts it into a percentage, and evaluates the score (out of 10).

## Features

1. **OCR Text Extraction**: Extracts text from images of handwritten or typed answer sheets.
2. **Spelling Correction**: Automatically corrects spelling errors in the extracted text.
3. **Semantic Similarity Calculation**: Uses a pre-trained transformer model (SentenceTransformer) to calculate the semantic similarity between the student's answer and the reference answer.
4. **Automated Scoring**: Scores the student's answer based on the calculated similarity, scaling it to a 10-point scale.
5. **Interactive UI**: Streamlit-based interface that allows users to upload images, view the extracted text, and see the evaluation results.

## Technologies Used

- **EasyOCR**: For optical character recognition to extract text from images.
- **Sentence Transformers**: For semantic text similarity using pre-trained models.
- **TextBlob**: For spelling correction.
- **Streamlit**: For building the user interface.
- **PIL** (Python Imaging Library): For image handling and display.
- **NumPy**: For numerical operations and image processing.

## Setup

### Prerequisites

Make sure you have Python 3.x installed and pip for package management.

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/automated-answer-grading-ocr.git
   cd automated-answer-grading-ocr
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Once the app is running, open your browser and go to `http://localhost:8501` to access the application.

## How It Works

1. **Upload Image**: The user uploads an image file containing the student's answer sheet.
2. **OCR Processing**: The OCR engine extracts the text from the image.
3. **Spelling Correction**: The extracted text is processed for spelling corrections using TextBlob.
4. **Answer Comparison**: The corrected text is compared with the reference (model) answer using semantic similarity techniques based on the pre-trained model (`SentenceTransformer`).
5. **Evaluation**: The system calculates the similarity score, converts it to a percentage, and generates the final score (out of 10).

## Streamlit UI Elements

- **File Uploader**: For uploading the answer sheet image.
- **Text Area**: For entering the reference (model) answer.
- **Evaluate Button**: Triggers the evaluation process after uploading the answer and entering the model answer.
- **Results**: Displays the corrected student answer, similarity percentage, and the final score.

## Example Usage

1. Upload an image of the answer sheet.
2. Enter the reference (model) answer in the text area.
3. Click the "Evaluate" button.
4. View the extracted text, similarity percentage, and final score.

## Contributing

If you would like to contribute to this project, feel free to fork the repository, create a branch, and submit a pull request. You can also report issues or suggest new features by opening an issue in the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **EasyOCR**: For text extraction from images.
- **SentenceTransformers**: For semantic similarity calculations.
- **TextBlob**: For spelling correction.

---

Happy grading! 🎓
```

### Notes:
1. **Streamlit App**: The file `app.py` is assumed to be the main application file where the Streamlit interface and logic for grading are implemented.
2. **Installation**: Instructions for setting up the environment using `pip` and the necessary dependencies (`requirements.txt`).
3. **Contributing**: Encourages others to contribute to the project, submit issues, or suggest features.

Let me know if you need further modifications!
