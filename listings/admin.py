from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
  list_display=('id','title','is_published','price','list_date','realtor') #display directly in listing
  list_display_links=('id','title')  # create links to click and see data
  list_filter=('realtor',) #create filter based on items in list or tuple..comma is required if 1 item
  list_editable=('is_published',)
  search_fields=('title','description','address','city','state','zipcode','price') #create search field
  list_per_page=25  #add pagination i.e. 25 lists per page

admin.site.register(Listing,ListingAdmin)
  
