/**
 * 
 * Lab: Human Dynamics Lab
 * Supervisor: Dazza Greenwood
 * Scripts written by: Shreyash Agrawal (MIT UROP)
 * 
 **/

function makeForm2()
{
  var spreadSheet = SpreadsheetApp.openById('1c_glzdHTinakGJNCJZsWh18e1HLLJa9fOaZjrCoa4is');
  var ss = spreadSheet.getSheetByName('Form Responses 1');
  var form = FormApp.openById('1kDUO5JyASBCASNYiNS-ReWU-O8FqhhtobkeLfoWUM4U');
  form.setTitle('Rate Proposed Law');
  while(form.getItems().length > 2)
  {
    form.deleteItem(form.getItems()[2]);
  }
  
  for (var i = 2; i<=getFirstEmptyRow('Form Responses 1'); i++)
  {
    var item = form.addScaleItem();
    item.setTitle(ss.getRange("B" + i).getValue()).setBounds(1, 5);
  }
}

function makeForm3()
{
  var spreadSheet = SpreadsheetApp.openById('1c_glzdHTinakGJNCJZsWh18e1HLLJa9fOaZjrCoa4is');
  var ss = spreadSheet.getSheetByName('Form Responses 2');
  var form = FormApp.openById('1d2eFekGlG7gN4p2dTrV0eRSLZM7GLBhwacXpF67fXQU');
  form.setTitle('What Success Metrics should be used for the Proposed Law: '+ topLaw());
}

function makeForm4()
{
  var spreadSheet = SpreadsheetApp.openById('1c_glzdHTinakGJNCJZsWh18e1HLLJa9fOaZjrCoa4is');
  var ss = spreadSheet.getSheetByName('Form Responses 3');
  var form = FormApp.openById('1CT8BZBZ19qMOWmOGRlkORZMWUrvQCu0qWaxrMnTyLBs');
  form.setTitle('Rate Outcomes and Measures');
  while(form.getItems().length > 2)
  {
    form.deleteItem(form.getItems()[2]);
  }
  for (var i = 2; i<=getFirstEmptyRow('Form Responses 3'); i++)
  {
    var item = form.addScaleItem();
    item.setTitle('Rate Outcome: ' + ss.getRange("D" + i).getValue()).setBounds(1, 5);
    
    var item2 = form.addScaleItem();
    item2.setTitle('Rate Measurement of Outcome: ' + ss.getRange("E" + i).getValue()).setBounds(1, 5);
  }
}

function makeDoc()
{
  var doc = DocumentApp.openById('1erhVTdXDT8EK3ZnlI5Rlkh5mp0rUFeHqm88PR23DjEo');
  var body = doc.getBody();
  body.clear();
  body.appendParagraph('Top Law: ' + topLaw());
  body.appendParagraph('Top Outcome: ' + topOutcome());
  body.appendParagraph('Top Measurement of Outcome: ' + topMeasure());
}

function reset()
{
  var spreadSheet = SpreadsheetApp.openById('1c_glzdHTinakGJNCJZsWh18e1HLLJa9fOaZjrCoa4is');
  var ss1 = spreadSheet.getSheetByName('Form Responses 1');
  var form1 = FormApp.openById('1vxMk19sru7dYoC_2TVK6JbfwBq1l3KI2-ZIjTopcrFk');
  form1.deleteAllResponses();
  if (ss1.getLastRow() > 1)
  {
    ss1.deleteRows(2, ss1.getLastRow()-1);
  }
  
  var ss2 = spreadSheet.getSheetByName('Form Responses 2');
  var form2 = FormApp.openById('1kDUO5JyASBCASNYiNS-ReWU-O8FqhhtobkeLfoWUM4U');
  form2.deleteAllResponses();
  if (ss2.getLastRow() > 1)
  {
    ss2.deleteRows(2, ss2.getLastRow()-1);
  }
  while(form2.getItems().length > 2)
  {
    form2.deleteItem(form2.getItems()[2]);
  }
  Utilities.sleep(1500);
  formLength = form2.getItems().length;
  Logger.log(formLength);
  if (ss2.getLastColumn() - formLength > 1)
  {
    ss2.deleteColumns(4, ss2.getLastColumn()-formLength-1);
  }
  
  var ss3 = spreadSheet.getSheetByName('Form Responses 3');
  var form3 = FormApp.openById('1d2eFekGlG7gN4p2dTrV0eRSLZM7GLBhwacXpF67fXQU');
  form3.deleteAllResponses();
  if (ss3.getLastRow() > 1)
  {
    ss3.deleteRows(2, ss3.getLastRow()-1);
  }
  
  var ss4 = spreadSheet.getSheetByName('Form Responses 4');
  var form4 = FormApp.openById('1CT8BZBZ19qMOWmOGRlkORZMWUrvQCu0qWaxrMnTyLBs');
  form4.deleteAllResponses();
  while(form4.getItems().length > 2)
  {
    form4.deleteItem(form4.getItems()[2]);
  }
  Utilities.sleep(2500);
  if (ss4.getLastRow() > 1)
  {
    ss4.deleteRows(2, ss4.getLastRow()-1);
  }
  formLength = form4.getItems().length;
  if (ss4.getLastColumn() - formLength > 1)
  {
    ss4.deleteColumns(4, ss4.getLastColumn()-formLength-1);
  }
}

