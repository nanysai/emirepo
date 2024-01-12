from django.shortcuts import render
from testapp.form import Form,Form2

# Create your views here.
def first(request):
    return render(request,'testapp/first.html')

def invest(request):
    submitted=False
    if request.method == "POST":
        obj=Form2(request.POST)
        if obj.is_valid():
            inv = obj.cleaned_data["invest_p_m"]
            ipy = obj.cleaned_data["intrest_p_y"]
            noy = obj.cleaned_data["duration_y"]
            b = inv
            c = inv * noy *12
            count=1
            for j in range(2, 1+noy *12  ):
                if j % 12 == 0  :
                   b = b + inv + (b * ipy / 100)
                else:
                   b = b + inv
                count=count+1
                l=b
            count=count
            t_amount=l
            t_intrest=l-c
            t_investment=c
        submitted=True
    obj=Form2()
    if submitted == True:
        dict={'t_amount':t_amount,'t_intrest':t_intrest,'t_investment':t_investment,'obj':obj,'submitted':submitted,'count':count}
    else:
       dict={'obj':obj,'submitted':submitted}
    dict=dict
    return render(request, 'testapp/invest.html', dict)

def psangam(request):
    submitted=False
    l={}
    if request.method == 'POST':
        obj=Form(request.POST)
        if obj.is_valid():
             appu=obj.cleaned_data['appu']
             mpay=obj.cleaned_data['mpay']
             int=obj.cleaned_data['intrest']
             rs=obj.cleaned_data['amtmult']
             count = 1
             boro=appu
             l[count]=boro
             while boro > 0:
                  amount = mpay - (boro / 100 * int)
                  if amount % rs == 0:
                       boro = boro - amount
                  else:
                       boro = boro - amount - ((boro / 100 * int) % rs) + rs
                  count = count + 1
                  l[count]=boro
        submitted=True
    obj = Form()
    dict={'obj':obj,'appu':l,'submitted':submitted}
    return render(request,'testapp/psangam.html',dict)