# Not tested
import requests
from . import __trash
from . import encrypt_k7s2

VXD_INFO = ((__trash.retTr()))

# from_ = "http://127.0.0.1:2781"

from_ = "https://vertexxdb.pythonanywhere.com"

# link_prefix = f"{from_}/handler/OPERATION/{VXD_INFO}/INFO-TO-RETIRIEVE-FROM-?"

# "http://127.0.0.1:2781/handler/get-all/&co;&sq;&00;&02;&02;&14;&20;&13;&19;&ws;&13;&00;&12;&04;&sq;&fc;&ws;&sq;&004;&001;&022;&009;&004;&st;&022;&005;&018;&020;&005;&024;&004;&002;&at;&012;&005;&004;&009;&020;&019;&016;&001;&003;&005;&st;&003;&015;&013;&sq;&cm;&ws;&sq;&00;&02;&02;&14;&20;&13;&19;&ws;&15;&00;&18;&18;&22;&14;&17;&03;&sq;&fc;&ws;&sq;&18;&008;&009;&016;&013;&001;&014;&&4;&&2;&ast;&sq;&cm;&ws;&sq;&03;&01;&ws;&13;&00;&12;&04;&sq;&fc;&ws;&sq;&022;&009;&004;&002;&021;&025;&und;&004;&002;&sq;&cm;&ws;&sq;&03;&01;&ws;&15;&00;&18;&18;&22;&14;&17;&03;&sq;&fc;&ws;&sq;&&2;&&3;&024;&004;&005;&hyph;&024;&bc;&ast;&bo;&020;&018;&009;&013;&&1;&&2;&hs;&&2;&sq;&cc;/&20;&019;&005;&018;&019;"

try:
	response = requests.get(from_)

	def request_then_text_POST(url, data):
		req = requests.post(url, data)
		return req.text

	def request_then_text(url):
		req = requests.get(url)
		return req.text

	session_token = eval(request_then_text(f"{from_}/handler/exchtk/{VXD_INFO}"))
	session_token.append("Bluvid_App_Vidbuy_Companies")
	session_token.append("ddx:/2#+fOPasta;-")
	session_token = encrypt_k7s2.encrypter(str(session_token))
	# print(eval(request_then_text(url=f'{from_}/handler/get-all/{VXD_INFO}/USER')))
	class dbORM:
		"""docstring for dbORM"""
		def __init__(self):
			self.init = True

		def getDBRaw():
			return request_then_text(url=f'{from_}/handler/get-db-raw/{VXD_INFO}')


		def get_all(table):
			pack = {
				"TABLE": table,
				'SESSION TOKEN': session_token
			}
			# connect()

			return eval(request_then_text_POST(url=f'{from_}/handler/get-all', data=pack))

		def find_all(table, column, value):
			pack = {
				'TABLE' : table,
				'FIND_PAIR' : str({column: value}),
				'SESSION TOKEN': session_token
			}
			return eval(request_then_text_POST(url=f'{from_}/handler/find-all', data=pack))

		def add_entry(table, entry):
			pack = {	
				'TABLE' : table,
				'ENTRY' : str(entry),
				'SESSION TOKEN': session_token
			}
			return eval(request_then_text_POST(url=f'{from_}/handler/add-entry', data=pack))
			# print(f">>>>>>>>>>>>>>>>>>>>>>>>>>\ne: {request_then_text(url=f'{from_}/handler/add-entry/{VXD_INFO}/{table}/{entry}')}")

			# except Exception as e:
				# print(f">>>>>>>>>>>>>>>>>>>>>>>>>>\ne: {e}\ntable: {table}\ncvp: {entry}")

		def find_one(table, column, value):
			pack = {	
				'TABLE' : table,
				'FIND_PAIR' : str({column: value}),
				'SESSION TOKEN': session_token
			}
			return eval(request_then_text_POST(url=f'{from_}/handler/find-one', data=pack))

		def update_entry(table, column, entry):
			pack = {	
				'ENTRY' : str(entry),
				'COLUMN' : column,
				'TABLE' : table,
				'SESSION TOKEN': session_token
			}
			return eval(request_then_text_POST(url=f'{from_}/handler/update-entry', data=pack))

		def update_entry_dnd(table, column, entry):
			pack = {
				'ENTRY' : str(entry),
				'COLUMN' : column,
				'TABLE' : table,
				'SESSION TOKEN': session_token
			}
			return eval(request_then_text_POST(url=f'{from_}/handler/update-entry-dnd', data=pack))

		def delete_entry(table, column):
			pack = {
				'TABLE': table,
				'COLUMN': column,
				'SESSION TOKEN': session_token
			}
			return eval(request_then_text_POST(url=f'{from_}/handler/delete-entry', data=pack))


except Exception as e:
	print(e)
	dbORM = None
