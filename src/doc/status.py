import gspread

from config import Common


class StatusSheet:
    __begin = 3
    __end = 33
    account: gspread.client.Client
    sheets: gspread.models.Spreadsheet
    sheet: list
    __sheet: gspread.models.Worksheet

    def __init__(self, account_key: str, sheets_key: str, sheet_title: str):
        StatusSheet.account = gspread.service_account(account_key)
        StatusSheet.sheets = StatusSheet.account.open_by_key(sheets_key)
        StatusSheet.__sheet = StatusSheet.sheets.worksheet(sheet_title)
        StatusSheet.sheet = StatusSheet.__sheet.get_all_values()
        pass

    @staticmethod
    def sync():
        StatusSheet.sheet = StatusSheet.__sheet.get_all_values()

    @staticmethod
    def sheet_update(range_name, values=None):
        StatusSheet.__sheet.update(range_name, values)
        StatusSheet.sync()

    @staticmethod
    def sheet_batch_update(data):
        StatusSheet.__sheet.batch_update(data)
        StatusSheet.sync()

    @staticmethod
    def add_member(nickname, idx: int):
        StatusSheet.sync()
        for i in range(StatusSheet.__begin, min(len(StatusSheet.sheet), StatusSheet.__end)):
            if StatusSheet.sheet[i][3] == '':
                StatusSheet.sheet_update('D{}'.format(i + 1), [[nickname]])

                member_entry = {'name': nickname, 'id': idx, 'permission': 0}

                Common.guild()['members'].append(member_entry)
                Common.sync()

                print(member_entry)
                return
            if StatusSheet.sheet[i][3] == nickname:
                return

    @staticmethod
    def update_b(exe: str, dmg: str, cmt: str, rep: str):
        for i in range(StatusSheet.__begin, min(len(StatusSheet.sheet), StatusSheet.__end)):
            if StatusSheet.sheet[i][3] == (rep or exe):
                StatusSheet.sheet_update('E{}:F{}'.format(i + 1, i + 1), [[dmg, cmt]])

    @staticmethod
    def update_c(exe: str, cmt: str, rep: str):
        for i in range(StatusSheet.__begin, min(len(StatusSheet.sheet), StatusSheet.__end)):
            if StatusSheet.sheet[i][3] == (rep or exe):
                StatusSheet.sheet_update('G{}'.format(i + 1), [[cmt]])

    @staticmethod
    def update_d(exe: str, rep: str, logout: bool):
        for i in range(StatusSheet.__begin, min(len(StatusSheet.sheet), StatusSheet.__end)):
            if StatusSheet.sheet[i][3] == rep:
                if logout and StatusSheet.sheet[i][2] == exe:
                    StatusSheet.sheet_update('C{}'.format(i + 1), [['']])
                    return
                else:
                    StatusSheet.sheet_update('C{}'.format(i + 1), [[logout and '' or exe]])
                    return

    @staticmethod
    def update_jd(exe: str, rep: str, enter: bool):
        for i in range(StatusSheet.__begin, min(len(StatusSheet.sheet), StatusSheet.__end)):
            if StatusSheet.sheet[i][3] == (rep or exe):
                StatusSheet.sheet_update('A{}'.format(i + 1), [[enter]])

    @staticmethod
    def shu_clean():
        StatusSheet.sync()
        update_list = []

        for i in range(StatusSheet.__begin, min(len(StatusSheet.sheet), StatusSheet.__end)):
            if StatusSheet.sheet[i][0] or StatusSheet.sheet[i][4] or StatusSheet.sheet[i][5]:
                update_list.append({'range': 'A{}'.format(i + 1), 'values': [[False]]})
                update_list.append({'range': 'E{}'.format(i + 1), 'values': [['']]})
                update_list.append({'range': 'F{}'.format(i + 1), 'values': [['']]})

        StatusSheet.sheet_batch_update(update_list)
        return

    @staticmethod
    def get_candao():
        StatusSheet.sync()
        with StatusSheet.sheet[StatusSheet.__begin:StatusSheet.__end] as table:
            return [{'name': i[3], 'cmt': i[6]} for i in filter(lambda i: i[6], table)]

    @staticmethod
    def get_shu():
        StatusSheet.sync()
        with StatusSheet.sheet[StatusSheet.__begin:StatusSheet.__end] as table:
            return [{'name': i[3], 'dmg': i[4], 'cmt': i[5]} for i in filter(lambda i: i[4] or i[5], table)]

    @staticmethod
    def get_d(exe: str):
        StatusSheet.sync()
        with StatusSheet.sheet[StatusSheet.__begin:StatusSheet.__end] as table:
            return {
                "rep": [i[3] for i in filter(lambda i: i[2] == exe, table)],
                "reped": [i[2] for i in filter(lambda i: i[3] == exe, table)]
            }
