import csv
import datetime as dt
from pprint import pprint
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from sqlalchemy import create_engine, Column, Date, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()


class PepParse(Base):
    __tablename__ = 'pep'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(20))


class PepParsePipeline:

    def open_spider(self, spider):
        engine = create_engine('sqlite:///sqlite.db')
        Base.metadata.create_all(engine)
        self.session = Session(engine)

    def process_item(self, item, spider):
        pep = PepParse(
            number=item['number'],
            name=item['name'],
            status=item['status'],
        )
        self.session.add(pep)
        self.session.commit()
        return item

    def close_spider(self, spider):
        all_peps = dict(
            self.session.query(
                PepParse.status, func.count(PepParse.id)
            ).group_by(PepParse.status).all()
        )

        with open(
            'results/status_summary_%(time)s.csv',
            mode='w', newline='', encoding='utf-8'
        ) as f:
            fieldnames = ['Статус', 'Количество']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for status, count in all_peps.items():
                writer.writerow(
                    {'Статус': status, 'Количество': count}
                )
            writer.writerow(
                {'Статус': 'Total', 'Количество': sum(all_peps.values())}
            )

        self.session.close()
