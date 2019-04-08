from django.shortcuts import render


# Create your views here.


def main(request):
    print(request)
    return render(request, 'main.html')


def result(request):
    print(request)
    fulltext = request.GET['fulltext']
    sentence = fulltext.split(' ')

    wordcount = len(sentence)

    realone = {}

    for word in sentence:
        if word in realone:
            realone[word] += 1

        else:
            realone[word] = 1

    return render(request, 'result.html', {
        'wordcount': wordcount,
        'fulltext': fulltext,
        'realone': realone.items(),
    })
