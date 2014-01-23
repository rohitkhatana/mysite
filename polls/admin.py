from django.contrib import admin
from polls.models import Poll, Choice

#admin.StackedInline shows the fields in the stacked line format
#if you want to show the choices in tabular form , we can use admin.TabularInline
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldssets = [
		(None, 				 {'fields' : ['question']}),
		('Date information', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']
	date_hierarchy = 'pub_date'


admin.site.register(Poll, PollAdmin)
