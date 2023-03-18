import pandas as pd, operator, numpy as np
from xgboost import XGBClassifier
from sklearn.preprocessing import OneHotEncoder

class CreditScoring(object):

    def __init__(self):
        self.__features = ['Age','Gender' ,'Education','MaritalStatus','NrOfDependants','EmploymentStatus','EmploymentDurationCurrentEmployer','WorkExperience','OccupationArea','HomeOwnershipType','IncomeTotal','LiabilitiesTotal','FreeCash']
        self.__categorical_features = ['EmploymentDurationCurrentEmployer', 'WorkExperience']
        self.__input_types = {'Age': 'int64', 'Gender': 'float64', 'Education': 'float64', 'MaritalStatus': 'float64', 'NrOfDependants': 'int64', 'EmploymentStatus': 'float64', 'EmploymentDurationCurrentEmployer': 'O', 'WorkExperience': 'O', 'OccupationArea': 'float64', 'HomeOwnershipType': 'float64', 'IncomeTotal': 'float64', 'LiabilitiesTotal': 'float64', 'FreeCash': 'float64'}
        self.__label = "Defaulted"
        self.__encoder = None
        self.__build_model()

    def __load_data(self):
        self.__data = pd.read_csv("data/loan_data_small.csv", low_memory=False)

    def __one_hot_encoding(self, data, train=True):
        if self.__encoder is None:
            self.__encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
            self.__encoder.fit(data[self.__categorical_features])
        encoded_data = pd.DataFrame(self.__encoder.transform(data[self.__categorical_features]), columns=self.__encoder.get_feature_names_out())
        return pd.concat([data.drop(columns=self.__categorical_features).reset_index(drop=True), encoded_data], axis=1)

    def __preprocess(self):
        self.__data['MaturityDate_Original'] = pd.to_datetime(self.__data['MaturityDate_Original'])
        self.__data['DefaultDate'] = pd.to_datetime(self.__data['DefaultDate'])
        self.__data['LoanDate'] = pd.to_datetime(self.__data['LoanDate'])
        self.__data['NrOfDependants'] = self.__data['NrOfDependants'].replace({"10Plus": 10}).fillna(0).astype('float').astype('int')
        self.__data.sort_values('LoanDate', inplace=True)
        self.__data = self.__data[(self.__data['MaturityDate_Original'] < pd.Timestamp.now())|(~self.__data['DefaultDate'].isna())].copy()
        self.__data["Defaulted"] = (~self.__data['DefaultDate'].isna()).astype(int)
        self.__data = self.__data[self.__features+[self.__label]]
        self.__data = self.__one_hot_encoding(self.__data)
        self.__post_features = [i for i in list(self.__data.columns) if i != self.__label]

    def __train_model(self):
        self.__model = XGBClassifier(eval_metric='logloss')
        self.__model.fit(self.__data[self.__post_features], self.__data[self.__label])

    def __build_model(self):
        self.__load_data()
        self.__preprocess()
        self.__train_model()

    def score(self, input_data):
        return float(self.__model.predict_proba(self.__one_hot_encoding(pd.DataFrame([input_data]).astype(self.__input_types), train=False))[0][0])
