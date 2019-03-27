odoo.define('website.editor', function (require) {
'use strict';
var Model = require('web.Model');
var Widget = require('web.Widget');
var base = require('web_editor.base');
var editor = require('web_editor.editor');
var widget = require('web_editor.widget');
var website = require('website.website');


website.TopBar.include({
    init: function  (){
        alert('primero')
    },
    start: function () {
        this.status_view = new website.TopBarCustomize();
        var def = this.status_view.attachTo($('#customize-menu'));
        console.log($.when(this._super(), def))
        return $.when(this._super(), def);
    }
});


});
