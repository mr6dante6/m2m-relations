from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_section_count = 0
        for form in self.forms:
            is_main = form.cleaned_data.get('is_main')
            if is_main:
                main_section_count += 1

        if main_section_count != 1:
            raise ValidationError('Необходимо указать один основной раздел.')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


admin.site.register(Tag)
