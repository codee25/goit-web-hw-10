from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AuthorForm, QuoteForm
from .models import Author, Quote


# Головна сторінка (доступна всім)
def main(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/index.html', {'quotes': quotes})

# Сторінка автора (доступна всім)
def author_about(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/author.html', {'author': author})

# Додавання автора (тільки для залогінених)
@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='root')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

# Додавання цитати (тільки для залогінених)
@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='root')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})