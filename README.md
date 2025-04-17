# 📝 **Automated Grading System using EasyOCR and Semantic Similarity** 🚀

## 🎯 Project Overview

Welcome to the **Automated Grading System** – a cutting-edge solution that automates the grading process for handwritten student answers! This web-based application leverages **EasyOCR** to extract text from scanned answer sheets, **TextBlob** for spelling correction, and **Sentence Transformers** for advanced semantic similarity comparison. By comparing the student's answer to the model answer, the system generates a similarity score, which is then used to calculate the final grade – all while supporting customizable weightage for each question. 📊

Say goodbye to manual grading! This tool helps teachers streamline the grading process, reduce errors, and focus on what truly matters: personalized feedback and teaching. 🎓

---

## 🌟 Key Features

- **OCR Text Extraction**: Harnessing the power of EasyOCR to extract text from scanned answer sheet images.
- **Spelling Correction**: Automatic error-free text, thanks to **TextBlob**'s spell-checking capabilities.
- **Semantic Similarity**: Compare the student’s answer to the model answer using **SentenceTransformers**, providing a much more accurate measure than simple keyword matching.
- **Flexible Grading**: Enter the total weightage for each question, and let the system adjust the final grade accordingly, ensuring fairness and accuracy.

---

## 💻 Tech Stack

- **Python**: The language behind the magic.
- **EasyOCR**: For text extraction from images – no more manual transcription!
- **Streamlit**: A seamless way to create and interact with the app through a user-friendly interface.
- **SentenceTransformers**: Leverages powerful embeddings to understand semantic meaning and compare answers.
- **TextBlob**: Fixing spelling errors and making sure everything reads perfectly.
- **NumPy & PIL**: For efficient image processing and manipulation.

---

## 🚀 Implementation Steps

### 1. **Set Up Your Environment**

First, clone the repository and install all the required dependencies:

```bash
git clone https://github.com/your-username/automated-grading-system.git
cd automated-grading-system
pip install -r requirements.txt
```

This will install all the libraries you'll need, including Streamlit, EasyOCR, and SentenceTransformers.

### 2. **Launch the Application**

Now you're ready to launch the app! Run the following command to start your local server:

```bash
streamlit run app.py
```

Your browser will open the application, and you can begin uploading images and testing out the grading system.

### 3. **Upload an Answer Sheet**

In the app, upload a scanned image of a student’s answer sheet (formats: PNG, JPG, JPEG). The system will automatically process and extract the text using OCR.

### 4. **Enter the Model Answer**

Once the text is extracted, input the **model answer** for that specific question into the provided text box. This will be used as the benchmark for comparison.

### 5. **Evaluate and Grade**

Click "Evaluate," and let the system work its magic. The app will compare the extracted student answer to the model answer using semantic similarity, correct any spelling mistakes, and then calculate the final grade based on the similarity score and the weightage you specify.

---

## 🔍 How the Grading Process Works

1. **Text Extraction**: Upload the answer sheet, and EasyOCR extracts the handwritten content.
2. **Spelling Correction**: TextBlob fixes any OCR errors in the extracted content, ensuring clean text.
3. **Semantic Similarity**: The corrected answer is compared to the model answer using **SentenceTransformers**, which calculates a semantic similarity score.
4. **Grading**: The final grade is calculated based on the similarity score, weighted by the value you assign to the question.

The output includes:
- **Corrected Student Answer**: See the OCR text after spelling corrections.
- **Similarity Score**: A percentage that indicates how closely the student's answer matches the model answer.
- **Marks Scored**: The final score, adjusted for the weightage of the question.

---

## 💡 Example Use Case

Imagine you're grading 100 assignments. With this system, you can upload the answer sheets, input the model answers, set the question weightage, and hit "Evaluate." The system does the rest, providing you with immediate feedback on each student's performance, including a similarity score and the final marks.

---

## ✨ Future Enhancements

While the current version of the app is highly functional, we have exciting plans for future improvements:

- **Multi-Language Support**: Extend OCR and NLP capabilities to support multiple languages, making the system global-ready.
- **Handwriting Recognition**: Enhance text extraction to better recognize and grade handwritten answers.
- **Database Integration**: Store results, track student progress, and generate reports over time.
- **Faster Performance**: Optimizing OCR and similarity calculations to make grading quicker, especially for larger documents.

---

## 📑 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 🙏 Acknowledgements

- **EasyOCR**: The fantastic OCR tool for text extraction.
- **TextBlob**: The go-to library for correcting spelling mistakes and making text read beautifully.
- **SentenceTransformers**: Cutting-edge semantic similarity technology that takes text understanding to the next level.

---

## 🤝 Contributing

We welcome contributions! If you have an idea for a feature or bug fix, feel free to fork the repository, create an issue, or submit a pull request. We’d love to collaborate and improve this project further!

---

## 📬 Contact

Have any questions? Feel free to open an issue, or contact the project maintainer directly at `your-email@example.com`.

---

### Ready to automate your grading? Try the **Automated Grading System using OCR** today and revolutionize the way you grade! 🚀

---

This version is crafted to be more engaging, making it easier for users to understand the purpose of the project, the tech behind it, and how to use it. The addition of emojis, creative language, and structure should make the README stand out and encourage more users and contributors.
