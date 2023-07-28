from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def topicforms(request):
    TFO=TopicForm()
    WFO=WebpageForm()
    ARFO=AccessRecordForm()
    d={'TFO':TFO,'WFO':WFO,'ARFO':ARFO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        WFD=WebpageForm(request.POST)
        ARFD=AccessRecordForm(request.POST)

        if TFD.is_valid() and WFD.is_valid() and ARFD.is_valid():
            TFD.save()

            NSWFO=WFD.save(commit=False)
            NSWFO.topic_name=TFD
            NSWFO.save()

            NSARO=AccessRecord.save(commit=False)
            NSARO.name=NSWFO
            NSARO.save()

            return HttpResponse('<center><h1>Topics Data is Inserted Succesfully</h1></center>')



    return render(request,'topicforms.html',d)
