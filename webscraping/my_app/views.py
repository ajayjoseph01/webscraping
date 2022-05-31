from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate,login
from my_app.models import *
from webscraping.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.views.defaults import page_not_found
from django.contrib import messages
import random
import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import random
from urllib.request import urlopen
import pandas as pd

def Register(request):
    if request.method == 'POST':
         fname = request.POST['fname']
         email = request.POST['email']
         contact = request.POST['contact']
         dob = request.POST['dob']
         gender = request.POST['gender']
         country = request.POST['country']
         state = request.POST['state']
         reg_date=datetime.now()
         username = fname
         password = random.randint(10000, 99999)
         photo = request.FILES['photo']
         if candidates.objects.filter(email=email).exists():
          msg_warning = "Mail id exists"
          return render(request,'user_registration.html',{'msg_warning':msg_warning})
         else:
          register = candidates(fullname=fname, email=email, contact_no=contact,
                              username=username, password=password, photo=photo,
                              date_of_birth=dob,gender=gender,country=country,reg_date=reg_date)
          register.save()
          messages.success(
          request, 'username and password  are sent to your registered mail id.........')
          member = candidates.objects.get(id=register.id)
          subject = 'Greetings from iNFOX TECHNOLOGIES'
          message = 'Congratulations,\n' \
            'You have successfully registered with Web Scraping Site.\n' \
            'following is your login credentials\n'\
            'username :'+str(member.username)+'\n' 'password :'+str(member.password)
              
          recepient = str(email)
          send_mail(subject, message, EMAIL_HOST_USER,
                  [recepient], fail_silently=False)
          msg_success = "Registration completed Check Your Mail"
          return render(request,'user_registration.html',{'msg_success':msg_success})              
    else:
      return render(request, 'user_registration.html')

def Login(request): 
    if request.method == 'POST':
        if candidates.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            mem = candidates.objects.get(
                password=request.POST['password'], email=request.POST['email'])
            request.session['username'] = mem.username
            request.session['username1'] = mem.id      
            username = request.session['username']
            username1 = request.session['username1']
            use = candidates.objects.filter(id=mem.id)
            return render(request, 'user_dashboard.html',{'use':use})      
        elif request.method == 'POST':
            username = request.POST['email']
            password = request.POST.get('password', None)
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                  context = {'msg_error': 'Invalid data'}
                  return render(request, 'user_login.html',context) 
    return render(request, 'user_login.html')  

def admin_dashboard(request):
    mem = User.objects.all()
    ctn = candidates.objects.all().count()
    return render(request,'admin_dashboard.html',{'mem':mem,'ctn':ctn})

def users(request):
    mem = User.objects.all()
    ctn = candidates.objects.all().count()
    return render(request,'users.html',{'mem':mem,'ctn':ctn,})

def users_table(request):
    mem = User.objects.all()
    z = candidates.objects.all()
    return render(request,'users_table.html',{'mem':mem,'z':z,})

def users_details(request,id):
    mem = User.objects.all()
    z = candidates.objects.filter(id=id)
    return render(request,'users_details.html',{'mem':mem,'z':z,})   

def logout(request):
    auth.logout(request)
    return redirect("/") 

def user_dashboard(request):
    if 'username1' in request.session:
      if request.session.has_key('username'):
        username = request.session['username']
      if request.session.has_key('username1'):
        username1 = request.session['username1']
      else:
        username1 = "dummy"
      use = candidates.objects.filter(id=username1)
    return render(request,'user_dashboard.html',{'use':use})
    
def user_logout(request):
    if 'username1' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def changepassword_user(request):
    if 'username1' in request.session:
        if request.session.has_key('username1'):
            username1 = request.session['username1']
        use = candidates.objects.filter(id=username1)
        if request.method == 'POST':
            abc = candidates.objects.get(id=username1)
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    msg_success="Password Changed Successfully"
                    return render(request, 'user_dashboard.html', {'use': use,'msg_success':msg_success})
            elif oldps == newps:
                messages.add_message(request, messages.INFO,
                                     'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')

            return render(request, 'changepassword_user.html', {'use': use})
        return render(request, 'changepassword_user.html', {'use': use})
    else:
        return redirect('/')

