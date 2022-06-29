#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from sqlalchemy import create_engine


def main():
    engine = create_engine(
        'postgresql://hassan:kopudoju@localhost:5432/prices')

    df = pd.read_csv('src/data.csv')

    df.to_sql(name='prices', con=engine, if_exists='replace')


if __name__ == '__main__':
    main()
