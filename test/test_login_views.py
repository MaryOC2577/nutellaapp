import unittest
from django.test import RequestFactory
from login.views import LoginView

class TestLoginViews(unittest.TestCase):

    def setup_view(view, request, *args, **kwargs):
        """Mimic as_view() returned callable, but returns view instance.
        args and kwargs are the same you would pass to ``reverse()``
        """
        view.request = request
        view.args = args
        view.kwargs = kwargs
        return view
    
    def test_context_data(self):
        """views.get_context_data() sets 'name' in context."""
        # Setup name.
        name = 'login'
        # Setup request and view.
        request = RequestFactory().get('/login')
        view = LoginView(template_name='login.html')
        view = setup_view(view, request, name=name)
        # Run.
        context = view.get_context_data()
        # Check.
        self.assertEqual(context['name'], name)
        