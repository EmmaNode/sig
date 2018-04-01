from __future__ import print_function
from httplib2 import Http

from apiclient import discovery
from oauth2client import client, file, tools
from oauth2client.file import Storage

# import qotd
signature = {'signature': '<div style="width:510px"><div> <div style="max-width:510px"> <table border="0" cellpadding="0" cellspacing="0" width="510"> <tr> <td valign="top" style="vertical-align:top;width:100px"> <table border="0" cellpadding="0" cellspacing="0"> <tr> <td> <img width="90" src="https://s3.amazonaws.com/corporate-v2.wisestamp.com/36b7a6e0-7c6e-45a8-8d7f-1c3c0e8aa089/MIRABELLA_AT_VILLAGE_GREEN_LOGO_ICON.jpg" alt="photo" style="max-width:90px"> </td> </tr> </table> </td> <td valign="top" style="vertical-align:top;padding-left:5px"> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td style="padding-bottom:6px"> <table border="0" cellpadding="0" cellspacing="0" width="100%" style="line-height:1.6;font-family:sans-serif;font-size:11px;color:#4e4b4c;padding-left:2px;font-weight:normal;width:100%"> <tr> <td> <span style="color:#7d7d7d;padding:0px;margin:0px;font-size:15px;font-weight:bold">Monique Viehman</span><br> <span>Marketing Manager</span> <span>at </span><span style="color:#7d7d7d">Mirabella Florida</span> </td> <td valign="top" align="right" style="text-align:right;vertical-align:bottom;padding-left:10px"> </td> </tr> </table> </td> </tr> <tr> <td style="border-top:0.3px solid #acacac;line-height:0px">  </td> </tr> <tr style="padding-bottom:3px"> <td style="padding-bottom:6px;padding-top:3px"> <table border="0" cellpadding="0" cellspacing="0" width="100%" style="line-height:1.6;font-family:sans-serif;font-size:11px;color:#4e4b4c;padding-left:2px;font-weight:normal;width:100%"> <tr> <td> <span style="color:#7d7d7d;font-weight:bold">Address </span><span>1401 Village Green Pkwy  Bradenton, FL 34209 </span><br> <span style="display:inline-flex;padding-right:7px"> <span style="color:#7d7d7d;font-weight:bold">Email </span> <a href="mailto:va7yva@mirabellaflorida.com" style="text-decoration:none;color:#4e4b4c" target="_blank">          va7yva@mirabellaflorida.com           </a> </span> <br> <span style="display:inline-flex;padding-right:7px"> <span style="color:#7d7d7d;font-weight:bold">Website </span> <a href="http://www.mirabellaflorida.com/?utm_source=WiseStamp&amp;utm_medium=email&amp;utm_term=&amp;utm_content=&amp;utm_campaign=signature" style="text-decoration:none;color:#4e4b4c" target="_blank">          http://www.mirabellaflorida.com/           </a> </span> </td>  </tr> </table> </td> </tr> <tr> <td style="border-top:0.3px solid #acacac;line-height:0px">  </td> </tr><tr> <td style="padding-top:6px"> </td> </tr> </table> </td> </tr> </table> </div> </div><a style="margin:8px 8px 0 0;display:inline-block;vertical-align:bottom" href="https://twitter.com/MirabellaFL?utm_source=WiseStamp&amp;utm_medium=email&amp;utm_term=&amp;utm_content=&amp;utm_campaign=signature" target="_blank"><img src="https://s3.amazonaws.com/images.wisestamp.com/email-apps/twitter_button/twitter-white.png"></a><a style="margin:8px 8px 0 0;display:inline-block;vertical-align:bottom" href="https://www.facebook.com/mirabellaflorida/?ref=hl&amp;utm_source=WiseStamp&amp;utm_medium=email&amp;utm_term=&amp;utm_content=&amp;utm_campaign=signature" target="_blank"><img src="https://s3.amazonaws.com/images.wisestamp.com/apps/facebook_like_us.png"></a><a style="margin:8px 8px 0 0;display:inline-block;vertical-align:bottom" href="https://www.instagram.com/mirabellaflorida/?utm_source=WiseStamp&amp;utm_medium=email&amp;utm_term=&amp;utm_content=&amp;utm_campaign=signature" target="_blank"><img src="https://s3.amazonaws.com/images.wisestamp.com/apps/instagram_white.png"></a><a style="margin:8px 8px 0 0;display:inline-block;vertical-align:bottom" href="https://www.pinterest.com/MirabellaFL/?utm_source=WiseStamp&amp;utm_medium=email&amp;utm_term=&amp;utm_content=&amp;utm_campaign=signature" target="_blank"><img src="https://s3.amazonaws.com/images.wisestamp.com/apps/pinterest_follow_us_white.png"></a></div>'}


SCOPES = 'https://www.googleapis.com/auth/gmail.settings.basic'
CLIENT_SECRET_FILE = 'client_secret.json'
store = file.Storage('storage.json')
creds = store.get()
# APPLICATION_NAME = 'Gmail API Python Quickstart'

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    creds = tools.run_flow(flow, store)
    # credentials = tools.run(flow, store)
GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))


addresses = GMAIL.users().settings().sendAs().list(userId='me',fields='sendAs(isPrimary,sendAsEmail)').execute().get('sendAs', [])
for address in addresses:
	if address['isPrimary']:
		break
 
rsp = GMAIL.users().settings().sendAs().patch(userId='me',sendAsEmail=address['sendAsEmail'], body=signature).execute()
print("Primary address signature changed to '%s'" % rsp['signature'])
