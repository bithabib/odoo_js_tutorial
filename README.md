# odoo web rpc tutorial
### 1. How to read template input values examples
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

### 2. FormController
```js
var FormController = require('web.FormController');
var ExtendFormController = FormController.include({
    saveRecord: function () {
        var res = this._super.apply(this, arguments);
        if(this.modelName == 'project.task'){
            var self = this;
            res.then(function(changedFields){
                console.log(changedFields);
                console.log(self.modelName);
                self.do_notify('title', 'message');
                // you can call a method on the server like this
                self._rpc({
                        model: self.modelName,
                        method: 'search_read',
                        fields: ['name'],
                        context: self.context,
                    }).then(function(result){
                        console.log('rpc result');
                        console.log(result);
                    })
            });
        }
        return res;
    }
});
```

```js
odoo.define('odoo_js_tutorial.odoo_tutorial', function (require) {
    'use strict';
    console.log('popup.js loaded');
    var FormController = require('web.FormController');

    var ExtendFormController = FormController.include({
        saveRecord: function (recordID) {
            
            var res = this._super.apply(this, arguments);
            console.log(res);
            if (this.modelName == 'odoo.tutorial'){
                console.log('saveRecord');
                console.log(recordID);
                this.do_notify('Success', 'Record Saved');
            }
            return res;
        }
    });

});
```

You also need to inherit the createRecord() method the same way.

A few notes:

the first console log line saying: ["name"] is the value of changedFields (I only changed the name of the task before hitting Save)
I was working on the project.task object but you can change that to sale.order :)
The official documentation is very helpful
