from Protocol.CriptosSistemPaillier import CriptosistPaillier
from users.file_helper import read_paillier_setup
from users.models import Patient


class PatientsRepository:
    def add_patients(self, patients):
        n, g, random_seed, s, shares, delta_patrat = read_paillier_setup()
        obiect = CriptosistPaillier()
        print(n, g, random_seed, s, shares, delta_patrat)
        for patient_dto in patients:
            patient_data = {
                'first_name': patient_dto.first_name,
                'last_name': patient_dto.last_name,
                'age': str(obiect.criptarePaillier(patient_dto.age, n, g, random_seed, s)),
                'age_bit_length': int.bit_length(patient_dto.age),
                'weight': str(obiect.criptarePaillier(patient_dto.weight, n, g, random_seed, s)),
                'weight_bit_length': int.bit_length(patient_dto.weight),
                'height': str(obiect.criptarePaillier(patient_dto.height, n, g, random_seed, s)),
                'height_bit_length': int.bit_length(patient_dto.height),
                'hospital': patient_dto.hospital
            }

            print(str(patient_dto.age) + ' ' + str(patient_dto.height) + ' ' + str(patient_dto.weight))
            Patient.objects.create(**patient_data)

    def get_patients(self, hospitals):
        patients = []
        for hospital in hospitals:
            patients_from_hospital = list(Patient.objects.filter(hospital=hospital))
            patients += patients_from_hospital
        return patients

    def get_attribute_values(self, patients, attribute):
        attribute_values = []
        bitlengths = []
        for patient in patients:
            print("Patient is ", patient)
            if attribute == "Age":
                attribute_values.append(int(patient.age))
                print("Age of patient is", patient.age)
                bitlengths.append(patient.age_bit_length)
            elif attribute == "Weight":
                attribute_values.append(int(patient.weight))
                bitlengths.append(patient.weight_bit_length)
            elif attribute == "Height":
                attribute_values.append(int(patient.height))
                bitlengths.append(patient.height_bit_length)
        return attribute_values, bitlengths

    def get_hospitals_attributes(self):
        hospitals = Patient.objects.values('hospital').distinct()
        response = []
        fields = ["Age", "Height", "Weight"]
        for hospital in hospitals:
            hospital_with_attributes = {
                "name": hospital['hospital'],
                "fields": fields
            }
            response.append(hospital_with_attributes)
        print(response)
        return response
