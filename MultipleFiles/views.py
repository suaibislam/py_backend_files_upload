# from django.shortcuts import render,redirect
# from .forms import MyFileForm
# from .models import MyFileUpload
# from django.contrib import messages
# from django.urls import path
# import os

# # Create your views here.

# def home(request):
#     mydata=MyFileUpload.objects.all()
#     myform=MyFileForm()

#     if mydata!='':
#         context={'form':myform,'mydata':mydata}
#         return render(request,'index.html',context)
#     else:    
#         context={'form':myform}
#         return render(request,'index.html',context)
    
# def uploadfile(request):
#     if request.method=="POST":    
#         myform=MyFileForm(request.POST,request.FILES)               
#         if myform.is_valid():  
#             print("hi")
#             for MyFile in request.FILES.getlist('file'):                        
#                 exists=MyFileUpload.objects.filter(my_file=MyFile).exists()
#                 if exists:
#                     data=1
#                 else:
#                     data=0
#                     MyFileUpload.objects.create(my_file=MyFile).save()  
#             if data==1:                
#                 messages.error(request,'The file already exists...!!!')
#             else:
#                 messages.success(request,"File uploaded successfully.")
#             return redirect('home')

# def deletefile(request,id):
#     mydata=MyFileUpload.objects.get(id=id)    
#     mydata.delete()    
#     os.remove(mydata.my_file.path)
#     messages.success(request,'File deleted successfully.')  
#     return redirect('home')

# def delete_all(request):
#     if request.method=="POST":
#         my_id=request.POST.getlist('id[]')
#         for id in my_id:
#             data = MyFileUpload.objects.get(id=id)
#             data.delete()
#             os.remove(data.my_file.path)
#         messages.success(request,'File deleted successfully.')  
#         return redirect('home')   

# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib import messages
# from .models import FileList
# from .forms import UploadFiles
 
# # Create your views here.
 
# def test(request):
#     return HttpResponse('<h1>Hello World!</h1>')
 
# def formpage(request):
#     form = UploadFiles()
#     print(form.fields)
#     return render(request, "sampleform.html", {"form": form})
 
# def upload(request):
#     if request.method == 'POST':
#         form = UploadFiles(request.POST, request.FILES)
#         if form.is_valid():
#             files = []
#             if 'file_path' in request.FILES:
#                 for file in request.FILES.getlist('file_path'):
#                     files.append(FileList(file_path=file))
#             # print(len(files))
#             if len(files) > 0:
#                 try:
#                     FileList.objects.bulk_create(files)
#                     messages.success(request, "File(s) has been uploaded successfully.")
#                 except Exception as ex:
#                     messages.error(request, ex)
#         else:
#             messages.error(request, 'Form data is invalid')
 
#     return redirect('home')



from django.shortcuts import render, redirect
from .models import UploadedFile
from .forms import UploadFileForm

def upload_and_display_files(request):
    files = UploadedFile.objects.all()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for uploaded_file in request.FILES.getlist('files'):
                UploadedFile.objects.create(file=uploaded_file)
            return redirect('upload_and_display')
    else:
        form = UploadFileForm()

    return render(request, 'upload_and_display.html', {'form': form, 'files': files})