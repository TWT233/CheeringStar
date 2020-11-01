import gspread


class StatusSheet:
    __instance = None

    def __init__(self, account_key: str, sheets_key: str, sheet_title: str):
        self.account = gspread.service_account(account_key)
        self.sheets = self.account.open_by_key(sheets_key)
        self.sheet = self.sheets.worksheet(sheet_title)
        StatusSheet.__instance = self

    @staticmethod
    def account():
        return StatusSheet.__instance.account

    @staticmethod
    def sheet():
        return StatusSheet.__instance.sheet

    @staticmethod
    def update_b(exe: str, dmg: str, cmt: str, rep: str):
        sheet = StatusSheet.sheet().get_all_values()
        for i in range(len(sheet)):
            if sheet[i][0] == (rep or exe):
                StatusSheet.sheet().update('B{}:D{}'.format(i + 1, i + 1), [[dmg, cmt, rep and exe or '']])

    @staticmethod
    def call_clean():
        sheet = StatusSheet.sheet
        sheet_data = sheet.get_all_values()
        update_list = []

        for i in range(1, min(len(sheet_data), 31)):
            if sheet_data[i][1] or sheet_data[i][2] or sheet_data[i][3]:
                update_list.append({'range': 'B{}:D{}'.format(i + 1, i + 1),
                                    'values': [['', '', '']]})

        sheet.batch_update(update_list)
        return
