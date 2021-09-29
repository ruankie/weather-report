# (PROJECT IN PROGRESS)

# Details
From [this](https://towardsdatascience.com/introduction-to-papermill-2c61f66bea30) tutorial on  Towards Data Science. Forecasts temperature and saves to `.pdf` file. This tutorial is for learning how to use the [papermill](https://papermill.readthedocs.io/en/latest/index.html) library for python that is used to parameterise jupyter notebooks.

# Setup
This tutorial uses some specific packages to forecast weather (`pyowm`), parameterise notebooks (`papermill`), and create .pdf files (`pdfkit`). Create a separate virtual environment for this project by running the following:

```console
conda create -n papermill-weather python=3.7
conda activate papermill-weather
pip install -r requirements.txt
```