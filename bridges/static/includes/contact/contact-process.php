<?php
define( "WEBMASTER_EMAIL", 'your-email@domain.com' );

$error = false;
$fields = array( 'name', 'email', 'subject', 'message' );

foreach ( $fields as $field ) {
	if ( empty( $_POST[$field] ) || trim( $_POST[$field] ) == '' )
		$error = true;
}

if ( ! $error ) {
	$name = stripslashes( $_POST['name'] );
	$email = trim( $_POST['email'] );
	$subject = stripslashes( $_POST['subject'] );
	$message = stripslashes( $_POST['message'] );

	$mail = @mail( WEBMASTER_EMAIL, $subject, $message,
		 "From: " . $name . " <" . $email . ">\r\n"
		."Reply-To: " . $email . "\r\n"
		."X-Mailer: PHP/" . phpversion() );

	if ( $mail ) {
		echo "Success";
	} else {
		echo "Error";
	}
}
?>