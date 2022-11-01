from django.forms import ModelForm
from berita_isu_terkini.models import Berita

class Create(ModelForm):
    class Meta:
        model = Berita
        fields = ['news_title', 'news_date', 'news_highlight' ]