from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/auth/', include('users.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/transactions/', include('transactions.urls')),
    path('api/budgets/', include('budgets.urls')),
    path('api/goals/', include('goals.urls')),
    path('api/recurring/', include('recurring_transactions.urls')),

    # Frontend pages
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login_page'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='register_page'),
    path('password-reset/', TemplateView.as_view(template_name='password_reset.html'), name='password_reset_page'),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('transactions/', TemplateView.as_view(template_name='transactions.html'), name='transactions_page'),
    path('recurring/', TemplateView.as_view(template_name='recurring.html'), name='recurring_page'),
    path('budgets/', TemplateView.as_view(template_name='budgets.html'), name='budgets_page'),
    path('goals/', TemplateView.as_view(template_name='goals.html'), name='goals_page'),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('debug/transactions/', TemplateView.as_view(template_name='debug_transactions.html'), name='debug_transactions'),
    path('debug/theme/', TemplateView.as_view(template_name='test_theme.html'), name='test_theme'),
    path('debug/theme-check/', TemplateView.as_view(template_name='theme_debug.html'), name='theme_debug'),
    path('debug/simple-dark/', TemplateView.as_view(template_name='simple_dark_test.html'), name='simple_dark_test'),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
