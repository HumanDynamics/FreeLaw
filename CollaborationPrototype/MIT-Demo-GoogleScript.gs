function getFirstEmptyRow() {
  var spr = SpreadsheetApp.getActiveSpreadsheet();
  var column = spr.getRange('A:A');
  var values = column.getValues(); // get all data in one call
  var ct = 0;
  while ( values[ct][0] != "" ) {
    ct++;
  }
  return (ct);
}

function makeForm()
{
  var ss = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var form = FormApp.create('MIT.edu/Law Collective Creation Prototype');
  form.addTextItem().setTitle('Name').setRequired(true);
  form.addTextItem().setTitle('Email').setRequired(true);
  for (var i = 2; i<getFirstEmptyRow(); i++)
  {
    var item = form.addScaleItem();
    item.setTitle('Rate ' + ss.getRange("B" + i).getValue()).setBounds(1, 5);
  }
}

/**
 *  This was Google Script was hacked with Dazza Greenwood at the Code for America 
 *  Bostob Brigade Tuesday Hack Night by Kenshin Maybe (who is a collaborator of MIT 
 *  Computational Law team on this project).  
 * 
 *  For more info on thus project, check out the Wiki of this GitHub Repository and MIT.edu/Law 
 **/
