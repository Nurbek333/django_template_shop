from django.urls import path
from .views import thankyou,shop,services,contact,checkout,cart,blog,about,index

urlpatterns = [

path('',index,name= "index-page"),
path('about/',about,name= "about-page"),
path('blog/',blog,name= "blog-page"),
path('cart/',cart,name= "cart-page"),
path('checkout/',checkout,name= "checkout-page"),
path('contact/',contact,name= "contact-page"),
path('services/',services,name= "services-page"),
path('shop/',shop,name= "shop-page"),
path('thankyou/',thankyou,name= "thankyou-page"),
]