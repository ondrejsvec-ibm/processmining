# IBM Process Mining – (Java) Script Filters <!-- omit in toc -->

**Authors:**
F&O - IBM Operations - Digital Strategy – Process Mining Squad: Fjodor Geurink, Aline Mian Soares  

**Thanks to:**
The IBM SW Process Mining Team for their great material made available to all IBM´ers
F&O Process Mining Community Members for their feedback and testing

## Contents <!-- omit in toc -->

* [Introduction to Script Filters in IBM Process Mining](#introduction-to-script-filters-in-ibm-process-mining)
  * [The Filters section](#the-filters-section)
  * [4 Filter options](#4-filter-options)
  * [This document will cover:](#this-document-will-cover)
* [Hands-On Practice material and environment](#hands-on-practice-material-and-environment)
  * [Use Case – Fashion After Sales](#use-case--fashion-after-sales)
  * [IBM Process Mining Tool](#ibm-process-mining-tool)
* [(Java) Script writing Basics](#java-script-writing-basics)
  * [Script Filter section](#script-filter-section)
  * [Simplified Javascript](#simplified-javascript)
  * [Some Basic Java Code writing Rules](#some-basic-java-code-writing-rules)
  * [Error messages:](#error-messages)
  * [Boolean Data Type](#boolean-data-type)
  * [Greater / Less than IF-statements:](#greater--less-than-if-statements)
  * [Dates:](#dates)
  * [Ways to get opposite results:](#ways-to-get-opposite-results)
  * [Script Filter Limitations](#script-filter-limitations)
* [Flow - Keep case for specified activity / activities](#flow---keep-case-for-specified-activity--activities)
* [Flow - First / Start Activities](#flow---first--start-activities)
* [Flow - Activity Relation = Activity X eventually followed by Activity Y](#flow---activity-relation--activity-x-eventually-followed-by-activity-y)
* [Rework – Case with at least one rework (FLAT processes only).](#rework--case-with-at-least-one-rework-flat-processes-only)
* [Rework - Activity + Self Loops nr \> or \< than X](#rework---activity--self-loops-nr--or--than-x)
* [Time - Activities within a certain Time-Frame](#time---activities-within-a-certain-time-frame)
* [Time - Cases that are completely executed in a certain period](#time---cases-that-are-completely-executed-in-a-certain-period)
* [Specific – Maverick Buying](#specific--maverick-buying)

## Introduction to Script Filters in IBM Process Mining

### The Filters section

   
is where you can analyze the process while considering a limited subset of cases that answers to specific user requests. Some Examples:
* I only want to see all cases which did not start with Activity X
* I want to see all cases that have a rework done

### 4 Filter options

In IBM Process Mining there are 4 options how to set Filters:
 
1.	Filters = is a very handy, easy to use way where you can select various criteria. This option can cover many standard requests/situations already and is a good starting point.
2.	Outliers = are cases and activities whose performance is different from the average and you can decide to exclude them or set the filter to show only those and analyze them further.
3.	KPIs = is to filter and visualize cases violating in line with one or more of the selected KPI rules
4.	Script Filters = is dedicated to developers who intend on building code-based filters. Here you can write code as well there are some prebuild code templates available.
For options 1, 2 and 3 there is good education material available at: IBM Documentation – Filters
Option 4 is becoming more Technical already and that is why this document has been created to help newbees to Javascript writing to start playing around with these kind of Filters.

### This document will cover:

1.	A Quick introduction to Javascript writing and some basic principles to take into account
2.	Hands-On Practice material and environment
3.	Ready to be used cases which you can copy/paste into your script filter and run yourself. 
Most of these cases are taken from the IBM SW Process Mining team and which are available to you as well in this Box Folder: IBM Process Mining – Script Filter Repository.
We have taken the most common Filters and added additional information on how to manipulate and run your script filter, what are potential use-cases as well some more options how to modify the purpose of that filter.
Aim is to stay as simple and practical as possible to get started into working with such Javascript Filters.
Note: In IBM Process Mining you can also write scripts for Dashboards. Those are not handled in this document and a separate material will be made available later on.
The authors of this document are also not technical and are new to this field. The document has to be seen as newbees helping newbees by sharing lessons learned.

 

## Hands-On Practice material and environment

Best way to learn is by practicing in a real tool and with some real data. 
Some material is made available to us to do so.

### Use Case – Fashion After Sales

The IBM SW Process Mining team has a bunch of Labs available to practice. See this folder.
The basic case to get started with is the Fashion – After Sales one.
The package contains a challenge in case you want to do go for it. However for this script education we have only been using the Dataset included in that Lab. 
Suggested is to download that Dataset and upload it in the IBM Process Mining Tool. All ready-to-use Filter examples provided further down in this document are all using examples of that dataset.

### IBM Process Mining Tool

You will need to get access to either the real IBM Cloud Pak for Business Automation SW, or there is a test environment (named Fyre) available to us.
Getting access is pretty simple and how to do so can be found here and go to the Access section.

Happy Practising !!!
 

## (Java) Script writing Basics

### Script Filter section

The script filter section has the following 3 boxes on top:
 
1.	Filter Title = Is auto-populated and will show which Filter is being displayed / worked on. Here you can also rename your filter. 
2.	Filter Operation = here you can select to either ¨Include matched cases¨, so cases that are responding to the filter criteria you set up, or select the opposite ¨Exclude matched cases¨.
3.	Templates = has a drop-down menu with various filters in it:
    - Script Filter = is the filter that is active / you are working on. This option is only available in the Fyre test environment and not in the Cloud Pak for Business Automation module.
    - Basic Filter = is giving the minimum starting coding needed and from there on you can add on your own code or simply copy/paste ready-to-use filters there.
    - 3 pre-build templates that you can select from and can get started straight away:
    - Activity Relation = to see where activity X (eg: Order Line Created) is eventually followed by activity Y (eg: Invoice Registered).
    - Maverick Buying = to apply in a P2P (Procure to Pay) process and which will show all cases where an Order is created but no Purchase Order (PO). 
    - Receipt Matching = under investigation where and what for it is used

### Simplified Javascript

Javascript (JS) is a well-known and widely used programming language. You can write there code from managing simple queries and building simple databases to very complex programs. 
In IBM Process Mining there is a simplified version available to help us build Scripted Filters.
It is simplified, since most of the advanced set-up and coding stuff is done already for us, and we are just left with an editor page (a text kind of box) where we can write our filters.
However there is still some more advanced coding needed/visible, so when you want to create a brand new filter you get this content already:
 
There is no direct need to dive deeper into all that complex coding, but if you want you can explore the:
* IBM Documentation – Cloud Paks – Script Filter page with script elements explained
* IBM Process Mining – Tech Expert course which has some videos on Script writing

### Some Basic Java Code writing Rules

There are some basic principles you need to take into account or else the script will give errors:
* Top Down = the script will be read from top down, so keep that into account with {} and () usage
* Statement = each line.   ; semicolon is to close the line. It is like a full stop at the end of a sentence
* Body = is a set of statements and needs to be opened and closed with curly brackets / braces {  }
* Indent Lines = in the example above you see white spaces at the start of lines 2 to 7. These are not mandatory to have, but it is a good common practice so the code stays easy to use and read.
* Misspelling = it is key to not have misspellings, missing instructions, wrong use of capital vs. small letters etc. The query will not work. For example commands like var, return, if etc. are always small letters.

### Error messages:

IPM has an error messages warning system build in showing with red circles and yellow triangles when a programming error is made in the script. The symbol will come in front of the line where the error occurred. 
* One error can cause multiple lines to give an error message, so once you fix the issue, often the error messages for the other lines will disappear.
* If you type code and there is no error, suddenly you can see errors appearing in other lines. This is caused  for example because a body is not closed yet by having both brackets { } applied.

### Boolean Data Type

Is just creating a True or False decision and is used too build decision moments. If True than do xxx
In the Script Filter you will see actions like:

* `return true`
* `return false`

You can use these statements to get the opposite effect as well. So replace true with false and false  with true and you will get the opposite result.

### Greater / Less than IF-statements:

Are handy to include for example for: show me cases which have more than 3 reworks. 
You can use these symbols to get the opposite effect as well, like changing the greater than symbol into less than, so you will get all cases which have less than 3 reworks. 
Options available:
* `> 	greater than`
* `>=	greater than or equal to`
* `<	less than`
* `<=	less than or equal to`

### Dates:

Dates in IBM Process Mining are according to the milliseconds long number format.
This is done to enhance performance, so speed of running the query, since operations between numbers are faster than operations between objects.
To set the datetime in milliseconds you can use a date to milli second converter to calculate it. 
For example:
* 1614294000000 stands for the Date 26 february 2021 00:00 hours.
* 1615417200000 stands for the Date 11 march 2021 00:00 hours.

 

### Ways to get opposite results:

If you write a script to for example ¨include all cases that have condition X¨, there are various simple  ways to get the opposite result, so in this example ¨exclude all cases that have condition X¨.
1.	Easiest way: In the Script writing editor, on top you can select ¨Filter Operation¨. Select Exclude Matched Cases.
 
2.	Swap return true / return false to return false / return true in your script
 
3.	Change Greater than symbol > to Less than symbol < or vice versa

### Script Filter Limitations

There are some features not available (yet) and things to take into account:
* The script filter is run in a protected sandbox because of security reasons and therefore it is not possible to import/reference 3rd party libraries
* A script filter is slower than a native standard filter set up since there are more architectural layers to be executed. Basically the script is run for each case, so your data set has 100 cases, the script runs 100x. On small data sets this difference is not so big but it will become more clear with very large data sets.
 

## Flow - Keep case for specified activity / activities

**Used for:**
Keep cases for a specified activity.
Or keep the case for the specified activities, but do note that the results are and/or.

**Application example in Aftersales use-case**
Data-Filling is the most time-consuming activity in this process so we want to see only the cases which had as activity ¨Data Filling¨ and we can perform further filtering or root-case analysis on those.

**More Options:**
* to get the opposite effect, so excluding all these cases, Set ¨exclude matched cases¨ or swap the return true and return false lines
  
**Script:**
Action = Copy/paste script and change activities.
In case you want to select more than 1 activity, you need to add activities in this format: 
 `var activities= ['Ticket Creation','Data Filling'];`

```javascript
var activities = ['Data Filling'];

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

## Flow - First / Start Activities

**Used for:**
Keep cases where the first activity is one (or more) of those inserted in activities.
This will help you see the most common Start Activity and/or the ideal process start point.

**Application example in Aftersales use-case**
The Happy-path (ideal process) shows that the process starts with ¨Ticket Creation¨. You can keep those correctly started cases and see how that evolves afterwards. Or you can exclude those cases and see with which activities they started and decide if that is a proper start activity as well or if corrective actions need to be taken.

**More Options:**
* On the other hand, you can also exclude that activity and see which cases do start with an incorrect starting activity. Just select ¨Exclude matched cases¨, or swap return true and return false

**Script:**
Action = Copy/paste script and change activities
In case you want to select more than 1 activity, you need to add activities in this format:
 `var activities= ['Ticket Creation','Ticket Assigned'];`

```javascript
var activities = ['Ticket Creation'];
var filter = {
    keepTrace: function(trace) {
        start_activity = trace.get(0).getEventClass();
        if (activities.indexOf(start_activity) > -1)
            return true;
        else return false;
    }
};
```

## Flow - Activity Relation = Activity X eventually followed by Activity Y

**Used for:**
Keep the cases that have Activity X and which are eventually followed by Activity Y. 
So in the script example you will get all cases that have activity ¨Delivery Header Block¨ and which eventually also get activity ¨Goods Issue¨. 
Eventually means that either the Goods Issue comes directly after Delivery Header Block, or it comes some steps down the road.
The below example is for example good to see which cases were blocked, but eventually had Goods issued and it can help you start further investigating if that block was removed correctly or bypassed.

**Application example in Aftersales use-case**
This is a small process so not really relevant, but feel free to play around with it any way.

**More Options:**
* This filter can also be set within the standard Filter module by using the ¨Process Flow Pattern¨ option located on the bottom of the list.

**Script:**
Action = This script is an already available Template in the drop-down Script section. 
Just fill in the Activity or Activities that you need as first and eventual steps, where:
* srcNode = Source Node = first activity you want to include
* drsNode = Destination Node = the eventual next activity you want to include

```javascript
var srcNode = 'Delivery Header Block';
var dstNode = 'Goods Issue';

var filter = {
    keepTrace: function(trace) {
        var hasSource = false;
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (!hasSource && srcNode === event.getEventClass()) {
                hasSource = true;
            } else if (hasSource && dstNode === event.getEventClass()) {
                return true;
            }
        }
        return false;
    }
};
```

## Rework – Case with at least one rework (FLAT processes only).

**Used for:**
Selects all cases where at least 1 Rework or Self-Loop took place:
* A rework is when the same activity happens two times or more in a case. It does not matter when the 2nd (or 3rd) time takes place in the same case. 
* A Self-Loop is a Rework type, but the same activity happens straight after the same activity. So for example ¨Data Filling¨ is followed directly by ¨Data Filling¨.

**Application example in Aftersales use-case**
When you run the below filter in the Aftersales use-case you will directly see that there are 125 cases where the ¨Ticket Assignment¨ took place 2 or more times in a case. This could mean re-assigning to somebody else, which often leads to delay in response.

**More Options:**
* In case you want to swap this, so only see all cases with no Rework/Self-Loop, just select ¨Exclude matched cases¨, or swap return true and return false

**Script:**
Action = Copy/Paste script, no additional modification is needed

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

## Rework - Activity + Self Loops nr > or < than X

**Used for:**
Selects 1 specific activity and will filter all cases that have more than X self-loops. 
A Self-loop is when an activity is followed directly by the same activity, eg: Ticket assignment is followed by Ticket assignment.

**Application example in Aftersales use-case**
A self-loop can happen if for example an employee assigns a case to the same status (=activity) again. However if this happens more often there is a problem and investigation needs to be done why the case is over and over set to the same status (activity). 
In the example below gives all cases where the activity ¨Ticket Assignment¨ has more than 4 self-loops.

**More Options:**
* In case you want more or equal than, just change the count > SLnum into count >= SLnum

**Script:**
Action = Copy/Paste script and fill-in fields marked

```javascript
var filter = {
    keepTrace: function(trace) {
        var count = 0;
        // to be changed
        var SLnum = 4;
        // to be changed
        var activity = "Ticket Assignment";
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            if (event.getEventClass() == activity)
                if (k > 0 && trace.get(k - 1).getEventClass() == activity) {
                    count++;
                    if (count > SLnum)
                        return true;
                }
        }
        return false;
    }
};
```

## Time - Activities within a certain Time-Frame

**Used for:**
Keep the case if at least one of the specified activities occurred between the specified date times.

**Application example in Aftersales use-case**
In this example we will see all cases that have as activity ¨Data Filling¨ done within the time-frame 26 feb 2021 and 11 march 2021. This filtering by time-frame can  be handy if you know that there were delivery issues, personnel issues or risk issues in a certain time-frame and analyze those further. 

**Script:**
Action = Copy/Paste script, fill in the Activity or Activities + make sure to set the datetime in milliseconds (use a date to milli second converter to calculate it). 
In below example the :
* 1614294000000 stands for the Date 26 february 2021 00:00 hours.
* 1615417200000 stands for the Date 11 march 2021 00:00 hours.

```javascript
var activities = ['Data Filling'];
date_low = 1614294000000;
date_up = 1615417200000;
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

## Time - Cases that are completely executed in a certain period

*Gives generic error… need to fix this*

**Used for:**
This filter will give all cases that are FULLY completed within the time frame you specify. 
So ALL activities from beginning to end within a case are handled in that period. So if you select 2nd quarter 2021, you will get all cases that have their first activity up to the last activity being executed within Q2 2021.

**Application example in Aftersales use-case**
x

**More Options:**
* This filter can also be set within the standard Filter module by using the ¨Event Attribute¨ option located on the top of the list, select from the drop-down the Process attribute and select the period you want to include. Don´t forget to enable the ¨Bound Time¨ toggle since that will give you all completed cases in that period.

**Script:**
Action = 

```javascript
var MIN_TIME = new Date(2021, 01, 01).getTime();
var MAX_Time = new Date(2021, 02, 01).getTime();

var filter = {
    keepTrace: function(trace) {
        var start = null;
        var end = null;
        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            start = (k === 0) ? event.getStartTime() : Math.min(start.event.getStartTime());
            end = (K === O) ? event.getEndTime() : Math.max(end, event.getEndTime());

        }
        return true;
    }
};
```

              

## Specific – Maverick Buying

**Used for:**
Maverick Buying is when goods, parts or materials are bought by an employee not following the formal buying channels and procedures in a company.
This can be a simple error by the employee by not knowing or having followed the process and this can for example result for the customer to get the full market price and not a discount (or other incentives) for volume they might have.
But it could also be malicious behaviour by the employee and buy outside the formal channels and get financial compensation (or other kind of benefits) from the supplier.
The logic for querying is to show all Orders which do not have a Purchase Requisition against it.

**Application example in Aftersales use-case**
Is not applicable in this small process of ticket handling. This would more often be used in a P2P (Procure to Pay) process.
More Options:
* Invoice without an Order = this could be possible to do, but in general this is not the case. An invoice should be based on a sale, so an order.
  
**Script:**
Action = This script is an already available Template in the drop-down Script section. 
Just fill in the Activity or Activities that you need

```javascript
var PURCH_REQ_CREATION = 'Purchase Req Creation';
var PURCH_REQ_CONFIRM = 'Purchase Req Confirmed';
var PURCH_ORDER_CREATION = 'Purchase Order Creation';

var filter = {
    keepTrace: function(trace) {

        var reqCreationCount = 0;
        var reqConfirmationCount = 0;
        var orderCreated = false;

        for (var k = 0; k < trace.size(); k++) {
            var event = trace.get(k);
            var eventClass = event.getEventClass();

            if (eventClass === PURCH_ORDER_CREATION) {
                orderCreated = true;
            } else if (eventClass === PURCH_REQ_CREATION) {
                reqCreationCount++;
            } else if (eventClass === PURCH_REQ_CONFIRM) {
                reqConfirmationCount++;
            }
        }
        return (orderCreated === true) && (reqCreationCount !== reqConfirmationCount);
    }
};
```
