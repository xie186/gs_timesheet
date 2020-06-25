import gspread
from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

googleAPI = '/home/xie186/.config/gspread/service_account.json'
scope = ['https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_file(googleAPI)
scopedCreds = credentials.with_scopes(scope)
gc = gspread.Client(auth=scopedCreds)
gc.session = AuthorizedSession(scopedCreds)
sheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/14Nku4VGNPY1ALu_ev0AAba3Ert3ICUOKC7OhcmNXXps/edit?usp=sharing")
print(sheet)
