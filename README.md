# odoo web rpc tutorial
### How to read template input values examples
```js
odoo.define('theme_address.theme', function (require) {
    "use strict";

var Widget= require('web.Widget');
var widgetRegistry = require('web.widget_registry');

var changeTitle = function() {
        opp_name.value = value_input.value;
    };
    
var MyWidget = Widget.extend({

    template: 'sigPad',

    events: {
        'click .your_class': 'change_opp_name',
    },

    change_opp_name: function () {
        var opp_name = document.getElementById("o_field_input_21");
        var value_input = document.getElementById('value_input');
        var change_opp_name_button = document.getElementById('change_opp_name_button');
        var event = new Event('change');
        change_opp_name_button.addEventListener('change', changeTitle(), false);
        opp_name.dispatchEvent(event);
    }
});

widgetRegistry.add(
    'my_widget', MyWidget
);

return MyWidget;
```
```xml
<?xml version="1.0" encoding="utf-8"?>
<templates>
    <t t-name="sigPad">
        <div>
            <input type="text" id="value_input" class="form-control" style="max-width: 400px;  width: 150px"/>
            <input type="button" id="change_opp_name_button" class="your_class" value="Submit"/>
        </div>
    </t>
</templates>
```
