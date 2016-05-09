import pandas
import random

columns = ['Patient ID', 'Gender_M', 'Gender_F', 'Acromegaly', 'Addisons Disease', 'Alcohol Abuse',
           'Amputation of Limb', 'Amyloidosis', 'Anxiety', 'Aortic Aneurism', 'Arrhythmia', 'Arthropathy', 'Asthma',
           'Autism', 'Behcets Disease', 'Benign Brain Tumor', 'Bipolar Disease (Manic Depressive)', 'Blindness',
           'Bronchiectasis', 'Cardiomyopathy', 'Carotid Artery Disease', 'Celiac Disease', 'Cerebral Palsy', 'CHF',
           'Chronic Act/Per Hepatitis', 'Chronic Bronchitis', 'Chronic Renal Failure', 'Cirrhosis',
           'Congenital Anomalies', 'COPD', 'Crohns Disease', 'Cushings Disease', 'Cystic Fibrosis', 'Deafness',
           'Dementia / Alzheimers / OMS', 'Depression', 'Diabetes', 'Diabetes Insipidus', 'Dialysis', 'Disability',
           'Drug Abuse', 'Epilepsy', 'Familial Mediteranean Fever', 'Family History', 'G-6-P-D Deficiency',
           'Gaucher Disease', 'Glaucoma', 'Gout', 'Hemophilia', 'Hepatitis B Carrier', 'Hepatitis C Carrier',
           'Hereditary Neurological Disease', 'Hidradenitis Suppurativa', 'Hyperlipidemia', 'Hyperprolactinemia',
           'Hypertension', 'Hyperthyroidism', 'Hypo/Hyperparathyroidism', 'Hypophysary Adenoma', 'Hypothyroidism',
           'IHD', 'IHSS', 'Infertility Male/Female', 'Irritable Bowel Syndrome', 'ITP', 'Joint Replacement',
           'Kidney Transplant', 'Malignancy', 'Mental Retardation (incl. Down)', 'Motor Neuron Disease',
           'Multiple Sclerosis', 'Muscular Dystrophy', 'Myasthenia Gravis', 'Neuroses', 'Obesity',
           'organ Transplantation', 'Osteoporosis', 'Other Endocrine and Metabolic Disease',
           'Other Hematologic Dis (excl. Iron Def Anemia)', 'other kidney Disease', 'Other Liver Disease',
           'Other Neurological Disease', 'Other Rheumatic / Autoimmune', 'Parkinsons Disease', 'Pemphigus Vulgaris',
           'Peptic Ulcer', 'Pernicious Anemia', 'Polymyalgia Rheumatica', 'Prostatic Hypertrophy', 'Psoriasis',
           'Psychoses', 'Pulmonary Hypertension', 'PVD', 'Reflux Esophagitis / Gastritis / Deudenitis',
           'Retinitis Pigmentosum', 'Retinopathy', 'Rheumatoid Arthritis', 's/p CVA', 's/p Head of Femur Fracture',
           's/p Pneumothorax', 's/p Pulmonary Embolism', 's/p splenectomy', 'Sarcoidosis', 'Schizophrenia',
           'Scleroderma', 'Sickle Cell Anemia', 'SLE', 'Smoking', 'Syphilis / Gonorrhea', 'Thalassemia', 'Tuberculosis',
           'Tuberculosis s/p', 'Ulcerative Colitis', 'Valvular Cardiac Dis (excl.MVP)', 'Wilsons Disease'
           ]

statistic_data = pandas.DataFrame.from_csv("static/statistics.csv", index_col=False)
statistic_data = dict(zip(statistic_data['Disease'],
                          statistic_data['Percentage'].apply(lambda x: float(x.replace('%', '')))))
statistic_data['Gender_M'] = 50


def fill_row(x):
    repr_dict = x.to_dict()
    for key, value in repr_dict.iteritems():
        if key not in ['Patient ID', 'Gender_F']:
            num = random.uniform(0, 100)
            if num <= statistic_data[key]:
                x[key] = 1
            else:
                x[key] = 0

    return x


def save_dummy_data(path, name, cols=columns):
    """
    !!!!!!!!!!!!!!!Caution!!!!!!!!!! OVVERIDES THE EXISTING DATA FILE!!!!!!!!!!!!!!
    :param name: the name of the file.
    :param path: where the file should be saved, appended to current working directory.
    :param cols: the names of the columns of the data frame as a list.
    :return: a data frame object that represents the csv file.
    """
    df = pandas.DataFrame(columns=cols)
    df['Patient ID'] = range(10000)
    df = df.apply(lambda x: fill_row(x), axis=1)
    df['Gender_F'] = df['Gender_M'].apply(lambda x: 1 - x)
    df['Patient ID'] = df.index
    df.to_csv(path + name, index=False, encoding='utf-8')
    return df


def load_dummy_data_from_hard_disc(path, name):
    """
    :param path: where the file should be saved, appended to current working directory.
    :param name: the name of the file.
    :return: a data frame object that represents the csv file.
    """
    return pandas.DataFrame.from_csv(path + name, index_col=False)