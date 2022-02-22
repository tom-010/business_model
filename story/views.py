from django.views import View
from django.shortcuts import redirect, render, reverse, get_object_or_404
from story.models import Story

class BusinessModelCanvasesView(View):

    def get(self, request):
        context = {
            'business_model_canvases': BusinessModelCanvas.objects.all().order_by('-updated_at')
        }
        return render(request, 'business_model_canvas/all.html', context)

class CreateBusinessModelCanvasView(View):

    def post(self, request):
        bmc = BusinessModelCanvas.objects.create(name=request.POST['name'])
        return redirect(reverse('business_model_canvas:edit', kwargs={'pk': bmc.pk}))

class EditBusinessModelCanvas(View):
    
    def get(self, request, pk):
        bmc = get_object_or_404(BusinessModelCanvas, pk=pk)
        return render(request, 'business_model_canvas/edit.html', {'bmc': bmc})

    def post(self, request, pk):
        bmc = get_object_or_404(BusinessModelCanvas, pk=pk)
        bmc.name = request.POST['name']
        bmc.one_sentence = request.POST['one_sentence']
        bmc.key_partners = request.POST['key_partners']
        bmc.key_activies = request.POST['key_activies']
        bmc.key_resources = request.POST['key_resources']
        bmc.value_propositions = request.POST['value_propositions']
        bmc.customer_relationships = request.POST['customer_relationships']
        bmc.channels = request.POST['channels']
        bmc.customer_segments = request.POST['customer_segments']
        bmc.cost_structure = request.POST['cost_structure']
        bmc.revenue_streams = request.POST['revenue_streams']
        bmc.save()
        return redirect(reverse('business_model_canvas:edit', kwargs={'pk': bmc.pk}))

class CreateNewVersionView(View):

    def post(self, request,pk):
        bmc = get_object_or_404(BusinessModelCanvas, pk=pk)
        bmc = bmc.create_new_version()
        return redirect(reverse('business_model_canvas:edit', kwargs={'pk': bmc.pk}))


class StoriesView(View):

    def get(self, request):
        context = {
            'stories': Story.objects.all()
        }
        return render(request, 'business_model_canvas/stories.html', context)
