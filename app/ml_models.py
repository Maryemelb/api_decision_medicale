import pandas as pd
from sklearn import metrics
from sklearn.discriminant_analysis import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
import joblib

# data_preparation
data= pd.read_csv('./data/dataset.csv')
data['status']= data['status'].map({'negative':0, 'positive':1})

#split data
X= data.drop(columns='status')
y= data['status']
X_train, X_test, y_train, y_test= train_test_split( X,y, test_size=0.3, random_state=42)

#Normalisation
preprocessor= ColumnTransformer(
      transformers=[('X_num',StandardScaler(),X.columns)]
)

#hyper parametre logistic regression
hyper_param= {
      'classification__n_estimators': [50,80,100],
      'classification__max_depth': [1,10,100]
}

#piprline
pipeline_lr= Pipeline([
('preprocessor',preprocessor),
('select_best_features', SelectKBest(score_func=f_classif, k=6)),
('classification', RandomForestClassifier())
])

greadsearch= GridSearchCV(pipeline_lr,hyper_param, cv=4, scoring='f1')
greadsearch.fit(X_train, y_train)
y_pred= greadsearch.predict(X_test)

#metrics
print('Accuracy: ', metrics.accuracy_score(y_pred, y_test))
print('recall: ',metrics.recall_score(y_pred, y_test))
print('f1: ',metrics.f1_score(y_pred, y_test))

best_model= greadsearch.best_estimator_
# Sauvegarder le modèle dans un fichier
joblib.dump(best_model, "app/classification_model.pkl")