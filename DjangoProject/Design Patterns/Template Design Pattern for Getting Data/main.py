from DataFromCSV import DataFromCSV
from DataFromFiles import DataFromFiles
from DataFromXML import DataFromXML


def client_code(abstract_class: DataFromFiles) -> None:
    abstract_class.template_method()


if __name__ == "__main__":
    print("Get values from a CSV file")
    client_code(DataFromCSV())
    print("")

    print("Get values from a XML file")
    client_code(DataFromXML())
