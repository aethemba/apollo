from django.views.generic.base import TemplateView


class HomepageView(TemplateView):
    template_name="core/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['loops'] = [n for n in range(15)]
        return context
