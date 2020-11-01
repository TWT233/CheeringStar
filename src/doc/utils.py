from doc import StatusSheet


def tree_rip():
    sheet = StatusSheet.sheet()
    sheet_data = sheet.get_all_values()
    update_list = []

    for i in range(1, min(len(sheet_data), 31)):
        if sheet_data[i][1] or sheet_data[i][2] or sheet_data[i][3]:
            update_list.append({'range': 'B{}:D{}'.format(i + 1, i + 1),
                                'values': [['', '', '']]})

    sheet.batch_update(update_list)
    return
