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

for row in worksheet['A']:
    another_test_dict = {
        "RecordID": str(worksheet['A{}'.format(number_of_rows)].value),
        "PayerName": str(worksheet['B{}'.format(number_of_rows)].value),
        "PayerID": str(worksheet['C{}'.format(number_of_rows)].value),
        "PayerCity": str(worksheet['D{}'.format(number_of_rows)].value),
        "PayerState": str(worksheet['E{}'.format(number_of_rows)].value),
        "PayerZip": str(worksheet['F{}'.format(number_of_rows)].value),
        "Medicare": str(worksheet['G{}'.format(number_of_rows)].value),
        "Medicaid": str(worksheet['H{}'.format(number_of_rows)].value),
        "FECA": str(worksheet['I{}'.format(number_of_rows)].value),
        "Tricare": str(worksheet['J{}'.format(number_of_rows)].value),
        "GroupHealthPlan": str(worksheet['K{}'.format(number_of_rows)].value),
        "Champva": str(worksheet['L{}'.format(number_of_rows)].value),
        "Other": str(worksheet['M{}'.format(number_of_rows)].value),
        "InsuredsIDNo": str(worksheet['N{}'.format(number_of_rows)].value),
        "PatientLastName": str(worksheet['O{}'.format(number_of_rows)].value),
        "PatientFirstName": str(worksheet['P{}'.format(number_of_rows)].value),
        "PatientMiddleNameInitial": str(worksheet['Q{}'.format(number_of_rows)].value),
        "PatientDOBMonth": str(worksheet['R{}'.format(number_of_rows)].value),
        "PatientDOBDay": str(worksheet['S{}'.format(number_of_rows)].value),
        "PatientDOBYear": str(worksheet['T{}'.format(number_of_rows)].value),
        "PatientGenderM": str(worksheet['U{}'.format(number_of_rows)].value),
        "PatientGenderF": str(worksheet['V{}'.format(number_of_rows)].value),
        "InsuredsLastName": str(worksheet['W{}'.format(number_of_rows)].value),
        "InsuredsFirstName": str(worksheet['X{}'.format(number_of_rows)].value),
        "InsuredsMiddleNameInitial": str(worksheet['Y{}'.format(number_of_rows)].value),
        "PatientsAddressStreetNo": str(worksheet['Z{}'.format(number_of_rows)].value),
        "PatientsCity": str(worksheet['AA{}'.format(number_of_rows)].value),
        "PatientsState": str(worksheet['AB{}'.format(number_of_rows)].value),
        "PatientZipCode": str(worksheet['AC{}'.format(number_of_rows)].value),
        "PatientRelationshipToInsuredSpouse": str(worksheet['AD{}'.format(number_of_rows)].value),
        "PatientRelationshipToInsuredChild": str(worksheet['AE{}'.format(number_of_rows)].value),
        "PatientRelationshipToInsuredOther": str(worksheet['AF{}'.format(number_of_rows)].value),
        "PatientRelationshipToInsuredSelf": str(worksheet['AG{}'.format(number_of_rows)].value),
        "InsuredsAddressStreetNo": str(worksheet['AH{}'.format(number_of_rows)].value),
        "InsuredsCity": str(worksheet['AI{}'.format(number_of_rows)].value),
        "InsuredsState": str(worksheet['AJ{}'.format(number_of_rows)].value),
        "InsuredsZipCode": str(worksheet['AK{}'.format(number_of_rows)].value),
        "InsuredsGenderFemale": str(worksheet['AL{}'.format(number_of_rows)].value),
        "InsuredsGenderMale": str(worksheet['AM{}'.format(number_of_rows)].value),
        "InsuredsOtherNameLastFirstMInitial": str(worksheet['AN{}'.format(number_of_rows)].value),
        "InsuredsPolicyOrGroupNumberOther": str(worksheet['AO{}'.format(number_of_rows)].value),
        "InsurancePlanNameOrProgramName": str(worksheet['AP{}'.format(number_of_rows)].value),
        "AutoAccidentState": str(worksheet['AQ{}'.format(number_of_rows)].value),
        "PatientConditionOtherAccidentNo": str(worksheet['AR{}'.format(number_of_rows)].value),
        "PaitentConditionOtherAccidentX": str(worksheet['AS{}'.format(number_of_rows)].value),
        "PatientConditionAutoAccidentX": str(worksheet['AT{}'.format(number_of_rows)].value),
        "PatientConditionAutoNo": str(worksheet['AU{}'.format(number_of_rows)].value),
        "PatientConditionAutoNumber": str(worksheet['AV{}'.format(number_of_rows)].value),
        "PatientConditionEmploymentX": str(worksheet['AW{}'.format(number_of_rows)].value),
        "ClaimCodesDesignatedByNUCC": str(worksheet['AX{}'.format(number_of_rows)].value),
        "OtherHealthPlanYes": str(worksheet['AY{}'.format(number_of_rows)].value),
        "OtherHealthPlanNo": str(worksheet['AZ{}'.format(number_of_rows)].value),
        "InsuredsPolicyGroupOrFECANo": str(worksheet['BA{}'.format(number_of_rows)].value),
        "InsuredsDOBMonth": str(worksheet['BB{}'.format(number_of_rows)].value),
        "InsuredsDOBDate": str(worksheet['BC{}'.format(number_of_rows)].value),
        "InsuredsDOBYear": str(worksheet['BD{}'.format(number_of_rows)].value),
        "OtherHealthBenefitPlanYes": str(worksheet['BE{}'.format(number_of_rows)].value),
        "OtherHealthBenefitPlanNo": str(worksheet['BF{}'.format(number_of_rows)].value),
        "SignatureOnFileYes": str(worksheet['BG{}'.format(number_of_rows)].value),
        "Date": str(worksheet['BH{}'.format(number_of_rows)].value),
        "InsuredAuthorizedSignatureYes": str(worksheet['BI{}'.format(number_of_rows)].value),
        "DateOfCurrentIllness": str(worksheet['BJ{}'.format(number_of_rows)].value),
        "Qualifier": str(worksheet['BK{}'.format(number_of_rows)].value),
        "CurrentIllnessMonth": str(worksheet['BL{}'.format(number_of_rows)].value),
        "CurrentIllnessYear": str(worksheet['BM{}'.format(number_of_rows)].value),
        "ReferringProviderID": str(worksheet['BN{}'.format(number_of_rows)].value),
        "ICDIndicator0=icd10": str(worksheet['BO{}'.format(number_of_rows)].value),
        "DiagnosisA": str(worksheet['BP{}'.format(number_of_rows)].value),
        "DiagnosisB": str(worksheet['BQ{}'.format(number_of_rows)].value),
        "DiagnosisC": str(worksheet['BR{}'.format(number_of_rows)].value),
        "DiagnosisD": str(worksheet['BS{}'.format(number_of_rows)].value),
        "DiagnosisE": str(worksheet['BT{}'.format(number_of_rows)].value),
        "DateOfServiceFromMonth": str(worksheet['BU{}'.format(number_of_rows)].value),
        "DateOfServiceFromDay": str(worksheet['BV{}'.format(number_of_rows)].value),
        "DateOfServiceFromYear": str(worksheet['BW{}'.format(number_of_rows)].value),
        "POS": str(worksheet['BX{}'.format(number_of_rows)].value),
        "EMG": str(worksheet['BY{}'.format(number_of_rows)].value),
        "CPT/HCPS": str(worksheet['BZ{}'.format(number_of_rows)].value),
        "ModifierA": str(worksheet['CA{}'.format(number_of_rows)].value),
        "ModifierB": str(worksheet['CB{}'.format(number_of_rows)].value),
        "ModifierC": str(worksheet['CC{}'.format(number_of_rows)].value),
        "ModifierD": str(worksheet['CD{}'.format(number_of_rows)].value),
        "DiagnosisPointer": str(worksheet['CE{}'.format(number_of_rows)].value),
        "Charges": str(worksheet['CF{}'.format(number_of_rows)].value),
        "ChargesDecim": str(worksheet['CG{}'.format(number_of_rows)].value),
        "GDaysOrUnits": str(worksheet['CH{}'.format(number_of_rows)].value),
        "EPSDT": str(worksheet['CI{}'.format(number_of_rows)].value),
        "IQualifer": str(worksheet['CJ{}'.format(number_of_rows)].value),
        "RenderingProviderID": str(worksheet['CK{}'.format(number_of_rows)].value),
        "FederalTaxIDNumber": str(worksheet['CL{}'.format(number_of_rows)].value),
        "SSN": str(worksheet['CM{}'.format(number_of_rows)].value),
        "EIN": str(worksheet['CN{}'.format(number_of_rows)].value),
        "PatientAccountNo": str(worksheet['CO{}'.format(number_of_rows)].value),
        "AcceptAssignmentAlways": str(worksheet['CP{}'.format(number_of_rows)].value),
        "TotalCharge": str(worksheet['CQ{}'.format(number_of_rows)].value),
        "TotalChargeDecim": str(worksheet['CR{}'.format(number_of_rows)].value),
        "AmountPaid": str(worksheet['CS{}'.format(number_of_rows)].value),
        "AmountPaidDecim": str(worksheet['CT{}'.format(number_of_rows)].value),
        "ServiceFacultyName": str(worksheet['CU{}'.format(number_of_rows)].value),
        "ServiceFacultyAddress": str(worksheet['CV{}'.format(number_of_rows)].value),
        "ServiceFacultyCity": str(worksheet['CW{}'.format(number_of_rows)].value),
        "ServiceFacultyState": str(worksheet['CX{}'.format(number_of_rows)].value),
        "ServiceFacultyZip": str(worksheet['CY{}'.format(number_of_rows)].value),
        "FacilityProviderNPI": str(worksheet['CZ{}'.format(number_of_rows)].value),
        "FacilityProviderOtherID": str(worksheet['DA{}'.format(number_of_rows)].value),
        "BillingProviderFullName": str(worksheet['DB{}'.format(number_of_rows)].value),
        "BillingProviderAddress": str(worksheet['DC{}'.format(number_of_rows)].value),
        "BillingProviderCity": str(worksheet['DD{}'.format(number_of_rows)].value),
        "BillingProviderState": str(worksheet['DE{}'.format(number_of_rows)].value),
        "BillingProviderZip": str(worksheet['DF{}'.format(number_of_rows)].value),
        "BillingProviderPhoneAreaCode": str(worksheet['DG{}'.format(number_of_rows)].value),
        "BillingProviderPhoneNumber": str(worksheet['DH{}'.format(number_of_rows)].value),
        "BillingProviderNPI": str(worksheet['DI{}'.format(number_of_rows)].value),
        "BillingProviderOtherID": str(worksheet['DJ{}'.format(number_of_rows)].value),
        "RenderingNPI": str(worksheet['DK{}'.format(number_of_rows)].value)
    }
    # record_id = worksheet['A{}'.format(number_of_rows)].value
    # payer_name = worksheet['B{}'.format(number_of_rows)].value
    number_of_rows = number_of_rows - 1
    edi_claim = {
        # Loop  2000A Section
        "Loop2000A/BillingProvider/Hierarchy/1/20/1": "HL*1*20*1~",
        "Loop2000A/BillingProvider/Name": "NM1*85*2*" + another_test_dict["BillingProviderFullName"],
        "Loop2000A/BillingProvider/InfoCont": "CLINIC*****XX*" + another_test_dict["BillingProviderNPI"] + "~",
        "Loop2000A/BillingProvider/StreetAddress": "N3*" + another_test_dict["BillingProviderAddress"] + "~",
        "Loop2000A/BillingProvider/CityStateAndZip": "N4*" + another_test_dict["BillingProviderCity"] + "*" + another_test_dict["BillingProviderState"] + "*" + another_test_dict["BillingProviderZip"] + "~",
        "Loop2000A/BillingProvider/Reference/TaxID/EIN": "REF*EI*" + another_test_dict["FederalTaxIDNumber"] + "~",
        "Loop2000A/BillingProvider/InformationContact": "PERC*IC*" + another_test_dict["PatientLastName"] + "*TE*" + another_test_dict["BillingProviderPhoneNumber"] + "~",
        "Loop2000A/BillingProvider/NM1/87/2": "NM1*87*2*~",
        "Loop2000A/BillingProvider/StreetAddress": "N3*" + another_test_dict["BillingProviderAddress"] + "~",
        "Loop2000A/BillingProvider/CityStateAndZipCode": "N4*" + another_test_dict["BillingProviderCity"] + "*" + another_test_dict["BillingProviderState"] + "*" + another_test_dict["BillingProviderZip"] + "~"
    }
