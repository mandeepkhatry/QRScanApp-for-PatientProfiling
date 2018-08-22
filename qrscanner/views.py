from django.shortcuts import render

#Include model of the user account
from testapp.models import Testuser,UniqueScan

import uuid
from datetime import datetime,timedelta
# Create your views here.


def scan(request):
    if request.method =="POST" :
        code = str(request.POST.get('code'))
        object = Testuser.objects.filter(user_id=code)

        if(len(object)):
            user_in_uniquescan = list(UniqueScan.objects.filter(user = object[0]))

            # if user has scanned in the past
            if(len(user_in_uniquescan)):
                # check for last visit by the user

                last_scanned = user_in_uniquescan[len(user_in_uniquescan)-1]

                if ((((last_scanned.timestamp).replace(tzinfo=None))+ timedelta(days=7))>=datetime.now()):
                    # unique key is same and timestamp is changed to new
                    last_scanned.timestamp = datetime.now()
                    last_scanned.save()
                else:
                    # generate unique id
                    uniqueId = str(uuid.uuid4())
                    a = UniqueScan(user=object[0], unique_id=uniqueId, timestamp=datetime.now())
                    a.save()

            else:
                # generate unique id
                uniqueId = str(uuid.uuid4())
                a = UniqueScan(user=object[0], unique_id=uniqueId, timestamp=datetime.now())
                a.save()

        else:

            # Use alert for Error
            print("Error")
    return render(request,'qrscan.html')


