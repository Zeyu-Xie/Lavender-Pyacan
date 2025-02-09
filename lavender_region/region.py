import pandas as pd
import os

csv_path = os.path.join(os.path.dirname(__file__), "regions.csv")
df = pd.read_csv(csv_path, dtype={"Telephone Area Code": str})


class Region:
    def __init__(
        self,
        index=None,
        name=None,
        flag=None,
        country_code=None,
        capital=None,
        state=None,
        telephone_area_code=None,
        internet_domain=None,
    ):
        if index is not None:
            self.index = index
        elif name is not None:
            index_list = df[df["Name"] == name].index
            if len(index_list) == 0:
                raise ValueError(f"No region found with name '{name}'")
            self.index = index_list[0]
        elif flag is not None:
            index_list = df[df["Flag"] == flag].index
            if len(index_list) == 0:
                raise ValueError(f"No region found with flag '{flag}'")
            self.index = index_list[0]
        elif country_code is not None:
            index_list = df[df["Country Code"] == country_code].index
            if len(index_list) == 0:
                raise ValueError(f"No region found with country code '{country_code}'")
            self.index = index_list[0]
        elif capital is not None:
            index_list = df[df["Capital"] == capital].index
            if len(index_list) == 0:
                raise ValueError(f"No region found with capital '{capital}'")
            self.index = index_list[0]
        elif state is not None:
            index_list = df[df["State"] == state].index
            if len(index_list) == 0:
                raise ValueError(f"No region found with state '{state}'")
            self.index = index_list[0]
        elif telephone_area_code is not None:
            index_list = df[df["Telephone Area Code"] == telephone_area_code].index
            if len(index_list) == 0:
                raise ValueError(
                    f"No region found with telephone area code '{telephone_area_code}'"
                )
            self.index = index_list[0]
        elif internet_domain is not None:
            index_list = df[df["Internet Domain"] == internet_domain].index
            if len(index_list) == 0:
                raise ValueError(
                    f"No region found with internet domain '{internet_domain}'"
                )
            self.index = index_list[0]
        else:
            raise ValueError("Either index or name must be provided")

        self.name = df.iloc[self.index]["Name"]
        self.flag = df.iloc[self.index]["Flag"]
        self.country_code = df.iloc[self.index]["Country Code"]
        self.capital = df.iloc[self.index]["Capital"]
        self.state = df.iloc[self.index]["State"]
        self.telephone_area_code = df.iloc[self.index]["Telephone Area Code"]
        self.internet_domain = df.iloc[self.index]["Internet Domain"]

    def __str__(self):
        str = f"Name: {self.name}\nFlag: {self.flag}\nCountry Code: {self.country_code}\nCapital: {self.capital}\nState: {self.state}\nTelephone Area Code: {self.telephone_area_code}\nInternet Domain: {self.internet_domain}"
        return str
