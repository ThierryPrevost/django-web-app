from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages

#from django.http import HttpResponseRedirect

# Create your views here.
#def hello(request):
def band_list(request):
    bands = Band.objects.all()
    #return HttpResponse('<h1>Hello Django!</h1>')
    '''
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
    """)
    '''
    #return render(request, 'listings/hello.html')
    #return render(request, 'listings/hello.html',context={'first_band': bands[0]})
    #return render(request, 'listings/hello.html',{'bands': bands})
    return render(request, 'listings/band_list.html',{'bands': bands})


    #def band_detail(request, id):
def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    #return render(request, 'listings/band_detail.html', {'band_id': band_id})
    return render(request, 'listings/band_detail.html', {'band': band})

def band_create(request):
    #form = BandForm()
    form = BandForm(request.POST)
    if form.is_valid():
        band = form.save()
        return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})

def band_update(request, band_id):
    band = Band.objects.get(id=band_id)
    #form = BandForm(instance=band)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(reverse('band-detail', kwargs={'id': band.id}))
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form': form})

def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        band.delete()
        #messages.add_message(request, messages.SUCCESS, 'Le groupe ' + band.name + ' a été supprimé')
        messages.success(request, 'Le groupe "' + band.name + '" a été supprimé avec succès')
        #return HttpResponseRedirect(reverse('band-list', kwargs={'id': band.id}))
        return redirect('band-list')
    return render(request, 'listings/band_delete.html', {'band': band})

def about(request):
    #return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')
    return render(request, 'listings/about.html')


def listings(request):
    listings = Listing.objects.all()
    #return HttpResponse('<h1>Listings</h1> <p>Liste de merch !</p>')
    '''
    return HttpResponse(f"""
        <h1>Listings</h1>
        <p>Liste de merch !<p>
        <ul>
            <li>{listings[0].title}</li>
            <li>{listings[1].title}</li>
            <li>{listings[2].title}</li>
            <li>{listings[3].title}</li>
        </ul>
    """)
    '''
    return render(request, 'listings/listings.html', {'listings': listings})

def listings_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, 'listings/listings_detail.html', {'listing': listing})

def listings_create(request):
    #form = BandForm()
    form = ListingForm(request.POST)
    if form.is_valid():
        listing = form.save()
        return redirect('listings-detail', listing.id)
    else:
        form = ListingForm()
    return render(request, 'listings/listings_create.html', {'form': form})

def listings_update(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    #form = ListingForm(instance=listing)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listings-detail', listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listings_update.html', {'form': form})

def listings_delete(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == 'POST':
        listing.delete()
        #messages.add_message(request, messages.SUCCESS, "L'annonce " + listing.title + " a été supprimée")
        messages.success(request, "L'annonce " + listing.title + " a été supprimée avec succès")
        #return HttpResponseRedirect(reverse('listings-list', kwargs={'id': listing.id}))
        return redirect('listings-list')
    return render(request, 'listings/listings_delete.html', {'listing': listing})

def contact(request):
    #print('La méthode de requête est : ', request.method)
    #print('Les données POST sont : ', request.POST)
    # form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    #return HttpResponse('<h1>Contact</h1> <p>Contacter merch !</p>')
    #return render(request, 'listings/contact.html')
    return render(request, 'listings/contact.html', {'form': form})

def email_sent(request):
    return render(request, 'listings/email_sent.html')