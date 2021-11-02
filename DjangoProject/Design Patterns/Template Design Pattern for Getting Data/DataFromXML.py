from DataFromFiles import DataFromFiles


class DataFromXML(DataFromFiles):

    def get_age(self) -> None:
        print("get the value from tag <age>")

    def get_bloodpressure(self) -> None:
        print("get the value from tag <bloodpressure>")
