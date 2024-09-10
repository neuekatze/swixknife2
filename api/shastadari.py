
import pathlib

TEMPLATE_PATH = pathlib.Path(__file__).parent.resolve().joinpath('template')
CALCULATOR_TEMPLATE_PATH = TEMPLATE_PATH.joinpath('calculator')

from flask import send_file, redirect, Response
from main import app
from  locale_detection import browser_preferred_locale


@app.route('/shastadari')
def shastadari_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari', code=302)

    return redirect('/en/shastadari', code=302)

@app.route('/en/shastadari')
def shastadari_en_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('shastadari_en.html'), mimetype='text/html')

@app.route('/pt/xastadári')
def shastadari_pt_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('shastadari_pt.html'), mimetype='text/html')

@app.route('/bz/xastadari')
def shastadari_bz_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('shastadari_bz.html'), mimetype='text/html')


@app.route('/shastadari/prefixes')
def shastadari_prefixes_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/prefixos', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/prefiksus', code=302)

    return redirect('/en/shastadari/prefixes', code=302)

@app.route('/en/shastadari/prefixes')
def shastadari_prefixes_en_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('prefixes_en.html'), mimetype='text/html')

@app.route('/pt/xastadári/prefixos')
def shastadari_prefixes_pt_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('prefixes_pt.html'), mimetype='text/html')

@app.route('/bz/xastadari/prefiksus')
def shastadari_prefixes_bz_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('prefixes_bz.html'), mimetype='text/html')


@app.route('/shastadari/base-units')
def shastadari_base_units_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/unidades-fundamentais', code=302)

    return redirect('/en/shastadari/base-units', code=302)

@app.route('/en/shastadari/base-units')
def shastadari_base_units_en_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('base_units_en.html'), mimetype='text/html')

@app.route('/pt/xastadári/unidades-fundamentais')
def shastadari_base_units_pt_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('base_units_pt.html'), mimetype='text/html')


@app.route('/shastadari/time-units')
def shastadari_time_units_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/unidades-de-tempo', code=302)

    return redirect('/en/shastadari/time-units', code=302)

@app.route('/en/shastadari/time-units')
def shastadari_time_units_en_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('time_units_en.html'), mimetype='text/html')

@app.route('/pt/xastadári/unidades-de-tempo')
def shastadari_time_units_pt_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('time_units_pt.html'), mimetype='text/html')


@app.route('/shastadari/derived-units')
def shastadari_derived_units_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/unidades-derivadas', code=302)

    return redirect('/en/shastadari/derived-units', code=302)

@app.route('/en/shastadari/derived-units')
def shastadari_derived_units_en_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('derived_units_en.html'), mimetype='text/html')

@app.route('/pt/xastadári/unidades-derivadas')
def shastadari_derived_units_pt_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('derived_units_pt.html'), mimetype='text/html')

@app.route('/shastadari/other-units')
def shastadari_other_units_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/outras-unidades', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/otras-unidadis', code=302)

    return redirect('/en/shastadari/other-units', code=302)

@app.route('/en/shastadari/other-units')
def shastadari_other_units_en_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('other_units_en.html'), mimetype='text/html')

@app.route('/pt/xastadári/outras-unidades')
def shastadari_other_units_pt_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('other_units_pt.html'), mimetype='text/html')

@app.route('/bz/xastadari/otras-unidadis')
def shastadari_other_units_bz_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('other_units_bz.html'), mimetype='text/html')


@app.route('/shastadari/scales')
def shastadari_scales_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/escalas', code=302)

    return redirect('/en/shastadari/scales', code=302)

@app.route('/en/shastadari/scales')
def shastadari_scales_en_route() -> Response:
    if browser_preferred_locale().lower() == 'en-us':
        return send_file(TEMPLATE_PATH.joinpath('scales_en_us.html'), mimetype='text/html')
    elif browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/escalas', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/eskalas', code=302)

    return send_file(TEMPLATE_PATH.joinpath('scales_en.html'), mimetype='text/html')

@app.route('/pt/xastadári/escalas')
def shastadari_scales_pt_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('scales_pt.html'), mimetype='text/html')

@app.route('/bz/xastadari/eskalas')
def shastadari_scales_bz_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('scales_bz.html'), mimetype='text/html')


@app.route('/shastadari/fractions')
def sezimal_fractions_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/frações', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/frasoyns', code=302)

    return redirect('/en/shastadari/fractions', code=302)

@app.route('/en/shastadari/fractions')
def sezimal_fractions_en_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('fractions_en.html'), mimetype='text/html')

@app.route('/pt/xastadári/frações')
def sezimal_fractions_pt_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('fractions_pt.html'), mimetype='text/html')

@app.route('/bz/xastadari/frasoyns')
def sezimal_fractions_bz_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('fractions_bz.html'), mimetype='text/html')