def account_user(request):
    if 'username1' in request.session:
        if request.session.has_key('username1'):
            username1 = request.session['username1']
        use = candidates.objects.filter(id=username1)
        return render(request, 'account_user.html', {'use': use})
    else:
        return redirect('/')

def imagechange(request):
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = candidates.objects.get(id=id)
        abc.photo = request.FILES['filenamees']
        abc.save()
        return redirect('account_user')
    return render(request, 'account_user.html')


# GEtting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')
toi_headings = toi_soup.find_all('h2')
toi_headings = toi_headings[0:-13] # removing footers
images = toi_soup.find_all('div', class_="posrel")
  
# toi_img = []
# for item in images:
#     #print(item['src'])
#     toi_img.append(item['src'])

toi_news = []
for th in toi_headings:
    toi_news.append(th.text)

#News from theonion 

ht_r = requests.get("https://www.theonion.com/")
ht_soup = BeautifulSoup(ht_r.content, "html.parser")
ht_headings = ht_soup.find_all('h4')
ht_headings = ht_headings[2:]
ht_news = []
for hth in ht_headings:
    ht_news.append(hth.text)


def news(request):
    if 'username1' in request.session:
      if request.session.has_key('username'):
        username = request.session['username']
      if request.session.has_key('username1'):
        username1 = request.session['username1']
      else:
        username1 = "dummy"
      use = candidates.objects.filter(id=username1)
    return render(request, 'news.html', {'toi_news':toi_news, 'ht_news': ht_news,'use':use,'images':images,})

def get_html_content(request):
    import requests
    city = request.GET.get('city')
    city = city.replace(" ", "+")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://www.google.com/search?q=weather+{city}').text
    return html_content

def weather(request):
    if 'username1' in request.session:
      if request.session.has_key('username'):
        username = request.session['username']
      if request.session.has_key('username1'):
        username1 = request.session['username1']
      else:
        username1 = "dummy" 
      use = candidates.objects.filter(id=username1)
      result = None
      if 'city' in request.GET:
         # fetch the weather from Google.
         html_content = get_html_content(request)
         from bs4 import BeautifulSoup
         soup = BeautifulSoup(html_content, 'html.parser')
         result = dict()
         # extract region
         result['region'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
         # extract temperature now
         result['temp_now'] = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
         # get the day, hour and actual weather
         result['dayhour'], result['weather_now'] = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text.split(
            '\n')
      return render(request, 'weather.html', {'result': result,'use':use,})

########google

def user_search(request):
    if 'username1' in request.session:
      if request.session.has_key('username'):
        username = request.session['username']
      if request.session.has_key('username1'):
        username1 = request.session['username1']
      else:
        username1 = "dummy" 
      use = candidates.objects.filter(id=username1)
    return render(request,'google.html',{'use':use})
  
def scrap(request):
  if 'username1' in request.session:
      if request.session.has_key('username'):
        username = request.session['username']
      if request.session.has_key('username1'):
        username1 = request.session['username1']
      else:
        username1 = "dummy" 
      use = candidates.objects.filter(id=username1)
      scrapdata=request.POST['scrap_data']
      text = scrapdata
      url = 'https://google.com/search?q=' + text
      A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )
      Agent = A[random.randrange(len(A))]
      headers = {'user-agent': Agent}
      r = requests.get(url, headers=headers)
      soup = BeautifulSoup(r.text, 'lxml')
      googles=soup.find_all('h3')
      datas=[]
      for th in googles:
          datas.append(th.text)
         
      df = pd .DataFrame({"datas":datas})
      df.to_csv('text.csv')#Writing to csv file
      df.to_excel('text.xlsx', index=False,header = False)#Writing to Excel file
    
      return render(request,'search_data.html',{'datas':datas,'use':use,'text':text,})
