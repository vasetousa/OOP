import datetime

class DVD:

    def __init__(self, name: str, id: int, creation_year: int,
                 creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @staticmethod
    def int2mont(month: int):
        mnt_str = datetime.date(1900, int(month), 1).strftime("%B")
        return mnt_str

    @classmethod
    def from_date(cls, dvd_id: int, name: str, date: str, age_restriction: int):
        date, month, year = date.split('.')
        mon = cls.int2mont(int(month))
        return cls(name, dvd_id, int(year), mon, age_restriction)

    def __repr__(self):
        status = 'rented' if self.is_rented else 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} " \
               f"{self.creation_year}) has age restriction" \
               f" {self.age_restriction}. Status: {status}"