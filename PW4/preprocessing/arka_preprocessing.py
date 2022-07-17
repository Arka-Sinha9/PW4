import pandas as pd
from numpy import mean
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler

df=pd.DataFrame()

def get_dataframe():

    # example of evaluating a decision tree with random oversampling
    # define dataset
    X, y = make_classification(n_samples=10000, weights=[0.99], flip_y=0)
    # define pipeline
    steps = [('over', RandomOverSampler()), ('model', DecisionTreeClassifier())]
    pipeline = Pipeline(steps=steps)
    # evaluate pipeline
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    scores = cross_val_score(pipeline, X, y, scoring='f1_micro', cv=cv, n_jobs=-1)
    overscore = mean(scores)
    print('F1 Score: %.3f' % overscore)



    # example of evaluating a decision tree with random undersampling
    
    # define dataset
    X, y = make_classification(n_samples=10000, weights=[0.99], flip_y=0)
    # define pipeline
    steps = [('under', RandomUnderSampler()), ('model', DecisionTreeClassifier())]
    pipeline = Pipeline(steps=steps)
    # evaluate pipeline
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    scores = cross_val_score(pipeline, X, y, scoring='f1_micro', cv=cv, n_jobs=-1)
    underscore = mean(scores)
    print('F1 Score: %.3f' % underscore)




    # example of evaluating a model with random oversampling and undersampling
    
    X, y = make_classification(n_samples=10000, weights=[0.99], flip_y=0)
    # define pipeline
    over = RandomOverSampler(sampling_strategy=0.1)
    under = RandomUnderSampler(sampling_strategy=0.5)
    steps = [('o', over), ('u', under), ('m', DecisionTreeClassifier())]
    pipeline = Pipeline(steps=steps)
    # evaluate pipeline
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    scores = cross_val_score(pipeline, X, y, scoring='f1_micro', cv=cv, n_jobs=-1)
    combscore = mean(scores)
    print('F1 Score: %.3f' % combscore)

    df['oversampling']=[overscore]
    df['undersampling']=[underscore]
    df['combination']=[combscore]

    print(df)

    return df


get_dataframe()
