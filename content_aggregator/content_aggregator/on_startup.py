from django.utils import timezone

from main.models import Website 

def on_startup_loader():
    # Save yahoo 
    website = Website()
    website.web_data_title = "Yahoo News"
    website.web_identifier = "YANWS"
    website.updated_at = timezone.now()
    try:
        website.save()
    except Exception:
        print('[DEBUG] Exception occured unique website is already in the database....')
    print("[DEBUG] Successfully saved to the database...")

    pass
