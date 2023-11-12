<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>NLP_PROJECT</h1>
<h3>◦ HTTPStatus Exception: 401</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat-square&logo=Jupyter&logoColor=white" alt="Jupyter" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />
</p>
<img src="https://img.shields.io/github/license/IsaureStiffel/nlp_project?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/IsaureStiffel/nlp_project?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/IsaureStiffel/nlp_project?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/IsaureStiffel/nlp_project?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 The Dataset](#-the-dataset)
- [📂 repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running nlp_project](#-running-nlp_project)
- [🤝 Conclusion](#-conclusion)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

This is a NLP project for the EPF 5th year class. This is for me an introduction to the subject where I discovered how to manage this kind of project and the different necessary steps. The main goal of this project is to learn and explore different Machine Learning and Deep Learning models. 

It is based on a [Book Genre Prediction](#-https://www.kaggle.com/datasets/athu1105/book-genre-prediction/data) dataset from the plateform Kaggle. The goal is to analyze thanks to NLP the summary of books and classify them by their genre. 

This project is composed of three notebooks and one python script. 

---

## 📦 The Dataset

The dataset is composed of 4542 differents book summaries that are classified in 10 different genre : 'fantasy', 'science', 'crime', 'history', 'horror', 'thriller', 'psychology', 'romance', 'sports', 'travel'. 

We are also given the titles of the book but after some research the names were not relevant enough to be added to our model. We are only using the 'summary' column to classify the books. 
As a target we choose the 'genre' column. 

---


## 📂 Repository Structure

```sh
└── nlp_project/
    ├── notebook1_exploration.ipynb
    ├── notebook2_classification.ipynb
    ├── notebook3_ML.ipynb
    └── preprocessing.py

```

---


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                                                    | Summary                   |
| ---                                                                                                                     | ---                       |
| [notebook1_exploration.ipynb](https://github.com/IsaureStiffel/nlp_project/blob/main/notebook1_exploration.ipynb)       | Exploration of the dataset and decision on the preprocessing part|
| [notebook2_classification.ipynb](https://github.com/IsaureStiffel/nlp_project/blob/main/notebook2_classification.ipynb) | First classification and exploration of ML models |
| [notebook3_ML.ipynb](https://github.com/IsaureStiffel/nlp_project/blob/main/notebook3_ML.ipynb)                         | Improvement of the ML model and first attempts at DL|
| [preprocessing.py](https://github.com/IsaureStiffel/nlp_project/blob/main/preprocessing.py)                             | Preprocessing function |

</details>

---

## 🚀 Getting Started

***Dependencies***

### 🔧 Installation

1. Clone the nlp_project repository:
```sh
git clone https://github.com/IsaureStiffel/nlp_project
```

2. Change to the project directory:
```sh
cd nlp_project
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Running nlp_project

```sh
jupyter nbconvert --execute notebook.ipynb
```

---

## 🤝 Conclusion

This project was a first step in NLP world and helped me a lot with understanding better Machine Learning and Deep Learning. First we learned about how to preprocess the text and vectorize it to be understand by the model. Then we made the classification and tried to explore the errors and the different results to improve them. Finally we improved the model and tried some model of Deep Learning that are not as efficient as we would want for the moment but will be imporved in the future. 

The main challenge I encoutered during this project is the imbalanced classes, so I had to deal with a lot of underfitting. As a solution I tried to do some Oversampling on the datas wich improved the model a little bit. I also started to try weighted classes but had difficulties implementing it in my model, it is surely some improvement I will do in the future. 

For the Deep Learning part, I tried a lot of different models and a lot of Neural Networks, I had trouble applying them correctly to my model so they are not efficient for the moment. With some deeper research on the hyperparameters and the different layer I could apply, I will also improve it in the futur. 

## 👏 Acknowledgments

Thank you to [Ryan Pegoud](#-https://github.com/RPegoud) for this class, I learned a lot of thing. 

[**Return**](#Top)

---

