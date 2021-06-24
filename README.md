# Ironhack Final Project

![bann](https://user-images.githubusercontent.com/82451770/123253820-2dc32200-d4ee-11eb-97f0-1eb67ac46f9a.JPG)
(Bootcamp Data Analytics [ironhack](https://www.ironhack.com/es))

### 💻Introduction:

"255" is a project motivated by the curiosity of how machine learning is able to read and classify pictures as we human beings do.

### 💡 Goal: 

When travelling I always have issues to convert currencies, thus my goal is to create a currency converter based on image recognition. 

I am going to create a product concept which is 255.

### 👾 Process:

#### 1. Number detection
In order to detect numbers of images I have used two models:

  🎈**Convolutional neural network**(CNN). In deep learning,is a class of deep neural network, most commonly applied to analyze visual imagery. I have used 135 csv ***(https://archive.ics.uci.edu/ml/datasets/Character+Font+Images)*** to train my model, which has been the Sequential model. ***(Sequential model is a linear stack of layers. You create a sequential model by calling the keras_model_sequential () function then a series of layer functions)***
  
  🎈**Python-tesseract** is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images. After exploring the CNN I have decided to use the Pytesseract tool, which eases the OCR process.
  
#### 2 . Currency converter
As my main goal is to create a currency converter based on images I have used **google-currency** to do so. It can convert the currency of 153 codes.
  
  ****Disclaimer: google-currency package fetch the result from Google using web scrapping. Owner will not be responsible for any misuse of this package. This is solely for the purpose of learning.****

#### 🕸️Outcome 
 After navigating the data and choosing the best tool to process the images, which have been then converted. I have created a Streamlit app, where you can see 255 product concept. 
  
  🌟Streamlit: http://192.168.97.50:8501/
  


