  function printCalendar(date, divDestination) {
        var myOutput=document.getElementById(divDestination)
        myOutput.innerHTML=makeCalendar(date.getFullYear(), date.getMonth());
    }
    
    function nextMonth(date, divDestination) {
        date.setMonth(date.getMonth()+1);
        printCalendar(date, divDestination);
    }

    function prevMonth(date, divDestination) {
        date.setMonth(date.getMonth()-1);
        printCalendar(date, divDestination);
    }

    function test(divDestination){
        var myOutput=document.getElementById(divDestination)
        myOutput.innerHTML += eventmonth; //???
    }

    function leapYear(yr) { 
        if (yr < 1000) yr+=1900
        return((yr%4 == 0) && ((yr%100 == 0) || (yr%400 ==0)))
    }

    function startCol(width, height, color){
        return('<TD WIDTH=' + width + ' HEIGHT=' + height + '>' + '<FONT COLOR="' + color + '">');
    }

    function getHoliday(monthSelected,theday)
    {
        monthSelected = monthSelected + 1
        var holiday = ""
        var HolidayName = new Array (1, 1, "New Year's Day",7, 1, "Canada Day",12, 25, "Christmas Day",12, 26, "Boxing Day", 2,14,"Valentine's Day")
        for(var index = 0; HolidayName.length >= index; index++)
        {   
            if(HolidayName[index] == monthSelected && HolidayName[index+1] == theday)
            {
                holiday = HolidayName[index+2]
            }
        }
        return holiday
    
    }

    function makeCalendar(yr, mth)
    {
        var monthSelected = mth
        var months    = new Array("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")
        var days      = new Array(31, leapYear(yr)?29:28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        var weekDays  = new Array("Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat")

        var mthSz         = days[mth]
        var mthName       = months[mth]
        var firstDyofMnth = new Date(yr, mth, 1)
        var firstDay      = firstDyofMnth.getDay() + 1
        var numRows       = Math.ceil((mthSz + firstDay-1)/7)
        var mthNameHeight = 50

        var borderWidth   = 2
        var cellSpacing   = 4 
        var cellHeight    = 80 

        var hdrColor      = "midnightblue" 
        var hdrSz         = "+3" 
        var colWidth      = 100 

        var dayCellHeight = 25 
        var dayColor      = "black" 
        var dayCtr        = 1

        // Build the HTML Table 
        var txt = '<CENTER>'
        txt += '<TABLE BORDER=' + borderWidth + ' CELLSPACING=' + cellSpacing + '>' 

        //Show Month Name and Year
        txt += '<TH COLSPAN=7 HEIGHT=' + mthNameHeight + '>' 
        txt += '<FONT COLOR="' + hdrColor + '" SIZE=' + hdrSz + '>' 
        txt += mthName + ' ' + yr + '</FONT>' + '</TH>'

        // Show Days of the Week 
        txt += '<TR ALIGN="center" VALIGN="center">'
        for (var dy = 0; dy < 7; ++dy) {
            txt += startCol(colWidth, dayCellHeight, dayColor) + weekDays[dy] + '</FONT></TD>' 
        }
        txt += '</TR>'

        // Show Dates in Calendar
        for (var row=1; row <= numRows; ++row) 
        {
            txt += '<TR ALIGN="right" VALIGN="top">'
            for (var col = 1; col <= 7; ++col) 
            {
                if (((col < firstDay) && (row==1)) || (dayCtr>mthSz))
                    {txt += '<TD BGCOLOR="white"><BR></TD>'}
                else
                    {
                        var event = getHoliday(monthSelected, dayCtr)
                        txt += '<TD HEIGHT=' + cellHeight + '><FONT COLOR="' + dayColor + '"> <B>'
                        txt += dayCtr
                        txt += '</B></FONT><BR>' + event + '</TD>'
                        dayCtr++;
                    }       
            }
            txt += '</TR>'
        }
        // close all basic table tags and output txt string
        txt += '</TABLE></CENTER>'  
        return txt
        
    }      
    
//HTML    
//    <div align="center" id="divCalendar"></div>
//    <div align="center" id="myButtons">
//    <input type="button" onclick="test('divCalendar')" value="Say hi" />
//    <input type="button" onclick="prevMonth(myDate,'divCalendar')" value="Previous"/>
//    <input type="button" onclick="nextMonth(myDate,'divCalendar')" value="Next" />
//    <input type="button" onclick="printCalendar(myDate,'divCalendar')" value="Reload Calendar" />

//    <script src="/js/calendar.js"></script>
//    <script>
//        var myDate = new Date();
//        printCalendar(myDate, 'divCalendar');
//    </script>
