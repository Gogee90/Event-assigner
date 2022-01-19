from django.http import Http404
from rest_framework.permissions import DjangoObjectPermissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class CustomDjangoObjectPermissions(DjangoObjectPermissions):
    def __init__(self):
        self.perms_map["GET"] = ['%(app_label)s.view_%(model_name)s']

    def has_object_permission(self, request, view, obj):
        queryset = self._queryset(view)
        model_cls = queryset.model
        user = request.user

        perms = self.get_required_object_permissions(request.method, model_cls)

        if not user.has_perms(perms):

            if request.method in SAFE_METHODS:
                raise Http404

            read_perms = self.get_required_object_permissions('GET', model_cls)
            if not user.has_perms(read_perms):
                raise Http404

            raise Http404

        return True
