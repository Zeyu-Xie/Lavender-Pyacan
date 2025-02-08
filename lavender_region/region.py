import pandas as pd
import os

csv_path = os.path.join(os.path.dirname(__file__), 'regions.csv')
df = pd.read_csv(csv_path)

class Region:

    def __init__(self, name):
        self.name = name