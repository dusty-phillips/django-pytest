from django.contrib.auth.models import User, Group

def pytest_funcarg__user(request):
    '''Create a user with no special permissions.'''
    user = User.objects.create_user(username="user", password="user", email="user@example.com")
    return user

def pytest_funcarg__groups(request):
    '''Create some groups with users in them.'''
    groups = []
    for i in range(1, 4):
        group = Group.objects.create(name="group%s" % i)
        user = User.objects.create_user(username="group%s" % i,
                password="user",
                email="group%s@example.com" % i)
        group.user_set.add(user)
        group.save()
        groups.append(group)
    return groups

