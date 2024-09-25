import csv
import datetime as dt
from collections import defaultdict


time_now = dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
BASE_DIR = 'results/'
FILE_NAME = f'status_summary_{time_now}.csv'


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):

        with open(
            f'{BASE_DIR}/{FILE_NAME}',
            mode='w', newline='', encoding='utf-8'
        ) as f:
            fieldnames = ['Статус', 'Количество']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for status, count in self.results.items():
                writer.writerow(
                    {'Статус': status, 'Количество': count}
                )
            writer.writerow(
                {'Статус': 'Total', 'Количество': sum(self.results.values())}
            )
