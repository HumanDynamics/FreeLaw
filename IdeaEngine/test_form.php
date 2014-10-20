<!DOCTYPE html>
<html>
<head>
	<title>Test Form for Propose Law</title>
	<!--created by Karin
	Creative Commons 0 license-->
</head>

<body>
<?php

$nameErr = $emailErr = $lawErr = "";
$name = $email = $law= "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
   if (empty($_POST["name"])) {
     $nameErr = "Name is required";
   } else {
     $name = test_input($_POST["name"]);
     if (!preg_match("/^[a-zA-Z ]*$/",$name)) {
       $nameErr = "Only letters and white space allowed"; 
     }
   }
   
   if (empty($_POST["email"]))
     {$emailErr = "Email is required";}
     else
     {$email = test_input($_POST["email"]);
	 	 if (!preg_match("/([\w\-]+\@[\w\-]+\.[\w\-]+)/",$email))
       {
       $emailErr = "Invalid email format"; 
       }
	 }

   if (empty($_POST["law"])) {
     $lawErr = "Law is required";
   } else {
     $law = test_input($_POST["law"]);
   }

	
	 if ($nameErr == "" & $emailErr == "" & $lawErr == ""){
	
	  header("Location: test_formPro.php?&name=".$name."&email=".$email."&law=".$law); 
	  }	 
	
}

function test_input($data)
{
     $data = trim($data);
     $data = stripslashes($data);
     $data = htmlspecialchars($data);
     return $data;
	 
	 	 
}
?>
	<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" > 
	We need the following new or updated law: <input type="text" name="law" value="<?php echo $law;?>"><span class="error">* <?php echo $lawErr;?></span><br>
	Name: <input type="text" name="name" value="<?php echo $name;?>"><span class="error">* <?php echo $nameErr;?></span><br>
	E-mail: <input type="text" name="email" value="<?php echo $email;?>"><span class="error">* <?php echo $emailErr;?></span><br>
	<input type="submit" value= "Add Item">
	</form>

	<div id="update"></div>
</body>

</html>
