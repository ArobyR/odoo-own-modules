'use strict';
odoo.define('custom.cart_qty_check', function (require) {

    var ajax = require('web.ajax');
    var cart_button = $('#add_to_cart');

    var _onButton = function (e) {
//        throw "Check";
//        ajax.jsonRpc()
        console.log("this happened")
    };

    cart_button.click(_onButton);

});