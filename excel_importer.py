import openpyxl

# pass the excel file to a variable using openpyxl
records = openpyxl.load_workbook('records.xlsx')
worksheet = records.get_sheet_by_name('Sheet1')

# check if individual cells can be read
number = 2
recordID = worksheet['C{}'.format(number)]
# print(recordID.value)

# get the number of records inside the excel file
number_of_rows = worksheet.max_row
print("Found " + str(number_of_rows - 1) + " record(s).")

# textfile = open('test.txt', 'a')

# # iterate over each record
# for row in worksheet['B']:
#     # print(row)
#     # print(row.value)
#     if row.value != 'Payer Name':
#         textfile.write(row.value + '\n')
# textfile.close()

# assign the excel columns to their respective key
# values in a dictionary to generate claims later
test_dict_1 = {
    "RecordID": str(worksheet['A{}'.format(2)].value),
    "PayerName": worksheet['B{}'.format(2)].value
}

test_dict_2 = {
    "RecordID": str(worksheet['A{}'.format(3)].value),
    "PayerName": worksheet['B{}'.format(3)].value
}

mama_dict = {}

for row in worksheet['A']:
    another_test_dict = {
        "RecordID": worksheet['A{}'.format(number_of_rows)].value,
        "PayerName": worksheet['B{}'.format(number_of_rows)].value,
        "PayerID": worksheet['C{}'.format(number_of_rows)].value,
        "PayerCity": worksheet['D{}'.format(number_of_rows)].value,
        "PayerState": worksheet['E{}'.format(number_of_rows)].value,
        "PayerZip": worksheet['F{}'.format(number_of_rows)].value,
        "Medicare": worksheet['G{}'.format(number_of_rows)].value,
        "Medicaid": worksheet['H{}'.format(number_of_rows)].value,
        "FECA": worksheet['I{}'.format(number_of_rows)].value,
        "Tricare": worksheet['J{}'.format(number_of_rows)].value,
        "GroupHealthPlan": worksheet['K{}'.format(number_of_rows)].value,
        "Champva": worksheet['L{}'.format(number_of_rows)].value,
        "Other": worksheet['M{}'.format(number_of_rows)].value,
        "InsuredsIDNo": worksheet['N{}'.format(number_of_rows)].value,
        "PatientLastName": worksheet['O{}'.format(number_of_rows)].value,
        "PatientFirstName": worksheet['P{}'.format(number_of_rows)].value,
        "PatientMiddleNameInitial": worksheet['Q{}'.format(number_of_rows)].value,
        "PatientDOBMonth": worksheet['R{}'.format(number_of_rows)].value,
        "PatientDOBDay": worksheet['S{}'.format(number_of_rows)].value,
        "PatientDOBYear": worksheet['T{}'.format(number_of_rows)].value,
        "PatientGenderM": worksheet['U{}'.format(number_of_rows)].value,
        "PatientGenderF": worksheet['V{}'.format(number_of_rows)].value,
        "InsuredsLastName": worksheet['W{}'.format(number_of_rows)].value,
        "InsuredsFirstName": worksheet['X{}'.format(number_of_rows)].value,
        "InsuredsMiddleNameInitial": worksheet['Y{}'.format(number_of_rows)].value,
        "PatientsAddressStreetNo": worksheet['Z{}'.format(number_of_rows)].value,
        "PatientsCity": worksheet['AA{}'.format(number_of_rows)].value,
        "PatientsState": worksheet['AB{}'.format(number_of_rows)].value,
        "PatientZipCode": worksheet['AC{}'.format(number_of_rows)].value,
        "PatientRelationshipToInsuredSpouse": worksheet['AD{}'.format(number_of_rows)].value,
        "PatientRelationshipToInsuredChild": worksheet['AE{}'.format(number_of_rows)].value,
        "PatientRelationshipToInsuredOther": worksheet['AF{}'.format(number_of_rows)].value,
        "PatientRelationshipToInsuredSelf": worksheet['AG{}'.format(number_of_rows)].value,
        "InsuredsAddressStreetNo": worksheet['AH{}'.format(number_of_rows)].value,
        "InsuredsCity": worksheet['AI{}'.format(number_of_rows)].value,
        "InsuredsState": worksheet['AJ{}'.format(number_of_rows)].value,
        "InsuredsZipCode": worksheet['AK{}'.format(number_of_rows)].value,
        "InsuredsGenderFemale": worksheet['AL{}'.format(number_of_rows)].value,
        "InsuredsGenderMale": worksheet['AM{}'.format(number_of_rows)].value,
        "InsuredsOtherNameLastFirstMInitial": worksheet['AN{}'.format(number_of_rows)].value,
        "InsuredsPolicyOrGroupNumberOther": worksheet['AO{}'.format(number_of_rows)].value,
        "InsurancePlanNameOrProgramName": worksheet['AP{}'.format(number_of_rows)].value,
        "AutoAccidentState": worksheet['AQ{}'.format(number_of_rows)].value,
        "PatientConditionOtherAccidentNo": worksheet['AR{}'.format(number_of_rows)].value,
        "PaitentConditionOtherAccidentX": worksheet['AS{}'.format(number_of_rows)].value,
        "PatientConditionAutoAccidentX": worksheet['AT{}'.format(number_of_rows)].value,
        "PatientConditionAutoNo": worksheet['AU{}'.format(number_of_rows)].value,
        "PatientConditionAutoNumber": worksheet['AV{}'.format(number_of_rows)].value,
        "PatientConditionEmploymentX": worksheet['AW{}'.format(number_of_rows)].value,
        "ClaimCodesDesignatedByNUCC": worksheet['AX{}'.format(number_of_rows)].value,
        "OtherHealthPlanYes": worksheet['AY{}'.format(number_of_rows)].value,
        "OtherHealthPlanNo": worksheet['AZ{}'.format(number_of_rows)].value,
        "InsuredsPolicyGroupOrFECANo": worksheet['BA{}'.format(number_of_rows)].value,
        "InsuredsDOBMonth": worksheet['BB{}'.format(number_of_rows)].value,
        "InsuredsDOBDate": worksheet['BC{}'.format(number_of_rows)].value,
        "InsuredsDOBYear": worksheet['BD{}'.format(number_of_rows)].value,
        "OtherHealthBenefitPlanYes": worksheet['BE{}'.format(number_of_rows)].value,
        "OtherHealthBenefitPlanNo": worksheet['BF{}'.format(number_of_rows)].value,
        "SignatureOnFileYes": worksheet['BG{}'.format(number_of_rows)].value,
        "Date": worksheet['BH{}'.format(number_of_rows)].value,
        "InsuredAuthorizedSignatureYes": worksheet['BI{}'.format(number_of_rows)].value,
        "DateOfCurrentIllness": worksheet['BJ{}'.format(number_of_rows)].value,
        "Qualifier": worksheet['BK{}'.format(number_of_rows)].value,
        "CurrentIllnessMonth": worksheet['BL{}'.format(number_of_rows)].value,
        "CurrentIllnessYear": worksheet['BM{}'.format(number_of_rows)].value,
        "ReferringProviderID": worksheet['BN{}'.format(number_of_rows)].value,
        "ICDIndicator0=icd10": worksheet['BO{}'.format(number_of_rows)].value,
        "DiagnosisA": worksheet['BP{}'.format(number_of_rows)].value,
        "DiagnosisB": worksheet['BQ{}'.format(number_of_rows)].value,
        "DiagnosisC": worksheet['BR{}'.format(number_of_rows)].value,
        "DiagnosisD": worksheet['BS{}'.format(number_of_rows)].value,
        "DiagnosisE": worksheet['BT{}'.format(number_of_rows)].value,
        "DateOfServiceFromMonth": worksheet['BU{}'.format(number_of_rows)].value,
        "DateOfServiceFromDay": worksheet['BV{}'.format(number_of_rows)].value,
        "DateOfServiceFromYear": worksheet['BW{}'.format(number_of_rows)].value,
        "POS": worksheet['BX{}'.format(number_of_rows)].value,
        "EMG": worksheet['BY{}'.format(number_of_rows)].value,
        "CPT/HCPS": worksheet['BZ{}'.format(number_of_rows)].value,
        "ModifierA": worksheet['CA{}'.format(number_of_rows)].value,
        "ModifierB": worksheet['CB{}'.format(number_of_rows)].value,
        "ModifierC": worksheet['CC{}'.format(number_of_rows)].value,
        "ModifierD": worksheet['CD{}'.format(number_of_rows)].value,
        "DiagnosisPointer": worksheet['CE{}'.format(number_of_rows)].value,
        "Charges": worksheet['CF{}'.format(number_of_rows)].value,
        "ChargesDecim": worksheet['CG{}'.format(number_of_rows)].value,
        "GDaysOrUnits": worksheet['CH{}'.format(number_of_rows)].value,
        "EPSDT": worksheet['CI{}'.format(number_of_rows)].value,
        "IQualifer": worksheet['CJ{}'.format(number_of_rows)].value,
        "RenderingProviderID": worksheet['CK{}'.format(number_of_rows)].value,
        "FederalTaxIDNumber": worksheet['CL{}'.format(number_of_rows)].value,
        "SSN": worksheet['CM{}'.format(number_of_rows)].value,
        "EIN": worksheet['CN{}'.format(number_of_rows)].value,
        "PatientAccountNo": worksheet['CO{}'.format(number_of_rows)].value,
        "AcceptAssignmentAlways": worksheet['CP{}'.format(number_of_rows)].value,
        "TotalCharge": worksheet['CQ{}'.format(number_of_rows)].value,
        "TotalChargeDecim": worksheet['CR{}'.format(number_of_rows)].value,
        "AmountPaid": worksheet['CS{}'.format(number_of_rows)].value,
        "AmountPaidDecim": worksheet['CT{}'.format(number_of_rows)].value,
        "ServiceFacultyName": worksheet['CU{}'.format(number_of_rows)].value,
        "ServiceFacultyAddress": worksheet['CV{}'.format(number_of_rows)].value,
        "ServiceFacultyCity": worksheet['CW{}'.format(number_of_rows)].value,
        "ServiceFacultyState": worksheet['CX{}'.format(number_of_rows)].value,
        "ServiceFacultyZip": worksheet['CY{}'.format(number_of_rows)].value,
        "FacilityProviderNPI": worksheet['CZ{}'.format(number_of_rows)].value,
        "FaciltyProviderOtherID": worksheet['DA{}'.format(number_of_rows)].value,
        "BillingProviderFullName": worksheet['DB{}'.format(number_of_rows)].value,
        "BillingProviderAddress": worksheet['DC{}'.format(number_of_rows)].value,
        "BillingProviderCity": worksheet['DD{}'.format(number_of_rows)].value,
        "BillingProviderState": worksheet['DE{}'.format(number_of_rows)].value,
        "BillingProviderZip": worksheet['DF{}'.format(number_of_rows)].value,
        "BillingProviderPhoneAreaCode": worksheet['DG{}'.format(number_of_rows)].value,
        "BillingProviderPhoneNumber": worksheet['DH{}'.format(number_of_rows)].value,
        "BillingProviderNPI": worksheet['DI{}'.format(number_of_rows)].value,
        "BillingProviderOtherID": worksheet['DJ{}'.format(number_of_rows)].value,
        "RenderingNPI": worksheet['DK{}'.format(number_of_rows)].value
    }
    # record_id = worksheet['A{}'.format(number_of_rows)].value
    # payer_name = worksheet['B{}'.format(number_of_rows)].value
    number_of_rows = number_of_rows - 1
    # textfile = open('test.txt', 'a')
    # textfile.write(str(another_test_dict['RecordID']) + '\n')
    # textfile.write(str(another_test_dict['PayerName']) + '\n')
    # textfile.close()
