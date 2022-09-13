# Generates a configuration json for the chart on dashboard page.
def generate_chart(data, performance):
    if performance > 0:
        color_string = 'rgb(32,192,32)'
    else:
        color_string = 'rgb(255,0,0)'
    config = {
        'type': 'line',
        'data': {
            'labels': data,
            'datasets': [{
                'backgroundColor': color_string,
                'borderColor': color_string,
                'data': data
            }]
        },
        'options': {
            'scales': {
                'xAxis': {
                    'display': False
                },
                'yAxis': {
                    'display': False
                }
            },
            'elements': {
                'point': {
                    'radius': 0
                }
            },
            'plugins': {
                'legend': {
                    'display': False
                }
            }
        }
    }
    return config