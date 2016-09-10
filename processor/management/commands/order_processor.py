from processor.utils import get_message_from_sqs_queue
import logging
import requests
import time
import json
from marksafe import settings
from victim.models import Victim
from django.core.management import BaseCommand

class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def make_call(self, details):
        url = settings.MAKECALL_URL
        header = {
        'Authorization': settings.SR_KEY,
        'x-api-key': settings.APP_KEY,
        'Accept' : 'application/json'
        }
        data ={
               "k_number": settings.SR_NUMBER,
               "agent_number": settings.AGENT_NUMBER,
               "customer_number": details.phone_number
            }
        print (url, header, data,
               False)
        call = requests.post(url, headers = header, data= json.dumps(data),
                            verify=False)
        print call.content
        if not call or call.status_code != 200 or not call.content.get('sucess'):
            raise Exception("calling failed: api call failled")
    
    def handle(self, *args, **options):
        while(True):
            msg_list = get_message_from_sqs_queue()
            print msg_list
            for msg in msg_list:
                try:
                    logging.info("processing %s" % msg.get_body())
                    victim_details = json.loads(msg.get_body())
                    logging.info("victim_details %s" % victim_details)
                    victim = Victim.objects.get(id=victim_details['victim_id'])
                    if victim.safety_level not in (0,3,4) and victim.retry_count<= settings.MAX_RETRY:
                        self.make_call(victim)
                        victim.retry_count = victim.retry_count+1
                        victim.save()
                    else:
                        msg.delete()
                except Exception as e:
                    logging.error('failed while placing a call %s' % str(e))
            time.sleep(1)
