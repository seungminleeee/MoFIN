from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=100)
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)

    # 가입한 상품 목록 리스트를 ,로 구분된 문자열로 저장함
    financial_products = models.TextField(blank=True, null=True)

    # superuser fields
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

# class CustomAccountAdapter(DefaultAccountAdapter):
#     def save_user(self, request, user, form, commit=True):
#         """
#         Saves a new `User` instance using information provided in the
#         signup form.
#         """
#         from allauth.account.utils import user_email, user_field, user_username
        
#         data = form.cleaned_data
#         first_name = data.get("first_name")
#         last_name = data.get("last_name")
#         email = data.get("email")
#         username = data.get("username")
#         # name 필드를 추가
#         name = data.get("name")
#         nickname = data.get("nickname")
#         email = data.get("email")
#         profile_img = data.get('profile_img')
#         age = data.get('age')
#         money = data.get('money')
#         salary = data.get('salary')
#         financial_product = data.get('financial_products')

#         user_email(user, email)
#         user_username(user, username)
#         if first_name:
#             user_field(user, "first_name", first_name)
#         if last_name:
#             user_field(user, "last_name", last_name)
#         if nickname:
#             user_field(user, "nickname", nickname)
#         if name:
#             user_field(user, "name", name)
#         if email:
#             user_field(user, "email", email)
#         if profile_img:
#             user_field(user, "profile_img", profile_img)
#         if age:
#             user_field(user, "age", age)
#         if money:
#             user_field(user, "money", money)
#         if salary:
#             user_field(user, "salary", salary)
#         # if financial_product:
#         #     financial_products = user.financial_products.split(',')
#         #     financial_products.append(financial_product)
#         #     if len(financial_products) > 1:
#         #         financial_products = ','.join(financial_products)
#         #     user_field(user, "financial_products", financial_products)

#         if "password1" in data:
#             user.set_password(data["password1"])
#         else:
#             user.set_unusable_password()
#         self.populate_username(request, user)
#         if commit:
#             # Ability not to commit makes it easier to derive from
#             # this adapter by adding
#             user.save()
#         return user
    

