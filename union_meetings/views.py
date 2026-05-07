from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import UnionMeetingInfo
from .forms import UnionMeetingInfoForm
from .decorators import union_rep_required

@login_required
def meetings_home(request):
    meeting_info, created = UnionMeetingInfo.objects.get_or_create(id=1)

    can_edit_union_page = (
        request.user.is_superuser
        or request.user.groups.filter(name="Union Representative").exists()
    )

    return render(
        request,
        "union_meetings/meetings.html",
        {
            "meeting_info": meeting_info,
            "can_edit_union_page": can_edit_union_page,
        }
    )


@login_required
@union_rep_required
def edit_meeting_info(request):
    meeting_info, created = UnionMeetingInfo.objects.get_or_create(id=1)

    if request.method == "POST":
        form = UnionMeetingInfoForm(request.POST, instance=meeting_info)

        if form.is_valid():
            form.save()
            return redirect("union_meetings:home")
    else:
        form = UnionMeetingInfoForm(instance=meeting_info)

    return render(
        request,
        "union_meetings/edit_meeting_info.html",
        {
            "form": form,
        }
    )