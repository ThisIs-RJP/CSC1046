from django.core.cache import cache

def cached_global_variable(request):
    # Retrieve the cached variable, or set a default if it's not set
    global_var = cache.get('game_rooms', [])
    return {
        'game_rooms': global_var,
    }