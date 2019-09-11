from requests import get

with open('results.csv', 'w+') as f:
    d1 = get('http://localhost:5000/log/log_sample_1.log').json()
    d2 = get('http://localhost:5000/log/log_sample_2.log').json()
    d3 = get('http://localhost:5000/log/log_sample_3.log').json()

    f.writelines(','.join(d1.keys())+ '\n')
    for d in (d1, d2, d3):
        res = []
        for key, val in d.items():
            if key == 'portfolios_loaded':
                res.append('|'.join(val))
            else:
                res.append(str(val))
        f.writelines(','.join(res) + '\n')
