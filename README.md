Here's the full, properly formatted README text including implementation steps, descriptions, and all the required sections:

---

# Automated Grading System using EasyOCR and Semantic Similarity

## Project Overview

"Automated Grading System using OCR" is a web-based application designed to automate the grading of handwritten student answers using Optical Character Recognition (OCR) and Natural Language Processing (NLP). The project utilizes **EasyOCR** to extract text from scanned answer sheets and **Sentence Transformers** for semantic similarity comparison between the student's extracted answer and the model answer. The similarity score is then used to calculate the marks, with flexibility to account for different weightages for each question.

This system simplifies the grading process, reducing human effort and making grading scalable for educators dealing with large batches of handwritten answers.

---

## Key Features

- **OCR Extraction**: Uses EasyOCR to read and extract text from uploaded answer sheet images.
- **Spelling Correction**: Automatic spelling correction using **TextBlob** to ensure accuracy.
- **Semantic Similarity**: Compares the student’s extracted answer with the model answer using the **SentenceTransformers** library.
- **Grading Based on Weightage**: Allows users to set a total weightage for each question, which is used to calculate the final score, scaled based on the similarity score.

---

## Tech Stack

- **Python**: Programming language used for developing the application.
- **EasyOCR**: Optical Character Recognition library for text extraction.
- **Streamlit**: Framework for creating the web-based UI.
- **SentenceTransformers**: For semantic similarity comparison between the student’s answer and the model answer.
- **TextBlob**: For spelling correction.
- **NumPy** and **PIL**: For image processing and manipulation.

---

## Implementation Steps

### 1. **Set Up the Environment**

To start, you need to clone the repository and install the dependencies.

```bash
git clone https://github.com/your-username/automated-grading-system.git
cd automated-grading-system
pip install -r requirements.txt
```

The `requirements.txt` file includes the necessary Python libraries for this project, such as `streamlit`, `easyocr`, `sentence-transformers`, and more.

### 2. **Run the Application**

After installing the dependencies, you can run the application using the following command:

```bash
streamlit run app.py
```

This command will start a local server and open the Streamlit app in your browser, where you can interact with the grading system.

### 3. **Upload an Answer Sheet**

In the app, you will be prompted to upload an image of a student’s answer sheet (in PNG, JPG, or JPEG format). The system will process this image using EasyOCR to extract the text.

### 4. **Enter the Model Answer**

Once the text has been extracted, you will enter the model answer for the corresponding question in the text box. This will serve as the reference for comparison.

### 5. **Evaluation and Grading**

The app calculates the similarity between the extracted student answer and the model answer using the **SentenceTransformers** library. The system then calculates the score based on the similarity and scales it according to the weightage you specify for the question.

---

## How the Grading Process Works

1. **Text Extraction**: The uploaded image of the answer sheet is processed using EasyOCR to extract the raw text.
2. **Spelling Correction**: The extracted text is corrected using **TextBlob** to handle any OCR-related errors in spelling.
3. **Semantic Similarity Calculation**: The corrected text is compared to the model answer using **SentenceTransformers** to compute a semantic similarity score. This score is an indication of how closely the student’s answer matches the model answer.
4. **Grading**: The final score is calculated based on the similarity score, scaled by the weightage you enter for the question.

The result includes:
- **Corrected Student Answer**: The text extracted from the image with spelling errors corrected.
- **Similarity Score**: A percentage value indicating how similar the student’s answer is to the model answer.
- **Marks Scored**: The marks scored out of the total weightage.

---

## Example Use Case

1. **Upload Image**: A scanned answer sheet image (e.g., PNG, JPG).
2. **Enter Model Answer**: Provide the correct model answer for the question.
3. **Set Weightage**: Enter the total marks or weightage for that question (e.g., 20 marks).
4. **Click "Evaluate"**: The system will process the uploaded answer sheet, compare it with the model answer, and calculate the final marks based on similarity.

---

## Future Enhancements

While the current implementation is functional, there are several opportunities for improvement and feature additions, such as:

- **Multi-Language Support**: Extend OCR capabilities to support multiple languages for diverse test environments.
- **Handwriting Recognition**: Integrate handwriting recognition systems for even more accurate grading.
- **Database Integration**: Store historical results and grades in a database for easy reference and analysis.
- **Performance Optimizations**: Speed up the processing time by optimizing the OCR and similarity calculations.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- **EasyOCR**: A powerful tool for Optical Character Recognition.
- **TextBlob**: A simple library for spelling correction and NLP tasks.
- **SentenceTransformers**: A library for generating sentence embeddings and computing semantic similarity.

---

## Contributing

Feel free to fork this repository, create issues, and submit pull requests. Contributions are welcome to help improve the system and add more features. 

---

## Contact

If you have any questions or need help, feel free to open an issue in the repository, or reach out to the project maintainer at `kidkrrish3@gmail.com`.

---

This README provides a comprehensive guide for users and developers on how to set up and use the Automated Grading System, as well as detailed information on the features and how the system works internally.

---

Simply copy and paste this into your `README.md` file in your GitHub repository. This format provides a clear and concise explanation of the project, its usage, and how others can contribute or improve the project further.