function getFirstEmptyRow(sheetName) {
  var spreadSheet = SpreadsheetApp.openById('1c_glzdHTinakGJNCJZsWh18e1HLLJa9fOaZjrCoa4is');
  var spr = spreadSheet.getSheetByName(sheetName);
  var column = spr.getRange('A:A');
  var values = column.getValues(); // get all data in one call
  var ct = 0;
  while ( values[ct][0] != "" ) {
    ct++;
  }
  return (ct);
}

function topLaw() {
  var spreadSheet = SpreadsheetApp.openById('1c_glzdHTinakGJNCJZsWh18e1HLLJa9fOaZjrCoa4is');
  var ss = spreadSheet.getSheetByName('Form Responses 2');
  var sum = 0;
  var columnNum = 3;
  var lastRow = ss.getLastRow();
  for(var i = 3; i<ss.getLastColumn();i++)
  {
    counter = 0;
    var range = ss.getRange(2, i+1, lastRow-1);
    var values = range.getValues();
    for(var j = 0; j<range.getNumRows();j++)
    {
      counter += values[j][0];
    }
    if(counter > sum)
    {
      sum = counter;
      columnNum = i;
    }
  }
  title = ss.getRange(1, columnNum+1);
  return title.getValue();
}

function topOutcome() {
  var spreadSheet = SpreadsheetApp.openById('1c_glzdHTinakGJNCJZsWh18e1HLLJa9fOaZjrCoa4is');
  var ss = spreadSheet.getSheetByName('Form Responses 4');
  var sum = 0;
  var columnNum = 3;
  var lastRow = ss.getLastRow();
  for(var i = 3; i<ss.getLastColumn();i+=2)
  {
    counter = 0;
    var range = ss.getRange(2, i+1, lastRow-1);
    var values = range.getValues();
    for(var j = 0; j<range.getNumRows();j++)
    {
      counter += values[j][0];
    }
    if(counter > sum)
    {
      sum = counter;
      columnNum = i;
    }
  }
  title = ss.getRange(1, columnNum+1);
  Logger.log(title.getValue());
  return title.getValue();
}

function topMeasure() {
  var spreadSheet = SpreadsheetApp.openById('1c_glzdHTinakGJNCJZsWh18e1HLLJa9fOaZjrCoa4is');
  var ss = spreadSheet.getSheetByName('Form Responses 4');
  var sum = 0;
  var columnNum = 4;
  var lastRow = ss.getLastRow();
  for(var i = 4; i<ss.getLastColumn();i+=2)
  {
    counter = 0;
    var range = ss.getRange(2, i+1, lastRow-1);
    var values = range.getValues();
    for(var j = 0; j<range.getNumRows();j++)
    {
      counter += values[j][0];
    }
    if(counter > sum)
    {
      sum = counter;
      columnNum = i;
    }
  }
  title = ss.getRange(1, columnNum+1);
  Logger.log(title.getValue());
  return title.getValue();
}

