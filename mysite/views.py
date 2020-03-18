# this is created explicitly by programmers.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   #  return HttpResponse('<h1> hello raj </h1> <button><a href="about"> About Page </a>')
    return render(request, 'index.html', {"name": "raj"})


def about(request):
    return HttpResponse('hello this page is from about page')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    print(djtext)
    removePunc = request.POST.get('removePunc', 'default')
    fullCaps = request.POST.get('fullCaps', 'off')
    removeExtrasSpace = request.POST.get('removeExtrasSpace', 'off')
    charCnt = request.POST.get('charCnt', 'off')
    print(removePunc)
    if removePunc == "on":
        analyzed_text = ""
        punctuations = '''!()%-^&*~`@#$:"'?/_[]{}<>.,'''
        for char in djtext:
            if(char not in punctuations):
                analyzed_text = analyzed_text + char
        # print(analyzed_text)
        params = {"purpose": "Removed Punctuations",
                  "analyzed_text": analyzed_text}
        djtext = analyzed_text
        #  alayze the text
        # return render(request, 'analyze.html', params)
   
    if removeExtrasSpace == "on":
        analyzed_text = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed_text = analyzed_text + char

        params = {"purpose": "RemovedExtraSpaces From The Word",
                  "analyzed_text": analyzed_text}
        djtext = analyzed_text
   
   
    if fullCaps == "on":
        analyzed_text = ""
        analyzed_text = djtext.upper()
        params = {"purpose": "Uppercase The Word",
                  "analyzed_text": analyzed_text}
        # return render(request, 'analyze.html', params)
        djtext = analyzed_text

   
        # return render(request, 'analyze.html', params)

    if charCnt == "on":
        analyzed_text = "Total Character count In The Word is : " + str(len(djtext))
        params = {"purpose": "Count The Number Of Character in The Word",
                  "analyzed_text": analyzed_text} 
        djtext = analyzed_text           
    if(removePunc != "on" and removeExtrasSpace !="on" and fullCaps !="on" and charCnt !="on"):
        return HttpResponse("Please select any one of theme and try again!!!!!")
    
    return render(request, 'analyze.html', params)    
# def capitalizeFirst(request):
#     return HttpResponse('capitalize')


# def newlineRemove(request):
#     return HttpResponse('ne line')


# def charCount(request):
#     return HttpResponse('count')


# def spaceRemove(request):
#     return HttpResponse('space remove')
