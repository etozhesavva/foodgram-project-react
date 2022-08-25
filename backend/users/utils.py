from .models import Follow


def get_is_subscribed(self, obj):
    user = self.context.get('request').user
    return user.is_authenticated and Follow.objects.filter(
        author=obj, user=user
    ).exists()
