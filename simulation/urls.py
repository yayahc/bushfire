from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (simulations, register, logout_user, update_simulation, complete_simulation,
    delete_simulation, detail_simulation, new_simulation)


urlpatterns = [
    path("", simulations, name="simulations"),
    path("login/", LoginView.as_view(template_name="simulation/login.html"),
        name="login"),
    path("logout/", LogoutView.as_view(template_name="simulation/logout.html"),
        name="logout"),
    path("register/", register, name="register"),
    path("simulation/new/", new_simulation, name="new_simulation"),
    path("update/simulation/<int:pk>/", update_simulation, name="update_simulation"),
    path("simulation/<int:pk>/", detail_simulation, name="detail_simulation"),
    path("complete/simulation/<int:pk>/", complete_simulation, name="complete_simulation"),
    path("delete/simulation/<int:pk>/", delete_simulation, name="delete_simulation"),
]