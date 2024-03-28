Title: Contact Me
Menu: SideZ

Use this form to send me a message and I will reply to you shortly. Thank you.

<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/emailjs-com@2.3.2/dist/email.min.js"></script>
<script type="text/javascript">
    (function(){
        emailjs.init("XvZA_Lwwxjs5ASDE0");
    })();
</script>

<script type="text/javascript">
    window.onload = function() {
	document.getElementById('contact-form').addEventListener('submit', function(event) {
	    event.preventDefault();
	    emailjs.sendForm('default_service', 'contact_form', this)
	    .then(function(response) {
		alert('Your e-mail has been sent.');
		window.location.reload(false);
	    }, function(error) {
		alert('Your e-mail could not be sent: ' + error);
	    });
	});
    }
</script>

<form id="contact-form">
  <p><label><b>Your name:</b><br>
      <input type="text" name="user_name"
             placeholder="John Doe" size="50" required>
  </label></p>
  <p><label><b>Your e-mail address:</b><br>
      <input type="email" name="user_email"
             placeholder="john.doe@big_company.com" size="50" required>
  </label></p>
  <p><label><b>Subject:</b><br>
      <input type="text" name="subject" size="50" required>
  </label></p>
  <p><label><b>Message:</b><br>
      <textarea name="message" cols="80" rows="6" required></textarea>
  </label></p>

  <p><label>
      <!-- Client-side validation is a bit silly, but it's something. -->
      The following question is for testing whether you are a human
      visitor and to prevent automated spam submissions.<br>
      <b>What is my favorite art medium?</b><br>
      <input type="text" name="medium" size="10" required
             pattern="[Gg][Ll][Aa][Ss][Ss]"><br>
      <i>Hint: One word only, five letters total.</i>
  </label></p>

  <input type="submit" value="Send e-mail">
</form>
