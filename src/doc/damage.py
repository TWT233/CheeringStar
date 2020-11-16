import gspread


class DamageRecord:
    account: gspread.client.Client
    sheets: gspread.models.Spreadsheet
    sheet: list
    __sheet: gspread.models.Worksheet
    __begin = 2
    __end = 32

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
    def commit(r: int, boss: int, dmg: int, exe: str, rep: str, r_time: bool):
        DamageRecord.sheet = DamageRecord.__sheet.get_all_values()
        for i in range(DamageRecord.__begin, min(len(DamageRecord.sheet), DamageRecord.__end)):
            if DamageRecord.sheet[i][0] == (rep or exe):
                rol: list = DamageRecord.sheet[i]
                for col in [1, 5, 9, 13, 17, 21]:
                    if rol[col] == '':
                        DamageRecord.sheet_update(
                            '{}{}:{}{}'.format(chr(ord('A') + col), i + 1, chr(ord('D') + col), i + 1),
                            [['{}-{}'.format(r, boss), dmg, rep and exe or '', r_time]])
                        return
        pass
