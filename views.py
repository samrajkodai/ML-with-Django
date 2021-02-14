from django.shortcuts import render
from . import fake_model
from . import ml_model
def home(request):
    return render(request,'index.html')


def result(request):
    PassengerId=int(request.GET['PassengerId'])
    Pclass=int(request.GET['Pclass'])
    Sex=int(request.GET['Sex'])
    Age=int(request.GET['Age'])
    Parch=int(request.GET['Parch'])
    Fare=int(request.GET['Fare'])
    Embarked=int(request.GET['Embarked'])
    prediction=ml_model.prediction_model(PassengerId,Pclass,Sex,Age,Parch,Fare,Embarked)
    return render(request,'result.html',{'prediction':prediction})