from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (simulations, register, logout_user, update_simulation, complete_simulation,
    delete_simulation, detail_simulation, new_simulation, view_graphic, simulate, all_simmulations, about, contact)


urlpatterns = [
    path("", simulations, name="simulations"),
    path("login/", LoginView.as_view(template_name="simulation/login.html"),
        name="login"),
    path("logout/", LogoutView.as_view(template_name="simulation/logout.html"),
        name="logout"),
    path("register/", register, name="register"),
    path("simulation/new/", new_simulation, name="new_simulation"),
    path("simulations/", all_simmulations, name="all_simmulations"),
    path("update/simulation/<int:pk>/", update_simulation, name="update_simulation"),
    path("simulation/<int:pk>/", detail_simulation, name="detail_simulation"),
    path("complete/simulation/<int:pk>/", complete_simulation, name="complete_simulation"),
    path("delete/simulation/<int:pk>/", delete_simulation, name="delete_simulation"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    
    # path('simulation/<int:pk>/download/', download_simulation, name='download_simulation'),
    # path('simulations/download-all/', download_all_simulations, name='download_all_simulations'),
    
    # path('upload-simulation/', upload_simulation, name='upload_simulation'),

    path('simulation/<int:pk>/simulate/', simulate, name='simulate'),
    path('simulation/<int:pk>/graphic/', view_graphic, name='view_graphic'),
]