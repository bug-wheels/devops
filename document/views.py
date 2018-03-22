from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'document/index.html')


def detail(request):
    return render(request, 'document/document_detail.html')


def write(request):
    return render(request, 'document/full.html')


def archive(request, archive_id):
    """

    :param request:
    :param archive_id:
    :return:
    """

    str = '''
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
# Heading 1 link [Heading link](https://github.com/pandao/editor.md "Heading link")
## Heading 2 link [Heading link](https://github.com/pandao/editor.md "Heading link")
### Heading 3 link [Heading link](https://github.com/pandao/editor.md "Heading link")
#### Heading 4 link [Heading link](https://github.com/pandao/editor.md "Heading link") Heading link [Heading link](https://github.com/pandao/editor.md "Heading link")
##### Heading 5 link [Heading link](https://github.com/pandao/editor.md "Heading link")
###### Heading 6 link [Heading link](https://github.com/pandao/editor.md "Heading link")

#### 标题（用底线的形式）Heading (underline)

This is an H1
=============

This is an H2
-------------
'''

    return JsonResponse({"result": str}, safe=False)
