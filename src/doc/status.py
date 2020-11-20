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
    def sheet_update(range_name, values=None):
        StatusSheet.__sheet.update(range_name, values)
        StatusSheet.sheet = StatusSheet.__sheet.get_all_values()

    @staticmethod
    def sheet_batch_update(data):
        StatusSheet.__sheet.batch_update(data)
        StatusSheet.sheet = StatusSheet.__sheet.get_all_values()

    @staticmethod
    def add_member(nickname, idx: int):
        StatusSheet.sheet = StatusSheet.__sheet.get_all_values()
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

    @staticmethod
    def get_d(exe: str):
        d_list = {
            "rep": [],
            "reped": []
        }

        for i in StatusSheet.sheet[StatusSheet.__begin:StatusSheet.__end]:
            if i[2] == exe:
                d_list['rep'].append(i[3])
            if i[3] == exe:
                d_list['reped'].append(i[2])

        return d_list
