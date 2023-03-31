from django.contrib import admin
from listings.models import Band, Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre') # champs que nous voulons sur l'affichage de la liste

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'sold', 'year', 'type', 'band')

# Register your models here.
#admin.site.register(Band)
admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
