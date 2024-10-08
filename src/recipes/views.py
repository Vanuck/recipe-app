from django.shortcuts import render
from .models import Recipe, Ingredient


def home(request):
    return render(request, "app/recipes_home.html")


def recipe_overview(request):
    recipes = Recipe.objects.all()
    return render(request, "app/recipe_overview.html", {"recipes": recipes})


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    difficulty = recipe.calculate_difficulty()
    return render(
        request, "app/recipe_detail.html", {"recipe": recipe, "difficulty": difficulty}
    )


def search_by_ingredient(request):
    query = request.GET.get("query")
    if query:
        recipes = Recipe.objects.filter(ingredients__name__icontains=query).distinct()
    else:
        recipes = Recipe.objects.none()
    return render(request, "app/search_results.html", {"recipes": recipes})


def search_results(request):
    query = request.GET.get("query", "")
    if query:
        ingredients = Ingredient.objects.filter(name__icontains=query)
        recipes = Recipe.objects.filter(ingredients__in=ingredients).distinct()
    else:
        recipes = Recipe.objects.none()

    return render(request, "search_results.html", {"recipes": recipes})