from django.shortcuts import render
import pandas as pd
import numpy as np
# Create your views here.
def index(request):
    dicts = {
        "Days":[i for i in range(32)],
        "Months":['January','February','March','April','May','June','July','August','September','October','November','December'],
    }
    return render(request,'index.html',dicts)

def view_posts(request):
    d = int(request.POST.get('day'))
    m = request.POST.get('month')
    df = pd.read_csv('x.csv')
    
    df = df[(df['day']==d) & (df['month']==m)]
    idx = list(df['Unnamed: 0'])
    # imgs = list(df.img)
    desc = list(df.Desc)
    # print(d)
    # print(m)
    # print(type(d))
    # print(type(m))
    # print(len(imgs))
    # print(imgs)
    # print(len(desc))
    # print()
    context = {
        'imgs':idx,
        'desc':desc,
    }
    return render(request,'posts.html',context)

df = pd.read_csv('x.csv')
print(df['Unnamed: 0'][0])
