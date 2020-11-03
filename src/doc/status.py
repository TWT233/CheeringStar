import gspread


class StatusSheet:
    account: gspread.client.Client
    sheets: gspread.models.Spreadsheet
    sheet: list
    __sheet: gspread.models.Worksheet
    __begin = 3
    __end = 33

    def __init__(self, account_key: str, sheets_key: str, sheet_title: str):
        StatusSheet.account = gspread.service_account(account_key)
        StatusSheet.sheets = StatusSheet.account.open_by_key(sheets_key)
        StatusSheet.__sheet = StatusSheet.sheets.worksheet(sheet_title)
        StatusSheet.sheet = StatusSheet.__sheet.get_all_values()
        pass

    @staticmethod
    def sheet_update(range_name, values=None, **kwargs):
        StatusSheet.__sheet.update(range_name, values, kwargs)
        StatusSheet.sheet = StatusSheet.__sheet.get_all_values()

    @staticmethod
    def sheet_batch_update(data, **kwargs):
        StatusSheet.__sheet.batch_update(data, kwargs)
        StatusSheet.sheet = StatusSheet.__sheet.get_all_values()

    @staticmethod
    def update_b(exe: str, dmg: str, cmt: str, rep: str):
        for i in range(len(StatusSheet.sheet)):
            if StatusSheet.sheet[i][3] == (rep or exe):
                StatusSheet.sheet_update('B{}:D{}'.format(i + 1, i + 1), [[dmg, cmt, rep and exe or '']])

    @staticmethod
    def call_clean():
        update_list = []

        for i in range(StatusSheet.__begin, min(len(StatusSheet.sheet), StatusSheet.__end)):
            if StatusSheet.sheet[i][0] or StatusSheet.sheet[i][4] or StatusSheet.sheet[i][5]:
                update_list.append({'range': 'A{}'.format(i + 1), 'values': [['']]})
                update_list.append({'range': 'E{}'.format(i + 1), 'values': [['']]})
                update_list.append({'range': 'F{}'.format(i + 1), 'values': [['']]})

        StatusSheet.sheet_batch_update(update_list)
        return

    @staticmethod
    def get_candao():
        candao_list = []

        for i in StatusSheet.sheet[StatusSheet.__begin:StatusSheet.__end]:
            if i[6]:
                candao_list.append({'name': i[3], 'cmt': i[6]})

        return candao_list

    @staticmethod
    def get_shu():
        shu_list = []

        for i in StatusSheet.sheet[StatusSheet.__begin:StatusSheet.__end]:
            if i[4] or i[5]:
                shu_list.append({'name': i[3], 'dmg': i[4], 'cmt': i[5]})

        return shu_list
