# GBI Bethel App Data Harvester

GBI Bethel App is a church mobile app (Android & iOS) used for church events planning, announcements, etc. There were several known vulnerabilities in the software, making all church member data fetchable. This is a simple python script that could harvest the church member data including name, church card number, gender, complete address, birthday, phone number, marriage status, blood type, church member information, and complete device information. The vulnerabilities weren't local, so the script worked for harvesting church member data from all the app maker clients. You only needed to find the church name path and church member id range. However, by the time this script is published, all known vulnerabilities have been reported to the app maker and fixed.

The script was created with TOR proxy for anonimity, and uses ip address changer to prevent ip blocking or ip rate limit (although apparently there weren't any).

## Build Environment

Needs TOR proxy and stem library.
