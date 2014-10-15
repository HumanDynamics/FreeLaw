<?php

if (isset($_POST['name'])) {
    $name = $_POST['name'];
} else {
    $name = '';
}

if (isset($_POST['email'])) {
    $email = $_POST['email'];
} else {
    $email = '';
}

if (isset($_POST['law'])) {
    $law = $_POST['law'];
} else {
    $law = '';
}

echo $name.' '.$email.' '.$law;

///insert into sql database here
?>
