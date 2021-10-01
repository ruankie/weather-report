# Details
This repository is an updated version of [this](https://towardsdatascience.com/introduction-to-papermill-2c61f66bea30) tutorial on Towards Data Science (for September 2021) that produces a five-day temperature forecast for different cities. The following changes were made:
> 1. Incorporates new API calls - the older ones no loger work.
> 2. Incorporates parallel processing so that forecasts can be made of different cities at the same time.
> 3. Does not produce `.pdf` report files for forecasts - graphs produced in `.png` image format instead.

 The template notebook is used to forecast temperature for the next five days. In each slave notebook, the relevant city name is injected as a parameter so notebooks can be executed independently and in parallel. This also allows each slave notebook to function as a kind of report for a particular city where all the code and results are contained in the same file. 

 This repository can be used for learning how to use the [papermill](https://papermill.readthedocs.io/en/latest/index.html) library that is used to parameterise jupyter notebooks. It can als be used a guide to see how different parameterised notebooks can be executed in parallel using the [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) library for more efficient use of computer resources.

# Setup and Execution
1. This repository uses some specific packages to forecast weather (`pyowm`) and parameterise notebooks (`papermill`). Create a separate virtual environment with all the relevant packages for this project by running the following from your terminal:

```console
conda create -n papermill-weather python=3.7
conda activate papermill-weather
pip install -r requirements.txt
```

2. You will also have to create your own profile and generate a free API key on the [Open Weather Map](https://openweathermap.org/appid) website.

3. When your environment and API keys are set up as in step `1.` and `2.`, you can proceed to choose the cities you want temperature forecasts for by filling the dictionary in the `forecast_template.ipynb` notebook file. Give each city a name along with its longitude and latitude coordinates in decimal format.

4. Assign your own API key that you created in step `2.` to the `api_key` variable inside the `forecast_template.ipynb` notebook file **OR** create a file called `my_api_key.py` in the root directory of this repository and create a variable called `api_key` inside it with the value of your API key assigned to it. For the second option, you will need to import your API key from your `my_api_key.py` file into the `forecast_template.ipynb` notebook.

5. Finally, update the `cities` list inside `parallel_forecast.py` file with your city names and start the parallel forecasts from you terminal by running the following command:
```console
python parallel_forecast.py
```

# Results
> Your temperature forecasts (min, max, and day average) will be saved to plots in the `figures` folder. <br>
> The slave notebooks will be contained in the `slave_notebooks` folder.