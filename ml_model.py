def prediction_model(PassengerId,Pclass,Sex,Age,Parch,Fare,Embarked):
    import pickle
    x=[[PassengerId,Pclass,Sex,Age,Parch,Fare,Embarked]]
    classifier=pickle.load(open('titanic_model.sav','rb'))
    prediction=classifier.predict(x)
    if prediction==1:
        prediction='Survive'
    prediction='Not survive'

    return prediction