/*
 * Author: Unekwu Shaibu
 * file name: Score Automation
 * Date:26/08/2022
 * Functions: 4
 * Language: Javascript 
 */


//grading function

function grader(score)
{
	if((score == "") || (score == " "))
		alert("You have entered a blank score, please enter a number");
	else if((score < 0) || (score > 100))
		alert('Scores should be between 0 and 100, please make sure you have typed a score in the stated range');
	else if((score >= 0) & (score < 40))
		return "F";
	else if((score >= 40) & (score <= 45))
		return "E";
	else if((score > 45) & (score < 50))
		return "D";
	else if((score >= 50) & (score < 60))
		return "C";
	else if((score >= 60) & (score <= 69))
		return "B";
	else if((score >= 70) & (score <= 100))
		return "A";
	else
		alert("The character you have entered is not a digit, please retype a valid digit. Thankyou.");
}

	
/*
 * totalOf_5nums functions-
 * (This is a local function)
 */

function total() 
{
      e = parseFloat(document.getElementById('en').value);
      m = parseFloat(document.getElementById('ma').value);
      c = parseFloat(document.getElementById('ch').value);
      b = parseFloat(document.getElementById('bi').value);
      f = parseFloat(document.getElementById('fr').value);

      var totalscore = e + m + c + b + f ;
      return totalscore;
}


// averageOf 5_nums

function average5(arg)
{
	var avrge = (arg/5);
	return avrge;
}


//getRemark function takes one arg.

function getRemarks(arg)
{ 	
	if((arg >= 70) & (arg <= 100))
		return 'You are a star!';
        else if((arg >= 60) & (arg < 70))
                return 'Proud of you!';
        else if((arg >= 50) & (arg < 60))
                return 'Fair result, you can do better.';
	else if ((arg >= 45) & (arg < 50))
		return 'There is room for improvement.';
	else if((arg > 39) & (arg < 45))
		return 'Poor result, you can do better.'
        else if((arg >= 0) & (arg <= 39))
                return 'You have disappointed your teacher.You are adviced to reseat this course.';
        else if ((arg > 100) || (arg < 0))
                return 'Error!, please ensure you have typed in the correct scores.';
        else
                return 'Error, please ensures all input fields are filled with the correct data.';
}

function emoojee(a)
{	
	document.getElementById('emoji').src="images/default.png";

	if((a >= 70) & (a <= 100))
		document.getElementById('emoji').src="A.png";
	else if((a >= 60) & (a < 70))
		document.getElementById('emoji').src = "B.png";
	else if((a >= 50) & (a < 60))
		document.getElementById('emoji').src = "C.png";
	else if ((a >= 45) & (a < 50))
		document.getElementById('emoji').src = "D.png";
	else if ((a > 39) & (a < 45))
		document.getElementById('emoji').src = "E.png";
	else if (a <= 39)
		document.getElementById('emoji').src = "F.png";
}











