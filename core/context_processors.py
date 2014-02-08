from django.conf import settings

def installed_apps_context_processor(request):
    apollo_apps = []
    index = settings.INSTALLED_APPS.index('core')
    for app in settings.INSTALLED_APPS[index:]:
        apollo_apps.append(app)

    context = {
        'installed_apps' : settings.INSTALLED_APPS,
        'apollo_apps': apollo_apps
    }
    return context