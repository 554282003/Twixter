from django.shortcuts import render
from .models import Twix
from .forms import TwixForm , UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
# def demo(request):
    # return render(request,'demo.html')
def HomePage(request):
  twixs1 = Twix.objects.all().order_by('-created_at') 
  return render(request,'HomePage.html',{'twixs1':twixs1})
@login_required
def twix_create(request):
   if request.method == 'POST':
      form = TwixForm(request.POST,request.FILES)
      if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        return redirect('HomePage')
   else:
      form = TwixForm()
   return render(request,'twix_create.html',{'form':form})

@login_required
def tweet_edit(request,tweet_id):
  twix = get_object_or_404(Twix, pk=tweet_id,user = request.user)
  if request.method == 'POST':
    form = TwixForm(request.POST,request.FILES,instance=twix)
    if form.is_valid():
       tweet = form.save(commit=False)
       tweet.user = request.user
       tweet.save()
  else:
        form = TwixForm(instance=twix)
  return render(request,'twix_create.html',{'form':form})

@login_required
def tweet_delete(request,tweet_id):
   tweet = get_object_or_404(Twix,pk=tweet_id,user = request.user)
   if request.method == 'POST':
      tweet.delete()
      return redirect('HomePage')
   return render(request,'twix_confirm_delete.html',{'tweet':tweet})


def register(request):
   if request.method == 'POST':
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
         user = form.save(commit=False)
         user.set_password(form.cleaned_data['password1'])
         user.save()
         login(request,user)
         return redirect('HomePage')
   else:
      form = UserRegistrationForm()
   return render(request,'registration/register.html',{'form':form})
