from django import template

register = template.Library()


@register.inclusion_tag('store/prices.html')
def show_prices(r_price, h_price):
    if h_price > r_price:
        h_price_answer = '$' + strike(str(h_price))
        s_m = '$' + str(round((h_price - r_price), 2))
        original_price = 'original price'
        you_save = 'you save'

    else:
        r_price = r_price
        s_m = ''
        h_price_answer = ''
        original_price = ''
        you_save = ''

    return {'save_money': s_m, 'real_price': r_price, 'high_price': h_price_answer, 'o': original_price, 'y': you_save}


def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])
