import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path


time_now = dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results/'
FILE_NAME = f'status_summary_{time_now}.csv'


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(
            self.results_dir / FILE_NAME,
            mode='w', newline='', encoding='utf-8'
        ) as f:

            writer = csv.writer(f, dialect='unix')
            data = (
                ('Статус', 'Количество'),
                *sorted(self.results.items()),
                ('Всего', sum(self.results.values())),
            )
            writer.writerows(data)
