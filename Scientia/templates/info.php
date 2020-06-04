<?php

$connect = mysql_connect(“</localhost:3306>”, “root”, “vijay4004”); 
if (!connect) { die('Connection Failed: ' . mysql_error()); 
    { 
        mysql_select_db(“employees”, $connect);
        $user_info = “INSERT INTO empdetails (name,designation,address,phone) VALUES ('$_POST[name]', '$_POST[designation]', '$_POST[address]', '$_POST[phone]')”; 
        if (!mysql_query($user_info, $connect)) { die('Error: ' . mysql_error()); }

        echo “Employee information added to the database.”;

        mysql_close($connect); 
    }
?>