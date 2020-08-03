from django.views import generic, View

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import UploadFileForm
from . import upload_handler

percent_complete = 0

def upload_file(request):
    global percent_complete
    percent_complete = 0 # resets every time

    def progress_callback(monitor):
        # print(monitor.percent_complete, '%')
        global percent_complete
        percent_complete = monitor.percent_complete

    # def progress_callback(monitor):
    #     global percent_complete
    #     percent_complete= monitor.percent_complete
    #     print(monitor.percent_complete)

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload_handler.handle_uploaded_file(request.FILES['file'], callback=progress_callback)
            return HttpResponse('Success!')
            # return HttpResponseRedirect('/success')
    else:
        form = UploadFileForm()
    return render(request, 'fileupload/upload.html', {'form': form})


class UploadProgress(View):
    def get(self, request, **kwargs):
        # print(percent_complete)
        return JsonResponse({'percent_complete': percent_complete})

class Home(generic.TemplateView):
    template_name = 'fileupload/home.html'


class Upload(generic.TemplateView):
    template_name = 'fileupload/upload.html'


class Success(View):
    def get(self, request, **kwargs):
        return HttpResponse('Success!')