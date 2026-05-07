from django.http import HttpResponseForbidden


def union_rep_required(view_func):

    def wrapper(request, *args, **kwargs):

        if (
            request.user.is_superuser
            or request.user.groups.filter(
                name="Union Representative"
            ).exists()
        ):
            return view_func(request, *args, **kwargs)

        return HttpResponseForbidden()

    return wrapper