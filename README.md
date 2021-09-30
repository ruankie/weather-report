# (PROJECT IN PROGRESS)

# Details
Based on [this](https://towardsdatascience.com/introduction-to-papermill-2c61f66bea30) tutorial on Towards Data Science (updated for September 2021). The notebooks forecast temperature and rain volume and saves a `.pdf` report. In each notebook, the relevant city is used as a parameter so notebooks can be executed independently. This tutorial is for learning how to use the [papermill](https://papermill.readthedocs.io/en/latest/index.html) library for python that is used to parameterise jupyter notebooks.

# Setup
This tutorial uses some specific packages to forecast weather (`pyowm`), parameterise notebooks (`papermill`), and create .pdf files (`pdfkit`). Create a separate virtual environment for this project by running the following:

```console
conda create -n papermill-weather python=3.7
conda activate papermill-weather
pip install -r requirements.txt
```