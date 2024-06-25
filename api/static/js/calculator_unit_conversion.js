
function toggle_units(show) {
    if (show) {
        document.getElementById('units').hidden = false;
        document.getElementById('displays').hidden = true;
        // document.getElementById('buttons').hidden = true;
        document.getElementById('buttons').style = 'visibility: hidden;';
    } else {
        document.getElementById('units').hidden = true;
        document.getElementById('displays').hidden = false;
        // document.getElementById('buttons').hidden = false;
        document.getElementById('buttons').style = 'visibility: visible;';
        update_calculation();
    };
};

function set_unit_type() {
    const unit_type = document.getElementById('calculator-sezimal-unit-type').value;

    if (unit_type == 'ang') {
        set_unit_type_sezimal_decimal(unit_type, 'agm', 's');
    } else if (unit_type == 'avt') {
        set_unit_type_sezimal_decimal(unit_type, 'avt', 'Hz');
    } else if (unit_type == 'pad') {
        set_unit_type_sezimal_decimal(unit_type, 'Dpad', 'm');
    } else if (unit_type == 'kex') {
        set_unit_type_sezimal_decimal(unit_type, 'Dkex', 'm2');
    } else if (unit_type == 'ayt') {
        set_unit_type_sezimal_decimal(unit_type, 'Dayt', 'L');
    } else if (unit_type == 'veg') {
        set_unit_type_sezimal_decimal(unit_type, 'veg', 'km/h');
    } else if (unit_type == 'tvr') {
        set_unit_type_sezimal_decimal(unit_type, 'tvr', 'm/s2');
    } else if (unit_type == 'drv') {
        set_unit_type_sezimal_decimal(unit_type, 'Ddrv', 'kg');
    } else if (unit_type == 'gan') {
        set_unit_type_sezimal_decimal(unit_type, 'gan', 'kg/L');
    } else if (unit_type == 'bar') {
        set_unit_type_sezimal_decimal(unit_type, 'Dbar', 'N');
    } else if (unit_type == 'dab') {
        set_unit_type_sezimal_decimal(unit_type, 'Ddab', 'kPa');
    } else if (unit_type == 'kry') {
        set_unit_type_sezimal_decimal(unit_type, 'DXkry', 'kWh');
    } else if (unit_type == 'xat') {
        set_unit_type_sezimal_decimal(unit_type, 'Dxat', 'W');
    } else if (unit_type == 'gtk') {
        set_unit_type_sezimal_decimal(unit_type, 'Xgtk', 'K');
    } else if (unit_type == 'tap') {
        set_unit_type_sezimal_decimal(unit_type, 'tap', '°C');
    } else if (unit_type == 'agn') {
        set_unit_type_sezimal_decimal(unit_type, 'agn', 'J/K');
    } else if (unit_type == 'idn') {
        set_unit_type_sezimal_decimal(unit_type, 'idn', 'J/K/kg');
    } else if (unit_type == 'tln') {
        set_unit_type_sezimal_decimal(unit_type, 'tln', 'J/K/m3');
    } else if (unit_type == 'avx') {
        set_unit_type_sezimal_decimal(unit_type, 'Xavx', 'mAh');
    } else if (unit_type == 'dar') {
        set_unit_type_sezimal_decimal(unit_type, 'Tdar', 'A');
    } else if (unit_type == 'vbv') {
        set_unit_type_sezimal_decimal(unit_type, 'vbv', 'V');
    } else if (unit_type == 'ptr') {
        set_unit_type_sezimal_decimal(unit_type, 'ptr', 'Ω');
    } else if (unit_type == 'cln') {
        set_unit_type_sezimal_decimal(unit_type, 'cln', 'S');
    } else if (unit_type == 'prk') {
        set_unit_type_sezimal_decimal(unit_type, 'prk', 'H');
    } else if (unit_type == 'sam') {
        set_unit_type_sezimal_decimal(unit_type, 'sam', 'F');
    } else if (unit_type == 'abv') {
        set_unit_type_sezimal_decimal(unit_type, 'abv', 'Wb');
    } else if (unit_type == 'vtr') {
        set_unit_type_sezimal_decimal(unit_type, 'vtr', 'T');
    } else if (unit_type == 'prd') {
        set_unit_type_sezimal_decimal(unit_type, 'tprd', 'deg');
    } else if (unit_type == 'gol') {
        set_unit_type_sezimal_decimal(unit_type, 'gol', 'sr');
    } else if (unit_type == 'prt') {
        set_unit_type_sezimal_decimal(unit_type, 'dprt', '%');
    } else if (unit_type == 'atk') {
        set_unit_type_sezimal_decimal(unit_type, 'DXatk', 'GiB');
    } else if (unit_type == 'pvn') {
        set_unit_type_sezimal_decimal(unit_type, 'Xpvn', 'Mbps');
    } else {
        set_unit_type_sezimal_decimal(unit_type, '', '');
    };
};

function set_sezimal_unit(select) {
    localStorage.setItem('sezimal-calculator-unit', select.value);
    update_units_conversion();
};

function set_decimal_unit(select) {
    localStorage.setItem('sezimal-calculator-decimal-unit', select.value);
    update_units_conversion();
};

