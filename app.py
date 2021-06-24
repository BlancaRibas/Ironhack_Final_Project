{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6cac6004",
   "metadata": {},
   "source": [
    "#### Streamlit code "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f2eb396",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import libraries\n",
    "import streamlit as st\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from PIL import Image\n",
    "from google_currency import convert\n",
    "import pandas as pd\n",
    "import requests\n",
    "import cv2\n",
    "from streamlit_functions import *\n",
    "import json\n",
    "import os\n",
    "import pytesseract\n",
    "st.markdown('**Convert currencies from pictures!**:sunglasses:')\n",
    "\n",
    "#create slide bars for user to select currency to convert\n",
    "st.sidebar.markdown('**Input options**:rocket:')\n",
    "currency_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS',\n",
    "                 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD',\n",
    "                 'THB', 'TRY', 'USD', 'ZAR']\n",
    "\n",
    "input_price = st.sidebar.selectbox('Select base currency', currency_list)\n",
    "if len(input_price) == 0 or input_price == \"Select base currency\":\n",
    "    st.write(\"Please select currency\")\n",
    "\n",
    "output_price = st.sidebar.selectbox('Select target currency', currency_list)\n",
    "if len(output_price) == 0 or output_price == \"Select target currency\":\n",
    "    st.write(\"Please select currency\")\n",
    "\n",
    "#create a sidebar for user to upload image\n",
    "uploaded_file = st.sidebar.file_uploader(\" Upload image\", type = ['jpeg', 'jpg', 'png'])\n",
    "\n",
    "#insert pytesseract to read image\n",
    "if uploaded_file:\n",
    "    #st.write('File successfully uploaded')\n",
    "    img = Image.open(uploaded_file)\n",
    "    img.save('imagenes/a.jpg')\n",
    "  \n",
    "    image1 = cv2.imread('imagenes/a.jpg')\n",
    "    # change image to gray\n",
    "    gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)\n",
    "    # create copy of created image\n",
    "    image_aux = gray.copy()\n",
    "    x=pytesseract.image_to_string(image_aux)\n",
    "    #st.write(x)\n",
    "\n",
    "#print conversion\n",
    "    yas=converter(input_price,output_price,x)\n",
    "    st.write('**Converted!**:money_with_wings:')\n",
    "    st.write(yas)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "clase",
   "language": "python",
   "name": "clase"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
