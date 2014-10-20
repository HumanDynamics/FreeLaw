	
<?php	include("conn.php");
			
	if (isset($_GET['name'])) {
		$name = $_GET['name'];
	} else {
		$name = '';
	}
	
	if (isset($_GET['email'])) {
		$email = $_GET['email'];
	} else {
		$email = '';
	}
	
	if (isset($_GET['law'])) {
		$law = $_GET['law'];
	} else {
		$law = '';
	}
	
	//echo $name.' '.$email.' '.$law;
		
	
	$sql="INSERT INTO TEST
	(name, email, law, headline, rate_headline, blurb, rate_blurb)
		VALUES 
	('$name', '$email', '$law', '', '', '', '' )";
	
	$rs=odbc_exec($conn,$sql);
	if (!$rs) {exit("Error in SQL");} 
	
	
	//$Message = 'Submitted successfully';
	//header("Location:test_form.php?Message=".$Message);
	
?>
