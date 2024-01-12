from django import forms

class Form(forms.Form):
    appu=forms.IntegerField()
    mpay=forms.IntegerField()
    intrest=forms.FloatField()
    amtmult=forms.IntegerField()

class Form2(forms.Form):
    invest_p_m=forms.IntegerField()
    intrest_p_y=forms.FloatField()
    duration_y=forms.IntegerField()