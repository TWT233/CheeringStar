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
        return StatusSheet.ins().account

    @staticmethod
    def sheet():
        return StatusSheet.ins().sheet

    @staticmethod
    def update_b(exe: str, dmg: str, cmt: str, rep: str):
        sheet = StatusSheet.sheet().get_all_values()
        for i in range(len(sheet)):
            if sheet[i][0] == (rep or exe):
                StatusSheet.sheet().update('B{}:D{}'.format(i + 1, i + 1), [[dmg, cmt, rep and exe or '']])

    @staticmethod
    def ins():
        return StatusSheet.__instance
