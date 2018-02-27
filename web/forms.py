from django import forms

class RegisterForm(forms.Form):
    username=forms.CharField()
    email=forms.EmailField(required=True,error_messages={'invalid':'邮箱格式错误'})

class Alogin(forms.Form):
    username=forms.CharField(error_messages={'requied':('用户名不能为空'),'invalid':('用户名格式错误')})
    #email=forms.EmailField(required=True,error_messages={'requied':('邮箱不能为空'),'invalid':('邮箱格式错误')})
    email=forms.CharField(widget=forms.EmailInput(attrs={'css':'{"color":"red"}'}))  #给email增加样式
    ip=forms.GenericIPAddressField(error_messages={'requied':('ip不能为空'),'invalid':('ip格式错误')})