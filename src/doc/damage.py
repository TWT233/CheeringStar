import gspread


class DamageRecord:
    account: gspread.client.Client
    sheets: gspread.models.Spreadsheet
    sheet: list
    __sheet: gspread.models.Worksheet
    __begin = 3
    __end = 33

    def __init__(self, account_key: str, sheets_key: str, sheet_title: str):
        DamageRecord.account = gspread.service_account(account_key)
        DamageRecord.sheets = DamageRecord.account.open_by_key(sheets_key)
        DamageRecord.__sheet = DamageRecord.sheets.worksheet(sheet_title)
        DamageRecord.sheet = DamageRecord.__sheet.get_all_values()
        pass

    @staticmethod
    def sheet_update(range_name, values=None):
        DamageRecord.__sheet.update(range_name, values)
        DamageRecord.sheet = DamageRecord.__sheet.get_all_values()

    @staticmethod
    def sheet_batch_update(data):
        DamageRecord.__sheet.batch_update(data)
        DamageRecord.sheet = DamageRecord.__sheet.get_all_values()

    @staticmethod
    def commit(exe: str, dmg: int, rep: str, r_time: int):
        pass
