<?php
system("gpio -g write 4 0");
system("gpio -g mode 4 out");
system("gpio -g mode 17 out");
system("gpio -g mode 27 out");

//LED1 : Normal
    if($_GET['executer'] == 'ON')
    {
        system("gpio -g write 4 1");
    }
    else
    {
        system("gpio -g write 4 0");
    }

//LED2 : Dimming
    if($_GET['executer'] == 'ON_dim')
    {
	//exec("sudo python /var/www/html/dimLED.py");
	$command = escapeshellcmd("sudo python /var/www/html/dimLED.py");
	exec($command);

    }
    elseif ($_GET['executer'] == 'OFF_dim')
    {
	//exec("sudo pkill -f /var/www/html/dimLED.py");
        exec("sudo pkill -f dimLED.py");
        system("gpio -g write 17 0");
    }

//LED3 : PWM
    if($_GET['executer'] == 'ON_pwm')
    {
        exec("sudo python /var/www/html/pwmLED.py");
    }
    elseif ($_GET['executer'] == 'OFF_pwm')
    {   
	exec("sudo pkill -f pwmLED.py");
	system("gpio -g write 4 0");
    }

//LED4 : Alarm
    if($_GET['executer'] == 'ON_alarm')
    {
        exec("sudo python /var/www/html/alarm.py");
    }
    elseif ($_GET['executer'] == 'OFF_alarm')
    {
        exec("sudo pkill -f alarm.py");
        system("gpio -g write 17 0");
    }

//LED5 : ALL
    if($_GET['executer'] == 'ON_all')
    {
        system("gpio -g write 4 1");
	system("gpio -g write 17 1");
	system("gpio -g write 27 1");

    }
    elseif ($_GET['executer'] == 'OFF_all')
    {
	system("gpio -g write 4 0");
        system("gpio -g write 17 0");
        system("gpio -g write 27 0");
    }

//Music : Play music
    if($_GET['executer'] == 'music')
    {
        exec("aplay /home/pi/music/weeknd.wav");
    }
    elseif ($_GET['executer'] == 'offmusic')
    {
        system("sudo pkill -f aplay;");
    }


   header('Location: index.php');
?>

 
