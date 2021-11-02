from DataFromFiles import DataFromFiles


class DataFromCSV(DataFromFiles):

    def get_age(self) -> None:
        print("get the second value, which is age")

    def get_bloodpressure(self) -> None:
        print("get the third value, which is blood pressure")
