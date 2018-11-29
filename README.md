# QRScanApp-for-PatientProfiling
QrCode Scanning app for PatientProfiling that generates a unique token for patients if the useridin found in our normalized database of patients.


<h3>Dependencies</h3>

<ul>
  <li>Django 2.0.6</li>
  <li>Python 3.6</li>
  <li>PostgreSQL 10</li>
  <li>django-qr-code module</li>
</ul>

Apps:
1.QrScanner - used by receptionist
2.QRgenerate - should be called when user wants to generate his own QR code from profile app
3.TestApp - dummy app containing models of UserAccount named Test User 
          - model named UniqueScan  contains [user, unique_id, timestap] where user is a foreign key and has objects of TestUser
          

If user's qr code gets scanned within 1 week of previous scan, timestamp will be changed to "now". However the unique key remains unaltered,
If user's qr code gets scanned after 1 week of previous scan, new object with new unique key and current timestamp will be created.

Note:
If data decoded from qr code (user_id) doesnot matches the user_id in UserAccount, print("Error"). U may render error message in a unique way.