function set_unit_type_sezimal_decimal(unit_type, sezimal_unit, decimal_unit) {
    localStorage.setItem('sezimal-calculator-unit-type', unit_type);
    localStorage.setItem('sezimal-calculator-unit', sezimal_unit);
    localStorage.setItem('sezimal-calculator-decimal-unit', decimal_unit);

    hide_all_units();

    if (unit_type == 'units') {
        document.getElementById('unit-units-explanation').hidden = false;
        document.getElementById('toggle_units').innerHTML = '[ ↮ ]';
    } else if (unit_type == 'prefixes') {
        document.getElementById('unit-prefixes-explanation').hidden = false;
        document.getElementById('toggle_units').innerHTML = '[ ↮ ]';
    } else {
        document.getElementById('units-title').hidden = false;

        document.getElementById(`unit-${unit_type}-explanation`).hidden = false;
        document.getElementById(`unit-${unit_type}`).hidden = false;
        document.getElementById(`calculator-sezimal-unit-${unit_type}`).value = sezimal_unit;
        document.getElementById(`calculator-decimal-unit-${unit_type}`).value = decimal_unit;
    };

    update_units_conversion();
};

function update_units_conversion() {
    const sezimal_unit = localStorage.getItem('sezimal-calculator-unit');
    let decimal_unit = localStorage.getItem('sezimal-calculator-decimal-unit');

    console.log(decimal_unit.endsWith('day'), decimal_unit);
    if (decimal_unit.endsWith('day')) {
        const locale = localStorage.getItem('sezimal-calculator-locale');
        if (locale.startsWith('pt') || locale.startsWith('bz')) {
            decimal_unit = decimal_unit.replace('day', 'dia');
        };
    };

    document.getElementById('toggle_units').innerHTML = '[ ' + sezimal_unit + ' ↔ ' + decimal_unit + ' ]';
};

function hide_all_units() {
    document.getElementById('unit-units-explanation').hidden = true;
    document.getElementById('unit-prefixes-explanation').hidden = true;
    document.getElementById('units-title').hidden = true;

    document.getElementById('unit-ang-explanation').hidden = true;
    document.getElementById('unit-ang').hidden = true;
    document.getElementById('unit-avt-explanation').hidden = true;
    document.getElementById('unit-avt').hidden = true;
    document.getElementById('unit-pad-explanation').hidden = true;
    document.getElementById('unit-pad').hidden = true;
    document.getElementById('unit-kex-explanation').hidden = true;
    document.getElementById('unit-kex').hidden = true;
    document.getElementById('unit-ayt-explanation').hidden = true;
    document.getElementById('unit-ayt').hidden = true;
    document.getElementById('unit-drv-explanation').hidden = true;
    document.getElementById('unit-drv').hidden = true;
    document.getElementById('unit-gan-explanation').hidden = true;
    document.getElementById('unit-gan').hidden = true;
    document.getElementById('unit-veg-explanation').hidden = true;
    document.getElementById('unit-veg').hidden = true;
    document.getElementById('unit-tvr-explanation').hidden = true;
    document.getElementById('unit-tvr').hidden = true;
    document.getElementById('unit-bar-explanation').hidden = true;
    document.getElementById('unit-bar').hidden = true;
    document.getElementById('unit-dab-explanation').hidden = true;
    document.getElementById('unit-dab').hidden = true;
    document.getElementById('unit-kry-explanation').hidden = true;
    document.getElementById('unit-kry').hidden = true;
    document.getElementById('unit-xat-explanation').hidden = true;
    document.getElementById('unit-xat').hidden = true;
    document.getElementById('unit-gtk-explanation').hidden = true;
    document.getElementById('unit-gtk').hidden = true;
    document.getElementById('unit-tap-explanation').hidden = true;
    document.getElementById('unit-tap').hidden = true;
    document.getElementById('unit-agn-explanation').hidden = true;
    document.getElementById('unit-agn').hidden = true;
    document.getElementById('unit-idn-explanation').hidden = true;
    document.getElementById('unit-idn').hidden = true;
    document.getElementById('unit-tln-explanation').hidden = true;
    document.getElementById('unit-tln').hidden = true;
    document.getElementById('unit-avx-explanation').hidden = true;
    document.getElementById('unit-avx').hidden = true;
    document.getElementById('unit-dar-explanation').hidden = true;
    document.getElementById('unit-dar').hidden = true;
    document.getElementById('unit-vbv-explanation').hidden = true;
    document.getElementById('unit-vbv').hidden = true;
    document.getElementById('unit-ptr-explanation').hidden = true;
    document.getElementById('unit-ptr').hidden = true;
    document.getElementById('unit-cln-explanation').hidden = true;
    document.getElementById('unit-cln').hidden = true;
    document.getElementById('unit-prk-explanation').hidden = true;
    document.getElementById('unit-prk').hidden = true;
    document.getElementById('unit-sam-explanation').hidden = true;
    document.getElementById('unit-sam').hidden = true;
    document.getElementById('unit-abv-explanation').hidden = true;
    document.getElementById('unit-abv').hidden = true;
    document.getElementById('unit-vtr-explanation').hidden = true;
    document.getElementById('unit-vtr').hidden = true;
    document.getElementById('unit-prd-explanation').hidden = true;
    document.getElementById('unit-prd').hidden = true;
    document.getElementById('unit-gol-explanation').hidden = true;
    document.getElementById('unit-gol').hidden = true;
    document.getElementById('unit-prt-explanation').hidden = true;
    document.getElementById('unit-prt').hidden = true;
    document.getElementById('unit-atk-explanation').hidden = true;
    document.getElementById('unit-atk').hidden = true;
    document.getElementById('unit-pvn-explanation').hidden = true;
    document.getElementById('unit-pvn').hidden = true;
};
