# Shared Filters <!-- omit in toc -->
* [Rolling Filters](#rolling-filters)
  * [Keep all the cases started X days before today.](#keep-all-the-cases-started-x-days-before-today)
  * [Keep all the cases where a specific activity occurred X days before today.](#keep-all-the-cases-where-a-specific-activity-occurred-x-days-before-today)
  * [Keep all the cases where a specific activity occurred X days before today.](#keep-all-the-cases-where-a-specific-activity-occurred-x-days-before-today-1)
  * [Keep all the cases where ‘Invoice Registered’ occurred and on that activity the DUE\_DATE attribute value is \> today’s data + X days (tolerance).](#keep-all-the-cases-where-invoice-registered-occurred-and-on-that-activity-the-due_date-attribute-value-is--todays-data--x-days-tolerance)
* [Rework Filters](#rework-filters)
  * [Exclude case if, for a specified activity, the number of self-loops is \> than the specified threshold.](#exclude-case-if-for-a-specified-activity-the-number-of-self-loops-is--than-the-specified-threshold)
  * [Exclude the case if there is a rework for a specified activity, except for self-loops (self-loops should not be excluded).](#exclude-the-case-if-there-is-a-rework-for-a-specified-activity-except-for-self-loops-self-loops-should-not-be-excluded)
  * [Keep the case if at least a rework occurred (FLAT processes only).](#keep-the-case-if-at-least-a-rework-occurred-flat-processes-only)
* [Resource Filters](#resource-filters)
  * [Keep the case if the 2 specified activities are performed by the same resource.](#keep-the-case-if-the-2-specified-activities-are-performed-by-the-same-resource)
  * [Keep the case if the 2 specified activities are performed by the same resource.](#keep-the-case-if-the-2-specified-activities-are-performed-by-the-same-resource-1)
  * [Keep the case if the specified activity is performed by the specified resource.](#keep-the-case-if-the-specified-activity-is-performed-by-the-specified-resource)
  * [Keep the cases where 2 or more different resources are involved.](#keep-the-cases-where-2-or-more-different-resources-are-involved)
  * [Keep the cases where the Role field is always empty (for all the case’s activities).](#keep-the-cases-where-the-role-field-is-always-empty-for-all-the-cases-activities)
* [Or Filters on Contextual Data](#or-filters-on-contextual-data)
  * [Specify the activity on which you want to perform the check.](#specify-the-activity-on-which-you-want-to-perform-the-check)
  * [Keep the case if, in at least one of its events, the attribute MATERIAL has one of the values specified inside materials.](#keep-the-case-if-in-at-least-one-of-its-events-the-attribute-material-has-one-of-the-values-specified-inside-materials)
  * [Keep the case when the Contextual Data has one of the specified values.](#keep-the-case-when-the-contextual-data-has-one-of-the-specified-values)
  * [Keep the case if the specified activity is performed by one of the specified roles.](#keep-the-case-if-the-specified-activity-is-performed-by-one-of-the-specified-roles)
  * [Keep the case if one of the specified attributes has one of the specified values.](#keep-the-case-if-one-of-the-specified-attributes-has-one-of-the-specified-values)
* [Or Filters on Activity](#or-filters-on-activity)
  * [Keep the case if at least one of the specified activities occurred between the specified datetimes.](#keep-the-case-if-at-least-one-of-the-specified-activities-occurred-between-the-specified-datetimes)
  * [Keep the case if at least one of the specified activities occurred.](#keep-the-case-if-at-least-one-of-the-specified-activities-occurred)
  * [Keep cases where the first activity is one of those inserted in activities.](#keep-cases-where-the-first-activity-is-one-of-those-inserted-in-activities)
* [Or Filters on Activity Flows](#or-filters-on-activity-flows)
  * [CASES THAT SHOULD BE CLOSED BUT THAT ARE REOPENED](#cases-that-should-be-closed-but-that-are-reopened)
* [Operator Filters](#operator-filters)
  * [Keep the case if the ORDER\_HEADER\_AMOUNT is \> than the specified threshold.](#keep-the-case-if-the-order_header_amount-is--than-the-specified-threshold)
  * [Keep the invoices with higher amount compared to the respective orders (amount mismatch).](#keep-the-invoices-with-higher-amount-compared-to-the-respective-orders-amount-mismatch)
* [Null Contextual Data Filters](#null-contextual-data-filters)
  * [Only cases where the attribute has empty value across all the case’s activities are kept.](#only-cases-where-the-attribute-has-empty-value-across-all-the-cases-activities-are-kept)
  * [Keep only cases where the attribute has empty value for at least one case’s activity.](#keep-only-cases-where-the-attribute-has-empty-value-for-at-least-one-cases-activity)
* [Data Filters](#data-filters)
  * [Keep the cases started ended after the specified datetime custom field.](#keep-the-cases-started-ended-after-the-specified-datetime-custom-field)
  * [Keep the cases started after the specified datetime custom field.](#keep-the-cases-started-after-the-specified-datetime-custom-field)
  * [Keep the cases started after the specified datetime.](#keep-the-cases-started-after-the-specified-datetime)
  * [Keep the cases started between X and Y days after the specified datetime custom field.](#keep-the-cases-started-between-x-and-y-days-after-the-specified-datetime-custom-field)
  * [Keep cases that, in the specified datetime, are transitioning to the specified activity.](#keep-cases-that-in-the-specified-datetime-are-transitioning-to-the-specified-activity)
* [Case Length Filters](#case-length-filters)
  * [Keep the case if its number of activities is \<= than the specified number](#keep-the-case-if-its-number-of-activities-is--than-the-specified-number)

## Rolling Filters

### Keep all the cases started X days before today.

Day by day, the filter will get updated (warning: it could be necessary to work on the process to refresh the cache).

```javascript
var X = 30; //how many days you want to consider?

var today = new Date().getTime();
msback = X * 24 * 60 * 60 * 1000;

var filter = {
    keepTrace: function(trace) {
        if (trace.get(0).getStartTime() < (today - msback))
            return false;
        else return true;
    }
};
```

### Keep all the cases where a specific activity occurred X days before today.

The filter has tolerance on the week: e.g. if “today - X days” is Friday, all the cases occurred in that week are kept (therefore, starting from Monday of the same week).

Day by day, the filter will get updated (warning: it could be necessary to work on the process to refresh the cache).

```javascript
var X = 30; //how many days you want to consider?
var act = 'Order Information';

var today = new Date().getTime();
var mondayOffset = new Date().getDay() - 1;
if (mondayOffset == -1)
    mondayOffset = 6;
mondayOffset = mondayOffset - 7;
var msback = (X - mondayOffset) * 24 * 60 * 60 * 1000;

var filter = {
    keepTrace: function(trace) {
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (event.getEventClass() == act && event.getStartTime() > (today - msback))
                return true;
        }
        return false;
    }
};
```

### Keep all the cases where a specific activity occurred X days before today.

Day by day, the filter will get updated (warning: it could be necessary to work on the process to refresh the cache).

```javascript
var X = 30; //how many days you want to consider?
var act = 'Order Information';

var today = new Date().getTime();
msback = X * 24 * 60 * 60 * 1000;

var filter = {
    keepTrace: function(trace) {
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (event.getEventClass() == act && event.getStartTime() < (today - msback))
                return true;
        }
        return false;
    }
};
```

### Keep all the cases where ‘Invoice Registered’ occurred and on that activity the DUE_DATE attribute value is > today’s data + X days (tolerance).

In other words, this filter shows the invoices which are soon going to be overdue. 
Usually, this filter should be combined with another filter “Exclude activity = ‘Invoice Cleared’”.

Day by day, the filter will get updated (warning: it could be necessary to work on the process to refresh the cache).

```javascript
var today = new Date().getTime();
daysfwd = 3;
daysfwdms = daysfwd * 24 * 60 * 60 * 1000;

var filter = {
    keepTrace: function(trace) {
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (event.getEventClass() == 'Invoice Registered')
                if (event.getLongAttributeValue('attr-custom-DUE_DATE') > (today + daysfwdms))
                    return true;
                else return false;
        }
        return false;
    }
};
```

## Rework Filters

### Exclude case if, for a specified activity, the number of self-loops is > than the specified threshold.

```javascript
var filter = {
    keepTrace: function(trace) {
        var count = 0;
        var SLnum = 5;
        var activity = "DTU - RECEIVE - WRAP - Assegnazione Impresa";
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (event.getEventClass() == activity)
                if (k > 0 && trace.get(k - 1).getEventClass() == activity) {
                    count++;
                    if (count > SLnum)
                        return false;
                }
        }
        return true;
    }
};
```

### Exclude the case if there is a rework for a specified activity, except for self-loops (self-loops should not be excluded).

```javascript
var filter = {
    keepTrace: function(trace) {
        var activities = [];
        var firstFound = 0;
        var selfLoop = 0;
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            var activity = event.getEventClass();
            if (activity == 'In Pianificazione IT') {
                if (activities.indexOf(activity) == -1) {
                    activities.push(activity);
                    firstFound = 1;
                    continue;
                } else {
                    if (firstFound == 1)
                        selfLoop = 1;
                    else return false;
                }
            }
            if (activity != 'In Pianificazione IT')
                firstFound = 0;
        }
        return true;
    }
};
```

### Keep the case if at least a rework occurred (FLAT processes only).

```javascript
var filter = {
    keepTrace: function(trace) {
        var activities = [];
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            var activity = event.getEventClass();
            if (activities.indexOf(activity) == -1)
                activities.push(activity);
            else {
                return true;
            }
        }
        return false;
    }
};
```

## Resource Filters

### Keep the case if the 2 specified activities are performed by the same resource.

This filter is usable only for FLAT processes.

```javascript
var act1 = 'Invoice Registered';
var act2 = 'Invoice Cleared';

var filter = {
    keepTrace: function(trace) {
        var res1 = 'res1';
        var res2 = 'res2';
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            var activity = event.getEventClass();
            if (activity == act1)
                res1 = event.getResource();
            if (activity == act2)
                res2 = event.getResource();
        }
        if (res1 == res2)
            return true;
        else return false;
    }
};
```

### Keep the case if the 2 specified activities are performed by the same resource.

This filter is suitable for multilevel processes: insert as attr-process-X the subprocess index the activity refers to (note: it is not possible to check 2 activities of different subprocesses).
E.g.. P2P:

* Contract → attr-process-1
* Requisition → attr-process-2
* Order → attr-process-3
* Receipt → attr-process-4
* Invoice → attr-process-5

```javascript
var act1 = 'Purchase Order Line Creation';
var act2 = 'Purchase Order Released';

var filter = {
    keepTrace: function(trace) {
        var res1 = 'res1';
        var res2 = 'res2';
        var id1 = 'id1';
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            var activity = event.getEventClass();
            if (activity == act1 && event.getResource() != '') {
                res1 = event.getResource();
                id1 = event.getStringAttributeValue('attr-process-3');
            }
            if (activity == act2 && id1 == event.getStringAttributeValue('attr-process-3') && event.getResource() != '') {
                res2 = event.getResource();
                if (res1 == res2)
                    return true;
            }
        }
        return false;
    }
};
```

### Keep the case if the specified activity is performed by the specified resource.

```javascript
var filter = {
    keepTrace: function(trace) {
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            var act = event.getEventClass();
            if (act == 'Payment Service Closure') {
                var risorsa = event.getResource();
                if (risorsa == 'UT00844')
                    return true;
            }
        }
        return false;
    }
};
```

### Keep the cases where 2 or more different resources are involved.

```javascript
var filter = {
    keepTrace: function(trace) {
        resource1 = trace.get(0).getResource();
        for (var k = 1; k < trace.size(); k++) {
            var event = trace.get(k);
            if (event.getResource() != resource1)
                return true;
        }
        return false;
    }
};
```

### Keep the cases where the Role field is always empty (for all the case’s activities).

```javascript
var filter = {
    keepTrace: function(trace) {
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (event.getRole() != '')
                return true;
        }
        return false;
    }
};
```

## Or Filters on Contextual Data

### Specify the activity on which you want to perform the check.

The filter performs checks on one or more specified attributes and excludes the case if at least one of them contains a specified value (each attribute may have its own value to check).
This template shows also how to convert an attribute to upper case, for a case insensitive check.

```javascript
var filter = {
    keepTrace: function(trace) {
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            var act = event.getEventClass();
            if (act == 'Invoice Registered') {
                var inv_vendor_id = event.getStringAttributeValue("attr-custom-INVOICE_ID_VENDOR");
                inv_vendor = inv_vendor.toUpperCase();
                if (inv_vendor.indexOf('BLANKET') != -1)
                    return false;
                var inv_vendor = event.getStringAttributeValue("attr-custom-INVOICE_VENDOR_NAME");
                if (inv_vendor_id.indexOf('510_K') != -1)
                    return false;
                return true;
            }
        }
        return true;
    }
};
```

### Keep the case if, in at least one of its events, the attribute MATERIAL has one of the values specified inside materials.

```javascript
var materials = ['Iron', 'Still', 'Glass'];

var filter = {
    keepTrace: function(trace) {
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (materials.indexOf(event.getStringAttributeValue('attr-custom-MATERIAL')) > -1)
                return true;
        }
        return false;
    }
};
```

### Keep the case when the Contextual Data has one of the specified values.

The check is made when a specific activity is performed.

```javascript
var blanket_vendors = [
    'VND0001',
    'VND0002',
    'VND0003'
];

var filter = {
    keepTrace: function(trace) {
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (event.getEventClass() == 'Purchase Order Line Creation') {
                if (blanket_vendors.indexOf(event.getStringAttributeValue('attr-custom-ORDER_VENDOR_NAME')) > -1)
                    return true;
            }
        }
        return false;
    }
};
```

### Keep the case if the specified activity is performed by one of the specified roles.

```javascript
var roles = ['APPLICANT', 'DIRECTOR'];

var filter = {
    keepTrace: function(trace) {

        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (event.getEventClass() == 'Network Service Closure')
                if (roles.indexOf(event.getRole()) > -1)
                    return true;
        }
        return false;
    }
};
```

### Keep the case if one of the specified attributes has one of the specified values.

```javascript
var values = ['A', 'B', 'C'];

var filter = {
    keepTrace: function(trace) {
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (agencies.indexOf(event.getStringAttributeValue('attr-custom-INVOICE_AGENCY_NAME')) > -1)
                return true;
            if (agencies.indexOf(event.getStringAttributeValue('attr-custom-ORDER_AGENCY_NAME')) > -1)
                return true;
            if (agencies.indexOf(event.getStringAttributeValue('attr-custom-RECEIPT_AGENCY_NAME')) > -1)
                return true;
            if (agencies.indexOf(event.getStringAttributeValue('attr-custom-REQ_AGENCY_NAME')) > -1)
                return true;
        }
        return false;
    }
};
```

## Or Filters on Activity

### Keep the case if at least one of the specified activities occurred between the specified datetimes.

Note: make sure to set the datetime in milliseconds ([use a date to millisecond converter](https://codechi.com/dev-tools/date-to-millisecond-calculators/) to calculate it).

```javascript
var activities = ['ActivityA', 'ActivityB'];
// datetimes
date_low = 1546297200000;
date_up = 1577833200000;

var filter = {
    keepTrace: function(trace) {
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (activities.indexOf(event.getEventClass()) > -1)
                if (event.getStartTime() >= date_low && event.getStartTime() <= date_up)
                    return true;
                else return false;
        }
        return false;
    }
};
```

### Keep the case if at least one of the specified activities occurred.

```javascript
var activities = ['ActivityA', 'ActivityB'];

var filter = {
    keepTrace: function(trace) {
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (activities.indexOf(event.getEventClass()) > -1)
                return true;
        }
        return false;
    }
};
```

### Keep cases where the first activity is one of those inserted in activities.

```javascript
var activities = ['Requisition Created', 'Order Item Created'];

var filter = {
    keepTrace: function(trace) {
        start_activity = trace.get(0).getEventClass();
        if (activities.indexOf(start_activity) > -1)
            return true;
        else return false;
    }
};
```

## Or Filters on Activity Flows

### CASES THAT SHOULD BE CLOSED BUT THAT ARE REOPENED

```javascript
var filter = {
    keepTrace: function(trace) {
        var finalActivities = ['CLOSED', 'RESOLVED'];
        var reopenedActivities = ['OPENED', 'ON_GOING'];
        var shouldbeclosed = false;

        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);

            if (finalActivities.indexOf(event.getEventClass() > -1)) {
                shouldbeclosed = true;
            } else if (reopenedActivities.indexOf(event.getEventClass() > -1) && (shouldbeclosed === true)) {
                return true;
            }
        }
        return false;
    }
};
```

## Operator Filters

### Keep the case if the ORDER_HEADER_AMOUNT is > than the specified threshold.

The check is performed on a specific activity.
Note: the specified attribute has to be mapped as numeric.

```javascript
// threshold
var AmountTh = 25000;

var filter = {
    keepTrace: function(trace) {
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            var act = event.getEventClass();
            // specific activity
            if (act == 'Purchase Order Line Creation') {
                var order_am = event.getDoubleAttributeValue("attr-custom-ORDER_HEADER_AMOUNT");
                if (order_am < AmountTh) {
                    return false;
                }
            }
        }
        return true;
    }
};
```

### Keep the invoices with higher amount compared to the respective orders (amount mismatch).

The check is performed on the invoice bridge activity.
A tolerance is applied to consider changes in currency conversion rates.

```javascript
var filter = {
    keepTrace: function(trace) {
        var order_amount = 0;
        var invoice_amount = 0;
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            var act = event.getEventClass();
            // invoice bridge activity.
            if (act == 'Invoice Registered') {
                order_amount += event.getDoubleAttributeValue("attr-custom-ORDER_LINE_AMOUNT");
                invoice_amount = event.getDoubleAttributeValue("attr-custom-INVOICE_HEADER_AMOUNT");
            }
        }
        // 0.99 is the tolarance
        if (invoice_amount * 0.99 > order_amount)
            // 0.99 is to allow some tolerance on the currency conversion
            return true;
        else return false;
    }
};
```

## Null Contextual Data Filters

### Only cases where the attribute has empty value across all the case’s activities are kept.

```javascript
var filter = {
    keepTrace: function(trace) {
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (event.getStringAttributeValue('attr-custom-INVOICE_REVERSED') != '')
                return false;
        }
        return true;
    }
};
```

### Keep only cases where the attribute has empty value for at least one case’s activity.

```javascript
var filter = {
    keepTrace: function(trace) {
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (event.getStringAttributeValue('attr-custom-COUNTRY') == '')
                return true;
        }
        return false;
    }
};
```

## Data Filters

### Keep the cases started ended after the specified datetime custom field. 

The custom field’s value is detected on the last event of the case.

```javascript
var filter = {
    keepTrace: function(trace) {
        if (trace.get(trace.size() - 1).getStartTime() - trace.get(trace.size() - 1).getLongAttributeValue('attr-custom-DUE_DATE') > 0)
            return true;
        else
            return false;
    }
};
```

### Keep the cases started after the specified datetime custom field. 

The custom field’s value is detected on the first event of the case.

```javascript
var filter = {
    keepTrace: function(trace) {
        if (trace.get(0).getStartTime() - trace.get(0).getLongAttributeValue('attr-custom-INVOICE_DATE') > 0)
            return true;
        else
            return false;
    }
};
```

### Keep the cases started after the specified datetime.

Note: make sure to set the datetime in milliseconds (use a date to millisecond converter to calculate it).

```javascript
var date = 1567288800000;

var filter = {
    keepTrace: function(trace) {
        if (trace.get(0).getStartTime() >= date)
            return true;
        else
            return false;
    }
};
```

### Keep the cases started between X and Y days after the specified datetime custom field.

The custom field’s value is detected on the first event of the case.
Note: X is the lower bound, Y is the upper.

```javascript
days_X = 30;
days_Y = 60;

days_X_ms = days_X * 24 * 60 * 60 * 1000;
days_Y_ms = days_Y * 24 * 60 * 60 * 1000;

var filter = {
    keepTrace: function(trace) {
        if (trace.get(0).getStartTime() - trace.get(0).getLongAttributeValue('attr-custom-INVOICE_DATE') >= days_X_ms && trace.get(0).getStartTime() - trace.get(0).getLongAttributeValue('attr-custom-INVOICE_DATE') < days_Y_ms)
            return true;
        else
            return false;
    }
};
```

### Keep cases that, in the specified datetime, are transitioning to the specified activity.

Note: make sure to set the datetime in milliseconds (use a date to millisecond converter to calculate it).

```javascript
var today = new Date().getTime();
var REFERENCE_TIME = 1551253380000;

var filter = {
    keepTrace: function(trace) {
        var previousOk = false;
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (event.getStartTime() < REFERENCE_TIME) {
                previousOk = true;
            } else {
                if (previousOk && event.getEventClass() === 'EROGAZIONE INCOMPLETA') {
                    return true;
                } else {
                    return false;
                }
            }
        }
        return false;
    }
};
```

## Case Length Filters

### Keep the case if its number of activities is <= than the specified number

```javascript
var filter = {
    keepTrace: function(trace) {
        if (trace.size() <= 1) return true;
        else return false;
    }
};
```
