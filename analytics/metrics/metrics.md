# Metrics <!-- omit in toc -->

Examples and samples of custom metrics

## Contents <!-- omit in toc -->

* [Associate timeliness value based SLA adherence](#associate-timeliness-value-based-sla-adherence)
* [Calculate Due Date based on SLA](#calculate-due-date-based-on-sla)
* [Calculate Case Quality, based on previously occurred events](#calculate-case-quality-based-on-previously-occurred-events)
* [Associate SLA to Priority](#associate-sla-to-priority)

## Associate timeliness value based SLA adherence

This metrics associate a discrete (string) value to each case, depending on the comparison between a path (last “Order Approved” to last “Order Delivered”) and the related  “SLA” (in days):
* returns "ON TIME" if the path-time adhered within the SLA; 
* returns "LATE" if the path-time exceeded the SLA; 
* returns "ONGOING" if the last activity has not occurred for the case.

```javascript
var customMetric = {
    caseMetric: function(aCase) {
        var cron = 0;
        var SLA = 0;
        var delivered = 0;
        for (var k = 0; k < aCase.size(); k++) {
            var event = aCase.get(k);
            if (event.getEventClass() == 'Order Approved')
                cron = event.getStartTime();
            if (event.getEventClass() == 'Order Delivered') {
                cron = event.getStartTime() - cron;
                delivered = 1;
                SLA = event.getDoubleCustomAttributeValue('SLA');
            }
        }
        SLA = SLA * 24 * 60 * 60 * 1000;
        if (delivered == 0) return "ONGOING";
        else if (cron > SLA) return "LATE";
        else if (cron <= SLA) return "ON TIME";
        else return "ERROR";
    }
};
```

## Calculate Due Date based on SLA

This metrics associate a Due Date (date value) to each case, based on the case attribute “SLA”:
* Insert activity name where the SLA period starts

```javascript
var customMetric = {
    caseMetric: function(aCase) {
        var cron = 0;
        var SLA = 0;
        for (var k = 0; k < aCase.size(); k++) {
            var event = aCase.get(k);
            if (event.getEventClass() == 'Order Approved') {
                cron = event.getStartTime();
                SLA = event.getDoubleCustomAttributeValue('SLA');
            }
        }
        SLA = SLA * 24 * 60 * 60 * 1000;
        var Due_Date = cron + SLA;
        return new Date(Due_Date);
    }
};
```

## Calculate Case Quality, based on previously occurred events

This metrics associate a quality value (0-100) to each case, which would typically decrease if deviations occur.
In the provided example, the quality decreases by 7 every time an event which includes the word ‘Change’ occurs.

```javascript
var customMetric = {
    caseMetric: function(aCase) {
        var quality = 100;
        var changes = 0;
        for (var k = 0; k < aCase.size(); k++) {
            var event = aCase.get(k);
            var activity = event.getEventClass();
            if (activity.indexOf('Change') > -1)
                changes++;
        }
        quality -= changes * 7;
        return quality < 0 ? 0 : quality;
    }
};
```

## Associate SLA to Priority

This metrics associate an SLA (double value) to each case, based on the case attribute “priority”.
* Insert priority distinct values as if/else conditions
* Insert the corresponding SLA value, in hours

```javascript
var customMetric = {
    caseMetric: function(aCase) {
        var SLA_hours = 800;
        var event = aCase.get(aCase.size() - 1);
        var priority = event.getStringCustomAttributeValue('priority');
        if (priority == 'High') SLA_hours = 3;
        else if (priority == 'Medium') SLA_hours = 8;
        else SLA_hours = 800;
        return SLA_hours * 60 * 60 * 1000;
    }
};
```
