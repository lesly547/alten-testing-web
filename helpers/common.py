import csv
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

results = []


def create_screenshots(context, name_image):
    logging.info('Init save screenshot ' + name_image)
    context.driver.save_screenshot("screenshots/" + name_image)
    logging.info('End save screenshot ' + name_image)


def save_results(name, result, description_error):
    result = {
        'name': name, 'result': result, 'description_error': description_error
    }
    results.append(result)


def save_csv(name):
    logging.info('Init Create report ' + name)
    with open('reports/'+name, 'w', newline='') as file_csv:
        fields = ['name', 'result', 'description_error']
        writer_csv = csv.DictWriter(file_csv, fieldnames=fields)
        writer_csv.writeheader()
        for result in results:
            writer_csv.writerow(result)
    logging.info('End Create report ' + name)
