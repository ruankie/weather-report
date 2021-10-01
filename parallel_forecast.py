import papermill as pm
from multiprocessing import Process
import time

def forecast_city(city_name):
    start = time.time()
    print(f'\t*{city_name} started.')
    city_file_name = city_name.replace(' ','_')
    pm.execute_notebook(
                    input_path='forecast_template.ipynb',
                    output_path=f'slave_notebooks/forecast_{city_file_name}.ipynb',
                    parameters={'CITY':city_name},
                    progress_bar=True,
                   )
    #print(f'{city_name} forecast started.')
    print(f'\tforecast for {city_name} completed in', round(time.time() - start,2), 'seconds.')


if __name__ == '__main__':

	main_start = time.time()

	processes = []
	cities = ['Johannesburg',
            'Berlin', 
            'New York', 
            'Sao Paulo']

	for city in cities:
	    proc = Process(target=forecast_city, args=(city,))
	    processes.append(proc)
	    proc.start()
	    
	for p in processes:
	    p.join()
	    
	print()
	print('all forecasts done in', round(time.time() - main_start,2), 'seconds.')