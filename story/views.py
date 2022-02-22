from django.views import View
from django.shortcuts import redirect, render, reverse, get_object_or_404
from story.models import Story

class StoriesView(View):

    def get(self, request):
        context = {
            'stories': Story.objects.all().order_by('-updated_at')
        }
        return render(request, 'story/all.html', context)

class CreateStoryView(View):

    def post(self, request):
        story = Story.objects.create(name=request.POST['name'])
        return redirect(reverse('story:edit', kwargs={'pk': story.pk}))

class EditStory(View):
    
    def get(self, request, pk):
        story = get_object_or_404(Story, pk=pk)
        return render(request, 'story/edit.html', {'story': story})

    def post(self, request, pk):
        story = get_object_or_404(Story, pk=pk)
        story.name = request.POST['name']
        
        story.character = request.POST['character']
        story.problem_villain = request.POST['problem_villain']
        story.problem_external = request.POST['problem_external']
        story.problem_internal = request.POST['problem_internal']
        story.problem_philosophical = request.POST['problem_philosophical']
        story.guide_empathy = request.POST['guide_empathy']
        story.guide_competence = request.POST['guide_competence']
        story.plan_process = request.POST['plan_process']
        story.plan_agreement = request.POST['plan_agreement']
        story.action_direct = request.POST['action_direct']
        story.action_transitional = request.POST['action_transitional']
        story.avoid_failure = request.POST['avoid_failure']
        story.success = request.POST['success']
        story.integrated_story = request.POST['integrated_story']
        story.one_line_character = request.POST['one_line_character']
        story.one_line_problem = request.POST['one_line_problem']
        story.one_line_plan = request.POST['one_line_plan']
        story.one_line_success = request.POST['one_line_success']
        story.one_line_free = request.POST['one_line_free']
        story.what_do_they_have_from = request.POST['what_do_they_have_from']
        story.what_do_they_have_to = request.POST['what_do_they_have_to']
        story.what_are_they_feeling_from = request.POST['what_are_they_feeling_from']
        story.what_are_they_feeling_to = request.POST['what_are_they_feeling_to']
        story.what_is_an_average_day_like_from = request.POST['what_is_an_average_day_like_from']
        story.what_is_an_average_day_like_to = request.POST['what_is_an_average_day_like_to']
        story.what_is_their_status_from = request.POST['what_is_their_status_from']
        story.what_is_their_status_to = request.POST['what_is_their_status_to']


        story.save()
        return redirect(reverse('story:edit', kwargs={'pk': story.pk}))

class CreateNewVersionView(View):

    def post(self, request, pk):
        story = get_object_or_404(Story, pk=pk)
        story = story.create_new_version()
        return redirect(reverse('story:edit', kwargs={'pk': story.pk}))


class StoriesView(View):

    def get(self, request):
        context = {
            'stories': Story.objects.all()
        }
        return render(request, 'story/stories.html', context)
