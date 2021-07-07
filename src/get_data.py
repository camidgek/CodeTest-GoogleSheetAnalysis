import requests


def get_data_from_url(url):
	data = {}
	data['gsheet_url'] = url
	gsheet_id = get_id_from_url(url)
	data['gsheet_id'] = gsheet_id
	gsheet_data = get_sheets_data_by_id(gsheet_id)
	data.update(gsheet_data)
	return data

def get_id_from_url(url):
    # TODO: make this more robust
    try:
        return url.split('d/')[-1].split('/')[0]
    except: 
        return None

def get_sheets_data_by_id(id):
	# TODO: make request to Google Sheets url by page
	sheet_num = 0	
	ret_code = 200
	while ret_code == 200:
		sheet_num += 1
		ret_code, text = get_sheet_data_by_id(id, sheet_num)
	data = {}
	data['num_sheets'] = sheet_num - 1
	data['text'] = text
	return data

def get_sheet_data_by_id(id, sheet_num):
	url = f'https://spreadsheets.google.com/feeds/cells/{id}/{sheet_num}/public/full?alt=json'
	data = requests.get(url)
	return data.status_code, data.text
