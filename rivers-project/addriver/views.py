from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages 
from addriver.models import River
from addriver.riverconfig import *
import time


def Add_River(rivername, length, Miles, RiverRating):
     New_River = River(RiverName = rivername,
                        RiverLengthKm = length,
                        RiverLengthMiles = Miles,
                        RiverRating = RiverRating,)
                        
     print(New_River)
     New_River.save()

# Create your views here.
def New_River(request):
    
    if request.method == "POST":

        details = {}

        details['rivername'] = request.POST.get('rivername','')
        details['length'] = request.POST.get('length','')
        details['rapids'] = request.POST.get('rapids','')

        MissingFields = list()

        for DicKey, DicValue in details.items():
            if DicValue == "":
                MissingFields.append(DicKey)
                print(MissingFields)

        if MissingFields:
            errormsg = f"Missing fields for {', '.join(MissingFields)}"
            messages.add_message(request, messages.WARNING, errormsg)
            return render(request, "river.html")
        
        rapids = int(details['rapids'])
        length = int(details['length'])
        Miles = Km_To_Miles(length)
        RiverScore = Rating(length, rapids)
        RiverRating = River_Grade(RiverScore)
        Add_River(details['rivername'], length, Miles, RiverRating)
        print(Miles)
        print(RiverScore)
        print(RiverRating)      

    return render(request, "river.html")


def View_River_Details(request):
    print(request.method)
    if request.method =='POST':
        print("inside")
        print(request.method)
        all_rivers = River.objects.all()
        if 'Display' in request.POST:
            return render(request, "results.html", {'all_rivers': all_rivers,})
    
    return render(request, "results.html")

