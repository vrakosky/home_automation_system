<!doctype html>
<html lang="fr">
    <head>
        
        <meta charset="utf-8">
        <title>Contrôle GPIO</title>
        
        <link rel="stylesheet" type="text/css" href="stylesheet.css">
        
    </head>
    <body>
        
        <form action="script.php" method="get">
            <input type="submit" name="executer" value="ON" class="button" id="ON">
            <br/>
            <input type="submit" name="executer" value="OFF" class="button" id="OFF">
	    <br/>
	    <input type="submit" name="executer" value="ON_dim" class="button" id="ON_dim">
            <br/>
            <input type="submit" name="executer" value="OFF_dim" class="button" id="OFF_dim">
	    <br/>
            <input type="submit" name="executer" value="ON_pwm" class="button" id="ON_pwm">
            <br/>
            <input type="submit" name="executer" value="OFF_pwm" class="button" id="OFF_pwm">
	    <br/>
	    <input type="submit" name="executer" value="ON_alarm" class="button" id="ON_alarm">
            <br/>
            <input type="submit" name="executer" value="OFF_alarm" class="button" id="OFF_alarm">
            <br/>
            <input type="submit" name="executer" value="ON_all" class="button" id="ON_all">
            <br/>
            <input type="submit" name="executer" value="OFF_all" class="button" id="OFF_all">
	    <br/>
            <input type="submit" name="executer" value="music" class="button" id="music">
	    <br/>
            <input type="submit" name="executer" value="offmusic" class="button" id="offmusic">
        </form>
    </body>
</html>
