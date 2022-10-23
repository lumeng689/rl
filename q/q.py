


def filter(req):
    c1 = 'channel_id' in req and req['channel_id'] == 94349557814
    c2 = req.get('city') is not None and req['city'] in [u'\u5317\u4eac', u'__EMPTY_STRING__', u'\u5e7f\u5dde', u'\u6df1\u5733', u'\u4e1c\u839e', u'\u676d\u5dde']
    c3 = req.get('experiment_user') is not None and req['experiment_user'].find('refresh_f3') != -1
    c4 = 'channel_id' in req and req['channel_id'] == 94349557814
    c5 = req.get('device_model') is not None and req['device_model'] in [u'PAFM00 ROM', u'PAHM00', u'PAFT00', u'PAFT10', u'PAFM00', u'PDEM10', u'PDET10', u'PDEM10 ROM', u'PDEM30', u'PDEM30 ROM', u'CPH2025', u'PEDM00', u'PEEM00', u'PFFM10', u'PFEM10', u'PFFM20', u'PEUM00', u'PGBM10', u'PFZM10', u'PGAM10']
    c6 = req.get('experiment_user') is not None and req['experiment_user'].find('refresh_f3') != -1
    r =  c1 and c2 and c3 or c4 and c5 and c6
    print("r=", r)
    return r


if __name__ == "__main__":
    req = {
        'channel_id': 94349557814,
        'city': '温州',
        'device_model': 'RMX3115',
        'experiment_user': 'refresh_f3'
    }

    filter(req)
