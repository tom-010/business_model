from django.db import models
from helper.with_dates_and_version import WithDatesAndVersion

class Story(WithDatesAndVersion, models.Model):
    previous = models.ForeignKey('Story', null=True, blank=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=256, null=True, blank=True)

    character = models.TextField(default='', blank=True)
    problem_villain = models.TextField(default='', blank=True)
    problem_external = models.TextField(default='', blank=True)
    problem_internal = models.TextField(default='', blank=True)
    problem_philosophical = models.TextField(default='', blank=True)
    guide_empathy = models.TextField(default='', blank=True)
    guide_competence = models.TextField(default='', blank=True)
    plan_process = models.TextField(default='', blank=True)
    plan_agreement = models.TextField(default='', blank=True)
    action_direct = models.TextField(default='', blank=True)
    action_transitional = models.TextField(default='', blank=True)
    avoid_failure = models.TextField(default='', blank=True)
    success = models.TextField(default='', blank=True)

    integrated_story = models.TextField(default='', blank=True)

    one_line_character = models.TextField(default='', blank=True)
    one_line_problem = models.TextField(default='', blank=True)
    one_line_plan = models.TextField(default='', blank=True)
    one_line_success = models.TextField(default='', blank=True)
    one_line_free = models.TextField(default='', blank=True)

    what_do_they_have_from = models.TextField(default='', blank=True)
    what_do_they_have_to = models.TextField(default='', blank=True)
    what_are_they_feeling_from = models.TextField(default='', blank=True)
    what_are_they_feeling_to = models.TextField(default='', blank=True)
    what_is_an_average_day_like_from = models.TextField(default='', blank=True)
    what_is_an_average_day_like_to = models.TextField(default='', blank=True)
    what_is_their_status_from = models.TextField(default='', blank=True)
    what_is_their_status_to = models.TextField(default='', blank=True)

    @property
    def problem(self):
        return f'(Villain) {self.problem_villain} (External) {self.problem_external} (Internal) {self.problem_internal} (Philosophical) {self.problem_philosophical}'

    @property
    def guide(self):
        return f'(Empathy) {self.guide_empathy} (Competence) {self.guide_competence}'

    @property
    def plan(self):
        return f'(Process) {self.plan_process} (Agreement) {self.plan_agreement}'

    @property
    def action(self):
        return f'(Direct) {self.action_direct} (Transitional) {self.action_transitional}'

    def __str__(self):
        return f'[Character] {self.character} [Problem] {self.problem} [Guide] {self.guide} [Plan] {self.plan} [Action] {self.action} [Avoid Failure] {self.avoid_failure} [Success] {self.success}'