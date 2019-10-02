from django.utils import timezone

from ..constant import constants

from ..models import Website
from ..models import Link

def save_to_database(yahoo): 
    website = Website.objects.get(web_identifier=constants.constant['yahoo_news'])

    for key, value in yahoo.items():
        link = Link()
        link.link = key
        link.title = value
        link.web_identifier = constants.constant['yahoo_news']
        link.website = website
        link.updated_at = timezone.now()

        try:
            link.save()
        except Exception:
            print("[DEBUG] This data already exists in the database...")
    
    print("[DEBUG] Successfully saved to the database...")