#we made
from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    return render(request, 'index.html')
   
def parth(request):
    return HttpResponse('Yo')
def analyse(request):
    dj = request.POST.get('text' , 'default')
    yo = request.POST.get('remove' ,'off')
    fullcap = request.POST.get('fullcap' ,'off')
    newlin = request.POST.get('newlin','off')
    extraspace = request.POST.get('extraspaceremove' , 'off')

    print(dj)

    if yo == 'on':
        punc = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analysed = ""
        for char in dj:
            if char not in punc:
                analysed = analysed + char
        params = { 'purpose' : 'Remove Punctuations' , 'Analysed_text' : analysed}
        dj = analysed
    if(fullcap == 'on') :
        analysed = ""
        for char in dj:
            analysed = analysed + char.upper()
        params = { 'purpose' : 'Capitalize' , 'Analysed_text' : analysed}
        dj = analysed
    if(newlin == 'on'):
        analysed = ""
        for char in dj:
            if char != '/n' and char != '/r':
                analysed = analysed + char
            else:
                print("no")
        print("pre" , analysed)

        params = { 'purpose' : 'New Line Remover' , 'Analysed_text' : analysed}
        dj = analysed

    if(extraspace == 'on'):
        analysed = ""
        for index , char in enumerate(dj):
            if dj[index] == ' ' and dj[index + 1] == ' ' :
                pass
            else:
                analysed = analysed + char
        params = { 'purpose' : 'Extra Space Remove' , 'Analysed_text' : analysed}
    if  yo!= 'on' and fullcap != "on" and newlin != 'on' and extraspace != 'on':
            return HttpResponse('Error')
    return render(request , 'edittext.html' , params)

